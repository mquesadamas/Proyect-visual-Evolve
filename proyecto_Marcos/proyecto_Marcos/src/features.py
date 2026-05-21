import pandas as pd # type: ignore
import numpy as np # type: ignore

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # Partidos jugados
    home_matches = df["Home Team"].value_counts()
    away_matches = df["Away Team"].value_counts()

    # Puntos usando Winner
    df["Home_Points"] = df["Winner"].apply(lambda x: 3 if x == "Home Team" else 1 if x == "Draw" else 0)
    df["Away_Points"] = df["Winner"].apply(lambda x: 3 if x == "Away Team" else 1 if x == "Draw" else 0)

    # Tabla final
    teams = sorted(set(df["Home Team"]).union(set(df["Away Team"])))
    team_stats = pd.DataFrame(index=teams)
    team_stats.index.name = "Team"

    team_stats["Matches_Played"] = (
        home_matches.reindex(team_stats.index, fill_value=0) +
        away_matches.reindex(team_stats.index, fill_value=0)
    )

    team_stats["Total_Points"] = (
        df.groupby("Home Team")["Home_Points"].sum().reindex(team_stats.index, fill_value=0) +
        df.groupby("Away Team")["Away_Points"].sum().reindex(team_stats.index, fill_value=0)
    )

    team_stats["Total_Shots"] = (
        df.groupby("Home Team")["Shots (Home)"].sum().reindex(team_stats.index, fill_value=0) +
        df.groupby("Away Team")["Shots (Away)"].sum().reindex(team_stats.index, fill_value=0)
    )

    team_stats["Total_Goals"] = (
        df.groupby("Home Team")["Home Goals"].sum().reindex(team_stats.index, fill_value=0) +
        df.groupby("Away Team")["Away Goals"].sum().reindex(team_stats.index, fill_value=0)
    )

    team_stats["Average_Points"] = team_stats["Total_Points"] / team_stats["Matches_Played"]

    team_stats = team_stats.sort_values(["Average_Points","Total_Points", "Matches_Played", "Total_Goals", "Total_Shots"], ascending=False).reset_index()

    return team_stats, df