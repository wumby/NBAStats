
import pandas as pd
import numpy as np
import csv
  

player_list = pd.read_csv('playerlist.csv')
player_list.pop('unnamed')

column_names = ["playersList"]
df = pd.read_csv("playerlist.csv", names = column_names)
plist = df.playersList.to_list()
print(plist)