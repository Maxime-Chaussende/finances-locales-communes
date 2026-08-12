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


def pivot_agregats(df: pd.DataFrame,
                    budget_type: str = "Budget principal") -> pd.DataFrame:
    """
    Transforme le dataset OFGL (format long : une ligne par commune/année/agrégat)
    en format large (une ligne par commune/année, une colonne par agrégat).

    Filtre par défaut sur le budget principal pour éviter de mélanger
    les budgets annexes dans les agrégats globaux.
    """
    df_filt = df[df["Type de budget"] == budget_type].copy()

    pivot = df_filt.pivot_table(
        index=["Exercice", "Code Insee 2025 Commune", "Nom 2025 Commune", "Nom 2025 Département",
               "Strate population 2025", "Population totale"],
        columns="Agrégat",
        values="Montant",
        aggfunc="sum",
    ).reset_index()

    pivot.columns.name = None
    return pivot


def compute_taux_endettement(df: pd.DataFrame,
                              dette_col: str = "Encours de dette",
                              recettes_fonct_col: str = "Recettes de fonctionnement") -> pd.DataFrame:
    """
    Calcule un taux d'endettement simplifié = encours de dette / recettes de
    fonctionnement. À appliquer après pivot_agregats().
    """
    df = df.copy()
    df["taux_endettement"] = df[dette_col] / df[recettes_fonct_col]
    return df


# Note : le dataset OFGL fournit déjà une colonne "Strate population 2025"
# calculée par leurs soins — pas besoin de la recalculer manuellement.