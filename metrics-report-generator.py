

import pandas as pd

# create metrics DataFrame constructor
metrics_df = pd.DataFrame(columns=['CommitHash','CommitDate', 'CommitSituation','CountClassCoupled','PercentLackOfCohesion','PercentLackOfCohesionModified','Cyclomatic','CountLineCode','CountLineComment'])
project_commits = "metrics_dataframes/metrics_commits_aparapi-examples.csv"
project_df=pd.read_csv(project_commits)
commmit_nbr = 0
for commit in project_df['CommitHash']:
    commmit_nbr = commmit_nbr + 1
    CommitDate = project_df.loc[project_df['CommitHash'] == commit, 'CommitDate'].iloc[0]

    read_csv = "/Users/mac/Desktop/metrics_data_mining/results/updated/aparapi/aparapi-examples_metrics_"+commit+".csv"
    df=pd.read_csv(read_csv)
    df = df[df['Kind'].str.contains('Class', na=False)]
    df.drop(df[df['Kind'] == 'Anonymous Class'].index, inplace=True)
    df.drop(df[df['Kind'] == 'Public Abstract Generic Class'].index, inplace=True)
    df = df.drop(['Kind', 'Name'], axis=1)
    CountClassCoupled_mean = df['CountClassCoupled'].mean()
    PercentLackOfCohesion_mean = df['PercentLackOfCohesion'].mean()
    PercentLackOfCohesionModified_mean = df['PercentLackOfCohesionModified'].mean()
    SumCyclomatic_mean = df['SumCyclomatic'].mean()
    CountLineCode_sum = df['CountLineCode'].sum()
    CountLineComment_sum = df['CountLineComment'].sum()
    if (commmit_nbr % 2) == 0:
        commitSituation = "Previous commit"
    else:
        commitSituation = "Current commit"

    #print(CountLineComment_sum)
    #create new Row
    new_row = {'CommitHash': commit,'CommitDate': CommitDate , 'CommitSituation': commitSituation, 'CountClassCoupled':CountClassCoupled_mean,
               'PercentLackOfCohesion':PercentLackOfCohesion_mean, 'PercentLackOfCohesionModified':PercentLackOfCohesionModified_mean,
                'Cyclomatic':SumCyclomatic_mean, 'CountLineCode':CountLineCode_sum, 'CountLineComment':CountLineComment_sum  }
    # define row to add
    row_to_append = pd.DataFrame([new_row])
    # add row to empty DataFrame
    metrics_df = pd.concat([metrics_df, row_to_append], ignore_index=True)

print(metrics_df.to_string())

#get csv file name
save_url = project_commits.split("/metrics_commits_")[1]
#print to csv
metrics_df.to_csv('metrics_report/'+save_url, encoding='utf-8', index=False)
