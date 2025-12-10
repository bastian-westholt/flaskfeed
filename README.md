# FlaskFeed

Ein modernes, minimalistisches Blog-System gebaut mit Flask und Python.

![Python](https://img.shields.io/badge/python-3.13-blue)
![Flask](https://img.shields.io/badge/flask-latest-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## Übersicht

FlaskFeed ist eine leichtgewichtige Blog-Plattform, die es Nutzern ermöglicht, Posts zu erstellen, zu bearbeiten, zu löschen und zu liken. Das Projekt nutzt JSON als einfache Datenbank und bietet ein responsives, dunkles UI-Design mit Neon-Akzenten.

## Features

- **Posts erstellen** - Neue Blog-Posts mit Autor, Titel und Content
- **Posts bearbeiten** - Bestehende Posts aktualisieren
- **Posts löschen** - Unerwünschte Posts entfernen
- **Like-System** - Posts können geliked werden
- **Modernes UI** - Dunkles Design mit mediumspringgreen Akzenten
- **Responsive** - Funktioniert auf allen Bildschirmgrößen
- **JSON Storage** - Einfache Datenpersistenz ohne Datenbank

## Technologien

- **Backend:** Flask (Python 3.13)
- **Frontend:** HTML5, CSS3 (Grid/Flexbox)
- **Icons:** Google Material Symbols
- **Font:** JetBrains Mono
- **Storage:** JSON File-based Database

## Installation

### Voraussetzungen

- Python 3.13+
- pip

### Setup

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd flaskfeed
   ```

2. **Virtuelle Umgebung erstellen**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # oder
   .venv\Scripts\activate  # Windows
   ```

3. **Dependencies installieren**
   ```bash
   pip install flask
   ```

4. **Starten**
   ```bash
   python app.py
   ```

5. **Browser öffnen**
   ```
   http://localhost:5001
   ```

## Projektstruktur

```
flaskfeed/
├── app.py                  # Flask Backend & Routes
├── data/
│   └── storage.json        # JSON Datenbank
├── static/
│   └── style.css          # CSS Styling
├── templates/
│   ├── index.html         # Hauptseite (Feed)
│   ├── add.html           # Post erstellen
│   └── update.html        # Post bearbeiten
├── .gitignore
└── README.md
```

## Routes

| Route | Methode | Beschreibung |
|-------|---------|--------------|
| `/` | GET | Zeigt alle Posts |
| `/add` | GET/POST | Formular zum Erstellen eines Posts |
| `/update/<post_id>` | GET/POST | Post bearbeiten |
| `/delete/<post_id>` | GET | Post löschen |
| `/like/<post_id>` | POST | Post liken |

## Design Features

- **CSS Grid Layout** für Post-Struktur
- **Flexbox** für Button-Anordnung
- **Material Icons** für intuitive UI
- **Gradient Backgrounds** für Posts und Inputs
- **Hover Transitions** für interaktive Elemente
- **Color Scheme:**
  - Background: `#222222`
  - Accent: `mediumspringgreen`
  - Hover: `#ff9cf2` (Pink)
  - Delete: `#ff0e4f` (Red)

## Verwendung

### Post erstellen
1. Klicke auf den **+** Button im Header
2. Fülle Autor, Titel und Content aus
3. Klicke **SUBMIT**

### Post bearbeiten
1. Klicke auf das **Stift-Icon** am Post
2. Ändere die Felder
3. Klicke **UPDATE**

### Post löschen
1. Klicke auf das **Mülleimer-Icon** am Post
2. Post wird sofort gelöscht

### Post liken
1. Klicke auf das **Daumen-hoch-Icon**
2. Like-Counter erhöht sich

## Konfiguration

### Port ändern
In `app.py` (Zeile 77):
```python
app.run(host="0.0.0.0", port=5001, debug=True)
```

### Design anpassen
In `static/style.css`:
- Farben ändern (mediumspringgreen, #222222, etc.)
- Layout anpassen (Grid-Columns, Padding, etc.)

## Bekannte Einschränkungen

- Keine User-Authentication
- Keine Kommentar-Funktion
- JSON-basiert (nicht für Production geeignet)
- Keine Bild-Uploads

## Roadmap

- [ ] User Authentication
- [ ] Kommentar-System
- [ ] Markdown Support
- [ ] Bild-Uploads
- [ ] SQLite/PostgreSQL Integration
- [ ] REST API
- [ ] Docker Support

## Lizenz

MIT License - Frei verwendbar für persönliche und kommerzielle Projekte.

## Autor

**Bastian Westholt**
Masterschool Project 2025

## Beitragen

Pull Requests sind willkommen! Für größere Änderungen bitte zuerst ein Issue öffnen.

---

Made with Flask
