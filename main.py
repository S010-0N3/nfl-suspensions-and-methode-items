import csv

fruits ={"banane":9,"riz":13,"pomme":7,"kiwi":5,"orange":90,}

#####utilisation de la fonction items#####
for fruit,number in fruits.items():
  #print(fruit)
  #print(number)
  
########## Nombres de suspendu par annee ###############

f=open("nfl_suspension.csv")
nfl_s = list(csv.reader(f))
nfl_s = nfl_s[1:]

#year = 0

#years_column = nfl_s[5]
years = {}


for suspension in nfl_s:
  row_year = suspension[5]
  if row_year in years:
    years[row_year] += 1
  else:
    years[row_year] = 1

print(years)

###########################version 1#########################
unique_teams = []
unique_games = []

for i in nfl_s:
  row_team = i[1]
  row_game = i[2]
  if row_team is not unique_teams:
    unique_teams.append(row_team)
  if row_game is not unique_games:
    unique_games.append(row_game)

#print(set(unique_teams))
#print(set(unique_games))

###########################version 1#########################


print("###################version 2##########################")
##########################version 2###################
teams= [row[1]for row in nfl_s]
unique_teams = set(teams)
print(set(unique_teams))

games= [row[2]for row in nfl_s]
unique_games = set(games)
print(set(unique_games))