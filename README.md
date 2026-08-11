# Analyse des finances locales des communes françaises

Projet d'analyse de données appliqué aux finances publiques locales, réalisé dans le cadre de mon portfolio de Business Analyst / Data Analyst junior.

## 🎯 Contexte et objectif

Fort de 3 ans d'alternance en DSI au sein d'une collectivité territoriale, j'ai voulu construire un projet qui combine compétences techniques (Python, pandas, data visualisation) et compréhension métier des enjeux budgétaires locaux.

**Questions traitées :**
1. Comment évolue l'épargne brute (autofinancement) des communes selon leur strate de population ?
2. Quelles strates de communes voient leur endettement progresser plus vite que leurs recettes ?
3. Quel est le poids de l'investissement dans les budgets communaux, et comment évolue-t-il dans le temps ?
4. Existe-t-il des écarts significatifs entre régions ou strates démographiques sur ces indicateurs ?

> *(À ajuster une fois le dataset exploré — garder 3 à 4 questions maximum, claires et mesurables.)*

## 📊 Insights clés

*(Section à compléter une fois l'analyse terminée — c'est la partie que les recruteurs lisent en premier. Formuler chaque insight comme dans un rapport métier : le chiffre, le "pourquoi ça compte".)*

- Insight 1 : ...
- Insight 2 : ...
- Insight 3 : ...

## 🗂️ Source des données

Comptes individuels des communes — données issues de la DGFiP / Observatoire des Finances et de la Gestion publique Locale (OFGL), disponibles sur [data.gouv.fr](https://www.data.gouv.fr/datasets/comptes-individuels-des-collectivites/).

Périmètre retenu : *(préciser — ex. une région, ou l'ensemble des communes sur les 3 dernières années disponibles)*

## 🛠️ Méthodologie

1. **Nettoyage** — typage des colonnes, gestion des valeurs manquantes, filtrage du périmètre d'étude
2. **Construction d'indicateurs** — épargne brute, taux d'endettement, ratio investissement/recettes réelles de fonctionnement
3. **Exploration** — agrégations par strate de population et par année
4. **Visualisation** — évolutions temporelles et comparaisons inter-strates
5. **Synthèse** — traduction des résultats en enseignements exploitables

## 📁 Structure du repo

```
├── data/raw/              # données brutes (ou script de téléchargement si volumineux)
├── notebooks/
│   ├── 01_exploration.ipynb      # premier contact avec les données
│   ├── 02_nettoyage.ipynb        # nettoyage et construction des indicateurs
│   └── 03_analyse_insights.ipynb # analyse et visualisations finales
├── src/utils.py            # fonctions réutilisables (chargement, nettoyage)
├── outputs/figures/        # graphiques exportés
└── requirements.txt
```

## 🚀 Installation

```bash
git clone https://github.com/<ton-user>/finances-locales-communes.git
cd finances-locales-communes
pip install -r requirements.txt
```

## 🧰 Stack technique

Python · pandas · matplotlib / seaborn · Jupyter

## 👤 Auteur

*(ton nom, lien LinkedIn, contexte pro en une ligne)*
