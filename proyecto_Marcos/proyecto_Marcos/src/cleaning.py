import pandas as pd # type: ignore
import numpy as np # type: ignore

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    del df["Competition"] # Elimina la columna "Competition"

    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Date"] = df["Date"].dt.date

    def get_winner(row): #Arregla la función para determinar el ganador del partido
        if row["Home Goals"] > row["Away Goals"]:
            return "Home Team"
        elif row["Home Goals"] < row["Away Goals"]:
            return "Away Team"
        else:
            return "Draw"

    df["Winner"] = df.apply(get_winner, axis=1)

    unificar = {
    "Man City": "Manchester City",
    "PSG": "Paris Saint-Germain",
}

    df["Home Team"] = df["Home Team"].replace(unificar)
    df["Away Team"] = df["Away Team"].replace(unificar)
    return df