[fransizca_okuma_listesi_2026-11-21.md](https://github.com/user-attachments/files/35220729/fransizca_okuma_listesi_2026-11-21.md)

# French News RSS Feeds Script

```python3 French_News-Rss_Feeds.py```

Fransızca haber kaynaklarından RSS Feeds çekme script'i

---


```markdown
 **Français**

# 🇫🇷 Générateur de Listes de Lecture en Français (Niveaux A1–B2)

Un script Python simple et éducatif conçu pour collecter, nettoyer et filtrer de courts résumés d'actualités et d'articles de blog en français à partir de sources fiables (**1jour1actu**, **Français Authentique**, **TV5MONDE**). Il est destiné aux lycéens et aux étudiants universitaires de niveaux débutant et intermédiaire (A1–B2).

Ce projet sert également de support pédagogique pour apprendre les bases de la programmation en Python et le nettoyage de données (*Data Sanitization*).

---

## ✨ Fonctionnalités

* **Lecture Multi-Flux RSS :** Récupère automatiquement les derniers articles de sites éducatifs francophones.
* **En-têtes de Navigateur (`User-Agent`) :** Utilise une identité de navigateur standard pour éviter le blocage des requêtes (`403 Forbidden`) par les serveurs web.
* **Nettoyage Intelligent du Texte :** Supprime les balises HTML (`<p>`, `<br>`), décode les caractères spéciaux (`&#160;`) et efface les textes promotionnels répétitifs grâce aux expressions régulières.
* **Filtre de Niveau et de Langue :** Sélectionne des textes courts selon le nombre de mots (`MIN_WORDS` – `MAX_WORDS`) et élimine les descriptions en anglais.
* **Exportation Automatique en Markdown :** Crée un fichier `.md` daté, clair et prêt à être utilisé comme fiche de lecture.

---

## 🏗️ Architecture du Code (Comment ça marche ?)

Le script est divisé en **3 étapes principales** :

```text
[Sources de Flux RSS] 
       │
       ▼ (1. Collecte des données : requests + feedparser)
[Données Brutes XML / HTML] 
       │
       ▼ (2. Nettoyage & Filtrage : html.unescape + Regex + Compteur de mots)
[Textes Courts en Français] 
       │
       ▼ (3. Génération du rapport : Écriture de fichier)
[fransizca_okuma_listesi_AAAA-MM-JJ.md]

----
[fransizca_okuma_listesi_2026-11-21.md](https://github.com/user-attachments/files/35220729/fransizca_okuma_listesi_2026-11-21.md)

----

[ fransizca_okuma_listesi# Fransızca Okuma Listesi (A1–B2 Düzeyi)
**Oluşturulma Tarihi:** 2026-11-21 | **Toplam İçerik:** 9

---

### 1. Tes 3 infos de la semaine : les Restos du cœur, l’eau manque en Guyane, le succès mondial du jeu vidéo GTA 6
- **Kaynak:** 1jour1actu - Actualités
- **Kelime Sayısı:** 69 kelime
- **Yayın Tarihi:** Fri, 20 Nov 2026 01:00:00 +0000

> Ça s’est passé entre le 13 et le 19 novembre 2026 : les Restos du cœur ont repris leurs distributions de nourriture, l’eau manque en Guyane et les écoles ferment, le jeu GTA 6 est sorti. 1jour1actu te raconte. L'article Tes 3 infos de la semaine : les Restos du cœur, l’eau manque en Guyane, le succès mondial du jeu vidéo GTA 6 apparaît en premier sur 1jour1actu.com .

[Makalenin Tamamını Oku](https://www.1jour1actu.com/france/tes-3-infos-de-la-semaine-les-restos-du-coeur-leau-manque-en-guyane-le-succes-mondial-du-jeu-video-gta-6)

---

### 2. Les bonnes idées des enfants pour défendre leurs droits
- **Kaynak:** 1jour1actu - Actualités
- **Kelime Sayısı:** 53 kelime
- **Yayın Tarihi:** Fri, 20 Nov 2026 00:00:00 +0000

> Pour la Journée mondiale des droits de l'enfant qui a lieu le 20 novembre, ce sont des enfants comme toi qui ont écrit cette vidéo. Regarde, elle est pleine d'idées pour défendre les droits de l'enfant ! L'article Les bonnes idées des enfants pour défendre leurs droits apparaît en premier sur 1jour1actu.com .

[Makalenin Tamamını Oku](https://www.1jour1actu.com/monde/les-bonnes-idees-des-enfants-pour-defendre-leurs-droits)

---

### 3. C’est quoi un blocus ?
- **Kaynak:** 1jour1actu - Actualités
- **Kelime Sayısı:** 61 kelime
- **Yayın Tarihi:** Thu, 19 Nov 2026 00:00:00 +0000

> On entend beaucoup ce mot aux infos en ce moment pour parler des actions des lycéens. Car c’est un moyen pour eux de faire entendre leur besoin d’avoir de meilleures conditions pour étudier. Mais sais-tu que ce mot est aussi utilisé dans d’autres situations ? Découvre-le dans cette vidéo. L'article C’est quoi un blocus ? apparaît en premier sur 1jour1actu.com .

[Makalenin Tamamını Oku](https://www.1jour1actu.com/france/cest-quoi-un-blocus)

---

### 4. Et si une vie ordinaire était une vie réussie ?
- **Kaynak:** Français Authentique - Blog
- **Kelime Sayısı:** 16 kelime
- **Yayın Tarihi:** Wed, 18 Nov 2026 17:00:08 +0000

> ﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿ Salut et bienvenue dans ce nouvel épisode de Marchez avec Johan. C’est un plaisir de...

[Makalenin Tamamını Oku](https://www.francaisauthentique.com/et-si-une-vie-ordinaire-etait-une-vie-reussie/)

---

### 5. Et si la France quittait l’Union européenne ? (Café Avec Johan 23)
- **Kaynak:** Français Authentique - Blog
- **Kelime Sayısı:** 22 kelime
- **Yayın Tarihi:** Mon, 16 Nov 2026 17:00:04 +0000

> Salut ! Merci de me rejoindre dans cet épisode de Café avec Johan. C’est un plaisir pour moi de t’accueillir aujourd’hui. Et...

[Makalenin Tamamını Oku](https://www.francaisauthentique.com/et-si-la-france-quittait-lunion-europeenne-cafe-avec-johan-23/)

---

### 6. Accepter de redevenir débutant
- **Kaynak:** Français Authentique - Blog
- **Kelime Sayısı:** 28 kelime
- **Yayın Tarihi:** Wed, 11 Nov 2026 17:00:00 +0000

> ﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿ Salut et bienvenue dans ce nouvel épisode de Marchez avec Johan. Je suis très heureux que tu me rejoignes pour cette petite marche, et aujourd’hui, je voudrais...

[Makalenin Tamamını Oku](https://www.francaisauthentique.com/accepter-de-redevenir-debutant/)

---

### 7. 64' Débat : Londres se rapproche de Bruxelles, cinq ans après le Brexit
- **Kaynak:** TV5MONDE - Info & Culture
- **Kelime Sayısı:** 59 kelime
- **Yayın Tarihi:** 2026-11-21T19:47:35+00:00

> Par TV5MONDE NICOLAS GEORGE TV5 JWPlayer Field Le Royaume-Uni et l'Union européenne relancent leur coopération sur les échanges alimentaires, la mobilité des jeunes et le climat, ravivant les débats sur un éventuel rapprochement avec l'UE. On en parle avec Paul Taylor , journaliste spécialisé dans les affaires européennes et la maîtresse de conférences en civilisation britannique contemporaine Laëtitia Langlois.

[Makalenin Tamamını Oku](https://information.tv5monde.com/international/video/64-debat-londres-se-rapproche-de-bruxelles-cinq-ans-apres-le-brexit-2846649)

---

### 8. France : nouvelle mobilisation sociale
- **Kaynak:** TV5MONDE - Info & Culture
- **Kelime Sayısı:** 33 kelime
- **Yayın Tarihi:** 2026-11-21T18:47:52+00:00

> Par TV5MONDE PASCALE ACHARD TV5 JWPlayer Field Syndicats, étudiants et Gilets jaunes manifestent à Paris et dans plusieurs villes européennes pour réclamer de meilleures conditions de vie et une hausse du pouvoir d'achat.

[Makalenin Tamamını Oku](https://information.tv5monde.com/international/video/france-nouvelle-mobilisation-sociale-2846642)

---

### 9. Danemark : tensions avec la Russie
- **Kaynak:** TV5MONDE - Info & Culture
- **Kelime Sayısı:** 38 kelime
- **Yayın Tarihi:** 2026-11-21T18:47:45+00:00

> Par TV5MONDE MAY VALLAUD TV5 JWPlayer Field Copenhague accuse Moscou d'avoir planifié l'assassinat d'un rappeur ukrainien sur son territoire. En réponse, le Danemark a expulsé un diplomate russe et envisage de restreindre les visas Schengen aux ressortissants russes

[Makalenin Tamamını Oku](https://information.tv5monde.com/international/video/danemark-tensions-avec-la-russie-2846641)

---

_2026-11-21.md…]()


