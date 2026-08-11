"""
Fonctions utilitaires pour le chargement et le nettoyage des données
de finances locales des communes.
"""

import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Charge le fichier brut des comptes individuels des communes.

    Parameters
    ----------
    path : str
        Chemin vers le fichier CSV téléchargé depuis data.gouv.fr / OFGL.

    Returns
    -------
    pd.DataFrame
    """
    df = pd.read_csv(path, sep=";", encoding="utf-8", low_memory=False)
    return df


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalise les noms de colonnes : minuscules, sans espaces ni accents superflus.
    """
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("é", "e")
        .str.replace("è", "e")
    )
    return df


def compute_epargne_brute(df: pd.DataFrame,
                           recettes_fonct_col: str,
                           depenses_fonct_col: str) -> pd.DataFrame:
    """
    Calcule l'épargne brute (autofinancement) = recettes réelles de fonctionnement
    - dépenses réelles de fonctionnement.

    À adapter selon les noms exacts de colonnes du dataset une fois exploré.
    """
    df = df.copy()
    df["epargne_brute"] = df[recettes_fonct_col] - df[depenses_fonct_col]
    return df


def compute_taux_endettement(df: pd.DataFrame,
                              dette_col: str,
                              recettes_fonct_col: str) -> pd.DataFrame:
    """
    Calcule un taux d'endettement simplifié = encours de dette / recettes réelles
    de fonctionnement.
    """
    df = df.copy()
    df["taux_endettement"] = df[dette_col] / df[recettes_fonct_col]
    return df


def assign_strate_population(df: pd.DataFrame, pop_col: str) -> pd.DataFrame:
    """
    Attribue une strate de population standard (utilisée par la DGCL/OFGL)
    à chaque commune, à partir de sa population.
    """
    df = df.copy()
    bins = [0, 500, 2000, 3500, 5000, 10000, 20000, 50000, 100000, float("inf")]
    labels = [
        "<500", "500-2000", "2000-3500", "3500-5000", "5000-10000",
        "10000-20000", "20000-50000", "50000-100000", ">100000"
    ]
    df["strate_population"] = pd.cut(df[pop_col], bins=bins, labels=labels)
    return df
