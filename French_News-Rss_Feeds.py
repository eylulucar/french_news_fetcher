#french_news_fetcher by eylulucar

import html
import re
import time
from datetime import datetime
import feedparser
import requests

# ==========================================
# AYARLANABİLİR PARAMETRELER (CONFIGURATION)
# ==========================================

# Tamamı Fransızca güvenilir eğitim ve güncel haber RSS kaynakları
RSS_SOURCES = {
    "1jour1actu - Actualités": "https://www.1jour1actu.com/feed",
    "Français Authentique - Blog": "https://www.francaisauthentique.com/feed/",
    "TV5MONDE - Info & Culture": "https://information.tv5monde.com/rss.xml",
}

# Sitelerin bot engellemesini aşmak için standart tarayıcı kimliği (User-Agent)
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml, text/xml, */*",
}

# Temizlenecek standart reklam, oynatıcı ve imza şablonları (Regex desenleri)
BOILERPLATE_PATTERNS = [
    r"L'article .*? apparaît en premier sur 1jour1actu\.com\s*\.",
    r"L'article .*? a été publié la première fois sur .*?\.",
    r"Par TV5MONDE .*? TV5 JWPlayer Field",
    r"Ressource\(s\) évoquée\(s\) dans l’épisode\s*:",
    r"Télécharge notre application mobile gratuite mise à jour",
    r"\(Fais un clic droit sur ce lien pour enregistrer le fichier MP3\)",
    r"Abonne-toi à la chaîne YouTube pour ne manquer aucune vidéo\s*:\s*clique ici\.",
    r"Télécharge le fichier MP3 ici\.",
    r"Transcription de (l’épisode|la vidéo)\s*:",
]

# A1-B2 seviyesi için filtreleme sınırları (Kelime sayısı bazında)
MIN_WORDS = 12
MAX_WORDS = 150
ARTICLES_PER_SOURCE = 3


# ==========================================
# 1. TEMİZLEME VE FİLTRELEME KATMANI
# ==========================================
def clean_text_content(raw_text: str) -> str:
    """
    HTML karakter kodlarını çözer, HTML etiketlerini kaldırır ve
    BOILERPLATE_PATTERNS listesindeki tekrarlayan şablon ifadeleri siler.
    """
    if not raw_text:
        return ""

    # 1. Adım: HTML karakter kodlarını (&#160;, &#8217; vb.) gerçek karaktere çevir
    text = html.unescape(raw_text)

    # 2. Adım: Tüm HTML etiketlerini (<p>, <br>, <a...> vb.) temizle
    text = re.sub(r"<.*?>", " ", text)

    # 3. Adım: Tanımlı şablon cümleleri döngü ile metinden çıkar
    for pattern in BOILERPLATE_PATTERNS:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    # 4. Adım: Fazla boşlukları tek boşluğa indir ve kenarları kırp
    clean_text = re.sub(r"\s+", " ", text).strip()
    return clean_text


def is_french_text(text: str) -> bool:
    """
    Metnin yanlışlıkla İngilizce açıklamalar içerip içermediğini kontrol eder.
    Basit bir anahtar kelime kontrolü (Heuristic) kullanır.
    """
    english_markers = {"the", "and", "for", "with", "this", "published", "lesson"}
    words = set(re.findall(r"\b[a-z]+\b", text.lower()))
    return len(words.intersection(english_markers)) < 2


def is_suitable_level(text: str, min_words: int, max_words: int) -> bool:
    """
    Metnin hem Fransızca olduğunu hem de belirlenen A-B kuru
    kelime sayısı sınırları içinde kaldığını doğrular.
    """
    if not is_french_text(text):
        return False

    word_count = len(text.split())
    return min_words <= word_count <= max_words


# ==========================================
# 2. VERİ ÇEKME KATMANI (HTTP REQUEST + RSS)
# ==========================================
def fetch_articles(sources: dict) -> list:
    """
    Tarayıcı kimliği kullanarak RSS kaynaklarına bağlanır,
    XML verisini indirir, ayrıştırır ve uygun içerikleri döndürür.
    """
    collected_articles = []

    for source_name, url in sources.items():
        print(f"Bağlanılıyor: {source_name}...")

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.content)
        except requests.exceptions.RequestException as error:
            print(f"  [Hata] {source_name} bağlantısı başarısız: {error}")
            continue

        if not feed.entries:
            print(f"  [Uyarı] {source_name} kaynağında içerik bulunamadı.")
            continue

        added_count = 0
        for entry in feed.entries:
            if added_count >= ARTICLES_PER_SOURCE:
                break

            title = clean_text_content(entry.get("title", "Başlıksız İçerik"))
            raw_summary = entry.get("summary", entry.get("description", ""))
            clean_summary = clean_text_content(raw_summary)
            link = entry.get("link", "")
            published = entry.get("published", "Tarih belirtilmemiş")

            if is_suitable_level(clean_summary, MIN_WORDS, MAX_WORDS):
                collected_articles.append({
                    "source": source_name,
                    "title": title,
                    "summary": clean_summary,
                    "word_count": len(clean_summary.split()),
                    "link": link,
                    "published": published,
                })
                added_count += 1

        print(f"  -> {added_count} adet uygun Fransızca içerik alındı.")
        time.sleep(1)

    return collected_articles


# ==========================================
# 3. ÇIKTI VE RAPORLAMA KATMANI (MARKDOWN)
# ==========================================
def save_to_markdown(articles: list) -> str:
    """
    Toplanan ve filtrelenen makaleleri düzenli bir Markdown (.md)
    dosyasına kaydeder ve dosya adını döndürür.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"fransizca_okuma_listesi_{today_str}.md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# Fransızca Okuma Listesi (A1–B2 Düzeyi)\n")
        file.write(f"**Oluşturulma Tarihi:** {today_str} | **Toplam İçerik:** {len(articles)}\n\n")
        file.write("---\n\n")

        if not articles:
            file.write("Kriterlere uygun yeni içerik bulunamadı.\n")
            return filename

        for index, item in enumerate(articles, start=1):
            file.write(f"### {index}. {item['title']}\n")
            file.write(f"- **Kaynak:** {item['source']}\n")
            file.write(f"- **Kelime Sayısı:** {item['word_count']} kelime\n")
            file.write(f"- **Yayın Tarihi:** {item['published']}\n\n")
            file.write(f"> {item['summary']}\n\n")
            file.write(f"[Makalenin Tamamını Oku]({item['link']})\n\n")
            file.write("---\n\n")

    return filename


# ==========================================
# ANA PROGRAM AKIŞI (MAIN EXECUTION)
# ==========================================
if __name__ == "__main__":
    print("=== Fransızca Eğitim İçeriği Toplayıcı (v3.1 - Nihai Sürüm) Başlatıldı ===\n")

    articles_list = fetch_articles(RSS_SOURCES)
    output_file = save_to_markdown(articles_list)

    print(f"\nİşlem tamamlandı! Toplam {len(articles_list)} adet saf Fransızca içerik bulundu.")
    print(f"Dosya kaydedildi: {output_file}")
