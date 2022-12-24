

import pandas as pd
from collections import namedtuple

class Dependency:
    def __init__(self, id, situation, groupId, artifactId,version):
        self.id = id
        self.situation = situation
        self.version = version
        self.groupId = groupId
        self.artifactId = artifactId

#read the csv file
df = pd.read_csv('Optimised_check_versions/CheckVersions__PetHospital.csv')
#csv file location
csv_file = 'data_parsing/parser_PetHospital.csv'

#remove rows of the latest version cause we don't need them here
df.drop(df[df['situation'] == 'latest pom version'].index, inplace = True)

#convert csv rows into object
listOfDependencies = [(Dependency(row.id, row.situation, row.groupId, row.artifactId, row.version)) for index, row in df.iterrows()]
print(listOfDependencies[0].version)


#read the csv file
commits_df = pd.read_csv(csv_file)
#get csv file name
save_url = csv_file.split("parser_")[1]
#delete commit comment column
commits_df.drop('CommitName', axis=1, inplace=True)

final_df = pd.DataFrame()
#loop the list of dependencies
for dependency_item in listOfDependencies:
    # selecting rows based on condition
    rslt_df = commits_df[(commits_df['artifactId'] == dependency_item.artifactId) & (commits_df['version'] != dependency_item.version)]
    #print(rslt_df)
    #drop duplicates
    df2 = rslt_df.drop_duplicates(subset='version', keep="first")
    final_df = pd.concat([final_df, df2])
    #final_df.append(df2)

final_df.to_csv('final_changes_'+save_url, encoding='utf-8', index=False)
print(final_df.to_string())
#rslt_df = commits_df[commits_df['artifactId'] == 'jackson-databind' & commits_df['version'] != '2.9.10']
#print(rslt_df.to_string())
#print(rslt_df)
#print(" drop duplicaats")
# keep first duplicate row
#df2 = rslt_df.drop_duplicates(subset='version', keep="first")
#df2 = rslt_df.drop_duplicates()
#print(df2.to_string())
#for rows in commits_df.iterrows():

#print(df.to_string())
#Dependency = namedtuple('Dependency', df.dtypes.index.tolist())
#dependency = Dependency(*df.iloc[1,:])
#print (dependency)
