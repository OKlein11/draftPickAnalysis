import csv
import pandas as pd


draft = pd.read_csv("data/draft_picks.csv")




player_stats = pd.read_csv("data/player_stats.csv")




players = pd.read_csv("data/players.csv")


player_career_stats = player_stats.groupby(["player_display_name"])
player_career_stats = player_career_stats.agg("sum", numeric_only=True)
player_career_stats = player_career_stats.reset_index()
print(player_career_stats.loc[0])

merged = draft.merge(player_career_stats,how="left",left_on="pfr_player_name",right_on="player_display_name")

merged = merged[merged["season_x"]>=2000]

qbs = merged[merged["position"] == "QB"]
rbs = merged[merged["position"] == "RB"]
wrs = merged[merged["position"] == "WR"]

qbs.to_csv("data/qbs.csv")
rbs.to_csv("data/rbs.csv")
wrs.to_csv("data/wrs.csv")

