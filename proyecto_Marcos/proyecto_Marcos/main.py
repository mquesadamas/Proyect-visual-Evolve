from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean_data 
from src.features import build_features
from src.utils import assert_columns, dataset_info, value_counts_summary
from src.viz import plot_graph

def main():
    df = load_csv(RAW_PATH)
    df = clean_data(df)
    team_stats, df = build_features(df)
    dataset_info(df)
    value_counts_summary(df, "Winner")
    value_counts_summary(team_stats, "Team")
    value_counts_summary(team_stats, "Total_Points")
    value_counts_summary(team_stats, "Total_Goals")

    plot_graph(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")

if __name__ == "__main__":
    main()