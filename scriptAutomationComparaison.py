# this python script is to compare the latest commit of modified dependencies with the latest available commit of the project 

import pandas as pd

# create metrics DataFrame constructor
metrics_df = pd.DataFrame(columns=['CommitHash', 'CommitSituation','CountClassCoupled','PercentLackOfCohesion','PercentLackOfCohesionModified','Cyclomatic','CountLineCode','CountLineComment'])
project_title = "universal-registrar"
file_title = "universal-registrar_metrics_"
current_commit = "49a9ee4a5a0e48c4fe66082d084e97d3afdd92f7"
latest_commit = "702e49dc0818b8d6e8305b4621ba71b512a8011f"
current_commit_path = "/Users/mac/Desktop/metrics_generator/results/updated/"
latest_commit_path = "/Users/mac/Desktop/metrics_generator/results/updated/"
read_current_csv = current_commit_path+project_title+"/"+file_title+current_commit+".csv"
read_latest_csv = current_commit_path+project_title+"/"+file_title+latest_commit+".csv"
#csv files
df_current=pd.read_csv(read_current_csv)
df_latest=pd.read_csv(read_latest_csv)
#curent
df_current = df_current[df_current['Kind'].str.contains('Class', na=False)]
df_current.drop(df_current[df_current['Kind'] == 'Anonymous Class'].index, inplace=True)
df_current.drop(df_current[df_current['Kind'] == 'Public Abstract Generic Class'].index, inplace=True)
df_current = df_current.drop(['Kind', 'Name'], axis=1)
CountClassCoupled_mean = df_current['CountClassCoupled'].mean()
PercentLackOfCohesion_mean = df_current['PercentLackOfCohesion'].mean()
PercentLackOfCohesionModified_mean = df_current['PercentLackOfCohesionModified'].mean()
SumCyclomatic_mean = df_current['SumCyclomatic'].mean()
CountLineCode_sum = df_current['CountLineCode'].sum()
CountLineComment_sum = df_current['CountLineComment'].sum()

# create new Row
new_row = {'CommitHash': current_commit, 'CommitSituation': 'latest commit with update',
           'CountClassCoupled': CountClassCoupled_mean,
           'PercentLackOfCohesion': PercentLackOfCohesion_mean,
           'PercentLackOfCohesionModified': PercentLackOfCohesionModified_mean,
           'Cyclomatic': SumCyclomatic_mean, 'CountLineCode': CountLineCode_sum,
           'CountLineComment': CountLineComment_sum}
# define row to add
row_to_append = pd.DataFrame([new_row])
# add row to empty DataFrame
metrics_df = pd.concat([metrics_df, row_to_append], ignore_index=True)

#latest
df_latest = df_latest[df_latest['Kind'].str.contains('Class', na=False)]
df_latest.drop(df_latest[df_latest['Kind'] == 'Anonymous Class'].index, inplace=True)
df_latest.drop(df_latest[df_latest['Kind'] == 'Public Abstract Generic Class'].index, inplace=True)
df_latest = df_latest.drop(['Kind', 'Name'], axis=1)
CountClassCoupled_mean = df_latest['CountClassCoupled'].mean()
PercentLackOfCohesion_mean = df_latest['PercentLackOfCohesion'].mean()
PercentLackOfCohesionModified_mean = df_latest['PercentLackOfCohesionModified'].mean()
SumCyclomatic_mean = df_latest['SumCyclomatic'].mean()
CountLineCode_sum = df_latest['CountLineCode'].sum()
CountLineComment_sum = df_latest['CountLineComment'].sum()

# create new Row
new_row = {'CommitHash': latest_commit, 'CommitSituation': 'last project commit ',
           'CountClassCoupled': CountClassCoupled_mean,
           'PercentLackOfCohesion': PercentLackOfCohesion_mean,
           'PercentLackOfCohesionModified': PercentLackOfCohesionModified_mean,
           'Cyclomatic': SumCyclomatic_mean, 'CountLineCode': CountLineCode_sum,
           'CountLineComment': CountLineComment_sum}
# define row to add
row_to_append = pd.DataFrame([new_row])
# add row to empty DataFrame
metrics_df = pd.concat([metrics_df, row_to_append], ignore_index=True)


#print to csv
metrics_df.to_csv('comparaison/'+project_title+".csv", encoding='utf-8', index=False)
