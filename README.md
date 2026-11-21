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

