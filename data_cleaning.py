# here i calculated the changes in each repo : total of lines changed - added - removed - number of commits with changes .....

import pandas as pd
from collections import namedtuple

""""
class Dependency:
    def __init__(self, id, situation, groupId, artifactId,version):
        self.id = id
        self.situation = situation
        self.version = version
        self.groupId = groupId
        self.artifactId = artifactId
"""

#read the csv file
df = pd.read_csv('final_changes_for_dependencies_in_pom_file/final_changes_PetHospital.csv')

#class represent the changed lines

class changedLine:
    def __init__(self, CommitHash, CommitName, CommitDate, ChangeType, groupId, artifactId, version, NbrAddedLines,NbrDeletedLines,NbrModifiedFiles):
        self.CommitHash = CommitHash
        self.CommitDate = CommitDate
        self.CommitName = CommitName
        self.ChangeType = ChangeType
        self.groupId = groupId
        self.artifactId = artifactId
        self.version = version
        self.NbrAddedLines = NbrAddedLines
        self.NbrDeletedLines = NbrDeletedLines
        self.NbrModifiedFiles = NbrModifiedFiles

#convert csv rows into object
#listOfDependencies = [(changedLine(row.CommitHash, row.CommitDate, row.ChangeType, row.groupId, row.artifactId, row.version, row.NbrAddedLines, row.NbrDeletedLines, row.NbrModifiedFiles)) for index, row in df.iterrows()]
#print(listOfDependencies[0].version)

#remove rows of the latest version cause we don't need them here
df.drop(df[df['ChangeType'] == 'ADD'].index, inplace = True)
#drop duplicates by hash
df2 = df.drop_duplicates(subset='CommitHash', keep="first")
#drop unecessary columns
#df2 = df2.drop(['ChangeType','groupId','artifactId','version','NbrAddedLines','NbrDeletedLines','NbrModifiedFiles'], axis=1)

#print(df2.to_string())

count_row = df2.shape[0]  # Gives number of rows
added_sum = sum(df2['NbrAddedLines'])
deleted_sum = sum(df2['NbrDeletedLines'])
modified_sum = sum(df2['NbrModifiedFiles'])

print(df2.to_string())

print("total number of rows : "+ str(count_row))
print("total added lines : "+str(added_sum))
print("total deleted lines : "+str(deleted_sum))
print("total modified files : "+str(modified_sum))

