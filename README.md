# Swati Tirunal Corpus (WIP)

Dataset of Swati Tirunal's compositions with standard romanization and metadata. The primary objective is to make the data easy to parse with minimal processing/cleaning and facilitate any sort of application without hassle.

Lyrics and metadata are sourced from [swathithirunal.in](https://www.swathithirunal.in/), [karnatik.com](https://www.karnatik.com/) (with manual cleaning) and a couple of [books](#sources).

## Table of Contents

- [Swati Tirunal Corpus](#swati-tirunal-corpus)
  - [Romanization Approach](#romanization-approach)
  - [Directory Structure](#directory-structure)
  - [Data Structure](#data-structure)
    - [Sample Source File](#sample-source-file)
    - [Sample Dataset Item](#sample-dataset-item)
  - [Sources](#sources)

## Romanization Approach

In general the *sandhis*, punctuation, formatting of text from the site has been preserved except for where it contradicts the material in the books referenced (see sources below) with markers and can be reconstructed from the dataset. The transliteration scheme adopted is ALA-LC. Conjunct consonants in Malayalam are transliterated according to their constituent letters. For example:

- കലശോദ്ഭവാമ്പിത --> kalaśōdbhavāmpita
- കൊണ്ടന്നെ --> koṇṭanne

but

- പത്മനാഭ --> padmanābha **not** patmanābha

The following markers indicate formatting that was preserved from the source images on the website and the books:

- `-` at the end of lines
- `-->` to indicate the text after it was aligned right
- `<->` to indicate a large space between two words

Omitted markers:

- `-` separating words in one line

## Directory Structure

The dataset itself it stored in `/dataset/corpus.json` (see structure below) and the possible metadata values (ragams,talams,etc.) in
their respective CSV files in `/source/meta`. A master list of compositions is stored in `/source/meta/index.csv` and contains references to
the other metadata files which are structured similarly. For example:

```csv
id ,name            ,ragam ,talam ,type ,language
1  ,āj āyē          ,1     ,1     ,1    ,1
2  ,āj unīndē       ,2     ,2     ,2    ,1
3  ,ānandavalli     ,3     ,3     ,3    ,2
4  ,āndoḷikā vāhanē ,4     ,4     ,4    ,4
```

`corpus.json` is generated from the raw text files written in an ad-hoc format (see structure below) for each piece in `/source/texts` numbered by that composition's id in `index.csv`. The script that parses these files, compiles it is stored in `/source/scripts`.
The complete directory structure is as shown here:

```plaintext
.
├── dataset
│   └── corpus.json
└── source
    ├── meta
    │   ├── index.csv
    │   ├── language.csv
    │   ├── ragam.csv
    │   ├── talam.csv
    │   └── type.csv
    ├── scripts
    │   ├── compile_corpus.py
    │   └── process_karnatik.sh
    └── texts
        ├── 1.txt
        ├── 2.txt
        ├── 3.txt
        └── ....
```

## Data Structure

The main dataset file `corpus.json` is a list of compositions. Each composition has a `meta` object for metadata and a `sahityam` object which contains objects for
each section of the composition. Each section is a list (for multiple *charanams*) which contains lists of lines for each instance of that section in the lyrics.
Text for each line and metadata is transliterated according to the [ALA-LC standard for Malayalam](https://www.loc.gov/catdir/cpso/romanization/malayalam.pdf).

For simplicity's sake, hindustani compositions have been folded into the Pallavi-Anupallavi-Charanam structure (as they were on the site, with the introductory labelled as the *pallavi* and the rest as *charanams*). The project is very much a WIP and this might change.

The raw source text files containing only the lyrics and delimiters prefixed with $ for each section. The parser ignores empty lines so a line break between sections (or any two lines) for readability is valid and preferred for readability. ""Comments"" can be added an invalid section header or as the contents of an invalid section.

**Valid delimiters**:

- `$PALLAVI`
- `$ANUPALLAVI`
- `$CHARANAM`

### Sample Source File

```plaintext
$PALLAVI
ānandavalli! kuru mudamavirataṃ
ānandavalli!

$ANUPALLAVI
dīnajasantapatimirāmr̥tkiraṇāyitasuhasē
dhr̥taśukapōtavilāsini jaya paraṃ

$CHARANAM
jambhavimatamukhasēvitapadayugaḷē girirājasutē ghana-
sāralasitavidhukhaṇḍasadr̥śaniṭilē
śambhuvadanasarasīruhamadhupē
sārasākṣi! hr̥di vihara divāniśaṃ

$CHARANAM
kēśapāśajitasajalajaladanikarē padapaṅkajasēvaka-
khēdajālaśamanaikaparamacaturē
nāśitāghacaritē bhuvanatraya-
nāyikē vitara mē śubhamanupamaṃ

$CHARANAM
śāradēndurucimñjuḷatamavadanē munihr̥dayanivāsini
cārukundmukuḷōpamavararadanē
pārijātatarupallavacaraṇē
padmnābhasahajē hara mē śucaṃ
```

### Sample Dataset Item

```json
{
   "meta": {
      "id": "3",
      "name": "ānandavalli",
      "type": "kīrtanaṃ",
      "language": "saṃskr̥taṃ",
      "ragam": "nīlāmbarī",
      "talam": "ādi"
   },
   "sahityam": {
      "pallavi": [
         [
            "ānandavalli! kuru mudamavirataṃ",
            "ānandavalli!"
         ]
      ],
      "anupallavi": [
         [
            "dīnajasantapatimirāmr̥tkiraṇāyitasuhasē",
            "dhr̥taśukapōtavilāsini jaya paraṃ"
         ]
      ],
      "charanam": [
         [
            "jambhavimatamukhasēvitapadayugaḷē girirājasutē ghana-",
            "sāralasitavidhukhaṇḍasadr̥śaniṭilē",
            "śambhuvadanasarasīruhamadhupē",
            "sārasākṣi! hr̥di vihara divāniśaṃ"
         ],
         [
            "kēśapāśajitasajalajaladanikarē padapaṅkajasēvaka-",
            "khēdajālaśamanaikaparamacaturē",
            "nāśitāghacaritē bhuvanatraya-",
            "nāyikē vitara mē śubhamanupamaṃ"
         ],
         [
            "śāradēndurucimñjuḷatamavadanē munihr̥dayanivāsini",
            "cārukundmukuḷōpamavararadanē",
            "pārijātatarupallavacaraṇē",
            "padmnābhasahajē hara mē śucaṃ"
         ]
      ]
   }
}
```

## Sources

- A comprehensive website on the life and music of Swathi Thirunal. (n.d.). swathithirunal.in. [https://www.swathithirunal.in/](https://www.swathithirunal.in/)
- Chidamabara Vadyar, K. (Ed.). (1916). Swathi Thirunal Sangeetha Kruthikal. Kerala Sahitya Akademi.
- Sambasiva Sastri, K. (Ed.). (1932). Sangitakritis of Swati Sri Rama Varma Maharaja. Government Press, Trivandrum.
