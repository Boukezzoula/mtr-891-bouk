# mtr-891-bouk

# Steps:

1- i have created "checkVersions_to_confirm_project_updated_outdated.py" to check all github project and retrieve the version of dependencies in the pom file and the latest available version of the dependency online.


2- i have created this script : "https://github.com/Boukezzoula/PomXmlParser" to parse all github project and extract all the changes in the dependencies

3- i have created the script "countChanges.py" to clean the data collected from steps 1 and 2 , to generate csv files which contains all the dependencies changes in our projects .

4- i have used this script "data_cleaning.py" to clean the data and collect information about number of added lines,deleted lines,modified files, and total number of changes .

5- i have used this script "previous_current_commits.py" to prepare the commits we will use in sci-tools understand , i have generated csv file for each project and saved it on "metrics_dataframes" folder , which contains the commit with modified dependency hash and the previous commit hash

6- to generate the metrics i've developed this script  : https://github.com/Boukezzoula/Scitools-Understand-software-metrics-collector

 6.A- folder : metrics data mining results ( current modifierd commit and previous commit ) : contains the metrics collected for all the commits with dependency modification and the previous commit .
 
 6.B- folder : metrics data mining results for latest modified commit and the latest exisiting commit in the project : contains the metrics collected to compare the commit with latest modified dependency and the latest commit available for the project , the results of the comparaison is available at comparaison folder.
 
7 - i have used "metrics-report-generator.py" to generate the mean of the metrics for all commits for each project and saved it on metrics report folder.

8- in the end i have created jupyter notebook "datafinding.ipynb" to generate p-values and compare the metrics.
