import pandas as pd 

gamesdata = pd.read_csv("games.csv")

# Adds the total points scored in a game to the end of the dataframe
point_total= gamesdata.PTS_home + gamesdata.PTS_away
gamesdata["point_total"] = point_total[0:23194]

# Removing entries before 2018 season 
gamesdata = gamesdata.loc[gamesdata.SEASON >= 2018]
gamesdata.sort_values(by=["GAME_DATE_EST"])
gamesdata = gamesdata.reset_index(drop = True)

# Checked missing values, there are none
#print (gamesdata.isnull().sum()) 




