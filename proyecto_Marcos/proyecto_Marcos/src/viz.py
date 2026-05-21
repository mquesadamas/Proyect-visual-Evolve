import pandas as pd # type: ignore
import numpy as np # type: ignore   
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from src.features import build_features

def plot_graph(df: pd.DataFrame) -> None:

    corr = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(14, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlación')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(x="Winner", data=df, order=df["Winner"].value_counts().index)
    plt.title("Victorias", fontsize=14)
    plt.show()

    team_stats, df = build_features(df)
    plt.figure(figsize=(10,6))
    sns.barplot(x="Team", y="Average_Points", data=team_stats, palette='Set1')
    plt.xticks(rotation=45)
    plt.show()