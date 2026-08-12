# Analyse des finances locales des communes françaises

Projet d'analyse de données appliqué aux finances publiques locales, réalisé dans le cadre de mon portfolio de Business Analyst / Data Analyst junior.

## 🎯 Contexte et objectif

Fort de 3 ans d'alternance en DSI au sein d'une collectivité territoriale, j'ai voulu construire un projet qui combine compétences techniques (Python, pandas, data visualisation) et compréhension métier des enjeux budgétaires locaux.

**Questions traitées :**
1. Comment évolue l'épargne brute (autofinancement) des communes selon leur strate de population ?
2. Quelles strates de communes voient leur endettement progresser plus vite que leurs recettes ?
3. Quel est le poids de l'investissement dans les budgets communaux, et comment évolue-t-il dans le temps ?


## 📊 Insights clés

- **Épargne brute** : plus élevée par habitant dans les très petites communes, mais 
  cet écart reflète surtout un effet mécanique de dénominateur (population faible) 
  plutôt qu'une meilleure santé financière.
- **Endettement** : en baisse sur la quasi-totalité des strates entre 2018 et 2025 ; 
  la seule exception notable (villes de 50-80k hab.) s'explique par la trajectoire 
  d'une commune isolée (Montauban), pas par une tendance de groupe.
- **Investissement** : suit nettement le cycle électoral municipal (pic en 2019, 
  creux en 2020-2021, remontée depuis), avec un niveau structurellement plus bas 
  dans les métropoles.

## 🗂️ Source des données

Comptes individuels des communes — données issues de la DGFiP / Observatoire des Finances et de la Gestion publique Locale (OFGL), disponibles sur [data.gouv.fr](https://www.data.gouv.fr/datasets/comptes-individuels-des-collectivites/).

Périmètre retenu : Région Occitanie sur la période 2018-2025

## 🛠️ Méthodologie

1. **Nettoyage** — typage des colonnes, gestion des valeurs manquantes, filtrage du périmètre d'étude
2. **Construction d'indicateurs** — épargne brute, taux d'endettement, ratio investissement/recettes réelles de fonctionnement
3. **Exploration** — agrégations par strate de population et par année
4. **Visualisation** — évolutions temporelles et comparaisons inter-strates
5. **Synthèse** — traduction des résultats en enseignements exploitables

## 📁 Structure du repo

```
├── data/raw/              # données brutes
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

Maxime Chaussende 
