import numpy as np
from pydriller import Repository
import pandas as pd
from collections import namedtuple

read_csv = "final_changes_for_dependencies_in_pom_file/final_changes_job-config-history-plugin.csv"
# analyzed repository
url = "https://github.com/jenkinsci/job-config-history-plugin"
#read the csv file
df = pd.read_csv(read_csv)


#remove rows of the latest version cause we don't need them here
df.drop(df[df['ChangeType'] == 'ADD'].index, inplace = True)
#drop duplicates by hash
df2 = df.drop_duplicates(subset='CommitHash', keep="first")
#drop unecessary columns
df2 = df2.drop(['ChangeType','groupId','artifactId','version','NbrAddedLines','NbrDeletedLines','NbrModifiedFiles'], axis=1)

print(df2.to_string())

# create repo DataFrame constructor
commits_df = pd.DataFrame(columns=['CommitHash', 'CommitDate'])

for commit in Repository(url).traverse_commits():
    new_row = {'CommitHash': commit.hash, 'CommitDate': commit.committer_date}
    # define row to add
    row_to_append = pd.DataFrame([{'CommitHash': commit.hash, 'CommitDate': commit.committer_date}])
    # add row to empty DataFrame
    commits_df = pd.concat([commits_df, row_to_append],ignore_index=True)

final_df = pd.DataFrame(columns=['CommitHash', 'CommitDate'])

for commit in df2['CommitHash']:
    if commit in commits_df['CommitHash'].values:
        print("true")
        row_to_append = commits_df.iloc[np.flatnonzero(commits_df.CommitHash == commit) - 1]
        final_df = pd.concat([final_df, commits_df.loc[commits_df['CommitHash'] == commit]])
        final_df = pd.concat([final_df, row_to_append])

#get csv file name
save_url = read_csv.split("/final_changes_")[1]
#print to csv
final_df.to_csv('metrics_commits_'+save_url, encoding='utf-8', index=False)

print(commits_df.to_string())
print("final")
print(final_df.to_string())