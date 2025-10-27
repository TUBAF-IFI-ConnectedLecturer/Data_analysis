# OPAL Data Analysis Project

Ein umfassendes Datenanalyseprojekt zur Verarbeitung und Analyse von OPAL-Bildungsressourcen mit Fokus auf Ähnlichkeitsberechnung, Keyword-Extraktion und Klassifikation.

## Übersicht

Dieses Projekt analysiert Bildungsressourcen aus der OPAL-Plattform (Online-Plattform für Akademisches Lehren und Lernen) durch verschiedene Ähnlichkeitsmetriken, automatische Keyword-Extraktion und DDC-basierte Klassifikation.

## Projektstruktur

```
Data_analysis/
├── README.md                           # Diese Datei
├── Pipfile                            # Python Dependency Management
├── Pipfile.lock                       # Locked Dependencies
├── src/                               # Source Code
│   ├── DataHandler.py                 # Zentraler Datenhandler
│   ├── ConfigManager.py               # Konfigurationsmanagement
│   └── checkAuthorNames.py            # Autorennamen-Validierung
├── OPAL/                              # Hauptanalyseverzeichnis
│   ├── config.yaml                    # Hierarchische Konfiguration
│   ├── classification/                # Klassifikations-Notebooks
│   │   ├── 00_extractKeywords.ipynb   # Keyword-Extraktion & DDC-Mapping
│   │   ├── 01_buildSimilarityMatrixes.ipynb # Ähnlichkeitsmatrizen
│   │   ├── 02_buildSimilartyFrame.ipynb     # Ähnlichkeits-Frameworks
│   │   ├── 03_compareWithZeidler.ipynb     # Vergleichsstudien
│   │   └── 04_addAttributs.ipynb           # Attributerweiterung
│   ├── names/                         # Autorennamen-Analyse
│   │   └── check_names.ipynb          # Namensprüfung & -normalisierung
│   └── queries/                       # Query-Notebooks
│       └── main.ipynb                 # Hauptabfragen
├── LiaScript/                         # LiaScript-spezifische Analysen
│   ├── 01_aggregate_features.ipynb    # Feature-Aggregation
│   ├── 97_historical_overview.ipynb   # Historische Übersicht
│   └── inspectLia.ipynb              # LiaScript-Inspektion
└── archive/                          # Archivierte Analysen
    ├── general_Metadataanalysis/      # Allgemeine Metadatenanalyse
    ├── OPAL_Dewey/                   # Dewey-Klassifikationsanalysen
    └── OPAL_Similarity/              # Ähnlichkeitsanalysen
```

## Datenstruktur

Das Projekt verwendet eine hierarchische Datenorganisation:

### Raw Data (`/media/sz/Data/Connected_Lecturers/Opal_transfer/raw/`)
```
raw/
├── content/                          # Volltext-Inhalte der Materialien
├── files/                           # Datei-Metadaten
├── OPAL_ai_meta.p                   # KI-generierte Metadaten
├── OPAL_files_meta.p                # Grundlegende Dateimetadaten
├── OPAL_files_attrib.p              # Erweiterte Dateiattribute
├── OPAL_files_filtered.p            # Gefilterte Datensätze
└── OPAL_content.p                   # Verarbeitete Inhalte
```

### Processed Data (`/media/sz/Data/Connected_Lecturers/Opal_transfer/processed/`)
```
processed/
├── keywords/                        # Keywords & Klassifikation
│   ├── keyword_list.p               # Extrahierte Keywords
│   ├── keyword_list.csv             # Keywords in CSV-Format
│   └── ddc_keywords.p               # DDC-klassifizierte Keywords
├── similarity/                      # Ähnlichkeitsmatrizen
│   ├── ai_similarity_matrix.p       # KI-basierte Ähnlichkeiten
│   ├── minhash_text_similarity.p    # MinHash-Textähnlichkeiten
│   ├── keyword_cosine_similarity.p  # Cosinus-Ähnlichkeit (Keywords)
│   ├── keyword_jaccard_similarity.p # Jaccard-Ähnlichkeit
│   ├── keyword_weighted_jaccard_similarity.p # Gewichtete Jaccard
│   ├── keyword_tfidf_cosine_similarity.p     # TF-IDF Cosinus
│   ├── keyword_overlap_similarity.p          # Overlap-Koeffizient
│   ├── keyword_dice_similarity.p             # Dice-Koeffizient
│   └── keyword_hierarchical_similarity.p     # Hierarchische Ähnlichkeit
└── analysis/                        # Kombinierte Analysen
    └── similarity_all_metrics.p     # Alle Ähnlichkeitsmetriken zusammengefasst
```

## Verarbeitungskette

### 1. Datenaufbereitung
- **Eingabe**: Rohdaten aus OPAL-Plattform
- **Verarbeitung**: Bereinigung, Normalisierung, Filterung
- **Ausgabe**: Strukturierte Metadaten und Inhalte

### 2. Keyword-Extraktion (`00_extractKeywords.ipynb`)
```python
# Hauptschritte:
1. Laden der Metadaten (df_aimeta)
2. DDC-Nummern-Extraktion aus URLs
3. Keyword-Validierung über GND (Gemeinsame Normdatei)
4. Erstellung von DDC-Labels für Materialien
5. Speicherung der verarbeiteten Keywords
```

**Features:**
- ✅ GND-Validierung für Keyword-Qualität
- ✅ DDC-Hierarchie-Mapping
- ✅ Statistische Keyword-Analyse
- ✅ Duplikat-Behandlung

### 3. Ähnlichkeitsberechnung (`01_buildSimilarityMatrixes.ipynb`)

#### 3.1 Keyword-basierte Ähnlichkeiten
```python
# Implementierte Algorithmen:
- Standard Jaccard Similarity
- Weighted Jaccard (Häufigkeitsgewichtet)
- TF-IDF Cosinus-Ähnlichkeit
- Overlap Coefficient (Szymkiewicz-Simpson)
- Dice Coefficient (Sørensen-Dice)
- Hierarchical Similarity (DDC-Baumstruktur)
- Cosinus-Ähnlichkeit (DDC-Vektoren)
```

#### 3.2 Content-basierte Ähnlichkeiten
```python
# Algorithmen:
- KI-basierte Ähnlichkeitsmatrizen
- MinHash für Text-Ähnlichkeit
- Konfigurierbare Textfeatures (Content/Title/Keywords)
```

### 4. Erweiterte Analysen
- **Ähnlichkeits-Frameworks**: Kombination verschiedener Metriken
- **Vergleichsstudien**: Benchmarking mit etablierten Methoden
- **Attributerweiterung**: Anreicherung mit zusätzlichen Metadaten

## Technische Komponenten

### DataHandler (`src/DataHandler.py`)
Zentraler Datenhandler mit folgenden Features:
- ✅ Einheitliche Lade-/Speicher-API
- ✅ Automatische Ordnererstellung
- ✅ Performance-Monitoring (Dateigröße, Timestamp, Dauer)
- ✅ Hierarchische Konfigurationsunterstützung

```python
# Beispielverwendung:
dataHandler = DataHandler("config.yaml")
df = dataHandler.load_data("data_files.raw_data.df_aimeta")
dataHandler.save_data(result_df, "data_files.processed_data.keywords.df_keywordlist")
```

### ConfigManager (`src/ConfigManager.py`)
Hierarchisches Konfigurationsmanagement:
- ✅ YAML-basierte Konfiguration
- ✅ Pfad-Interpolation mit Ankern
- ✅ Logische Datengruppierung
- ✅ Skalierbare Organisationsstruktur

## Ähnlichkeitsmetriken

### Keyword-basierte Metriken

| Metrik | Beschreibung | Verwendung |
|--------|-------------|------------|
| **Standard Jaccard** | `|A ∩ B| / |A ∪ B|` | Grundlegende Set-Ähnlichkeit |
| **Weighted Jaccard** | Häufigkeitsgewichtet | Berücksichtigt Keyword-Häufigkeiten |
| **TF-IDF Cosinus** | Seltene Keywords höher gewichtet | Fokus auf diskriminierende Keywords |
| **Overlap Coefficient** | `|A ∩ B| / min(|A|, |B|)` | Gut für unterschiedliche Dokumentgrößen |
| **Dice Coefficient** | `2|A ∩ B| / (|A| + |B|)` | Doppelgewicht auf Überschneidungen |
| **Hierarchical Similarity** | DDC-Baumstruktur-basiert | Berücksichtigt fachliche Hierarchien |

### Content-basierte Metriken

| Metrik | Beschreibung | Verwendung |
|--------|-------------|------------|
| **MinHash** | Locality-Sensitive Hashing | Effiziente Text-Ähnlichkeit |
| **KI-Similarity** | Deep Learning basiert | Semantische Ähnlichkeiten |

## Installation & Setup

### 1. Abhängigkeiten installieren
```bash
# Mit pipenv (empfohlen)
pip install pipenv
pipenv install

# Oder mit pip
pip install -r requirements.txt
```

### 2. Konfiguration anpassen
```yaml
# config.yaml - Pfade an lokale Umgebung anpassen
folder_structure:
  data_root: &BASE /path/to/your/data/folder
```

### 3. Notebooks ausführen
```bash
# Jupyter Notebook starten
jupyter notebook

# Oder mit VS Code
code .
```

## Verarbeitungsreihenfolge

1. **`00_extractKeywords.ipynb`** - Keyword-Extraktion und DDC-Mapping
2. **`01_buildSimilarityMatrixes.ipynb`** - Ähnlichkeitsmatrizen berechnen
3. **`02_buildSimilartyFrame.ipynb`** - Ähnlichkeits-Frameworks erstellen
4. **`03_compareWithZeidler.ipynb`** - Vergleichsstudien durchführen
5. **`04_addAttributs.ipynb`** - Attribute erweitern

## Hauptziele

- **Automatisierte Klassifikation** von Bildungsressourcen
- **Ähnlichkeitsberechnung** für Empfehlungssysteme
- **Qualitätsbewertung** von Metadaten
- **Vergleichsstudien** verschiedener Ähnlichkeitsmetriken
- **Skalierbare Datenverarbeitung** für große Datensätze

## Datenqualität & Validation

### Keyword-Validierung
- ✅ GND-Normierung für einheitliche Begriffe
- ✅ DDC-Hierarchie-Konsistenz
- ✅ Statistische Ausreißer-Erkennung

### Ähnlichkeitsvalidierung
- ✅ Matrix-Symmetrie-Prüfung
- ✅ Wertebereich-Validation [0,1]
- ✅ Performance-Vergleiche verschiedener Metriken

## Erweiterungsmöglichkeiten

- **Graph-basierte Analysen** der Ähnlichkeitsnetzwerke
- **Machine Learning** für erweiterte Klassifikation
- **Real-time Processing** für Live-Datenströme
- **Web-Interface** für interaktive Analysen
- **API-Entwicklung** für externe Integration

## Lizenz & Nutzung

Dieses Projekt ist Teil der Forschungsarbeit zu automatisierten Bildungsressourcen-Analysen. Bei Verwendung in akademischen Arbeiten bitte entsprechend zitieren.

## Mitwirkende

- Entwicklung: Connected Lecturers Projekt
- Institution: TU Bergakademie Freiberg
- Fachbereich: Informatik

---

*Letzte Aktualisierung: Juli 2025*
