# mtr-891-bouk

# Steps:

1- i have created "checkVersions_to_confirm_project_updated_outdated.py" to check all github project and retrieve the version of dependencies in the pom file and the latest available version of the dependency online.


2- using pom-parser to parse all github project and extract all the changes in the dependencies i have created this script : https://github.com/Boukezzoula/PomXmlParser

5- to generate the metrics i've developed this script  : https://github.com/Boukezzoula/Scitools-Understand-software-metrics-collector

 5.A- folder : metrics data mining results ( current modifierd commit and previous commit ) : contains the metrics collected for all the commits with dependency modification and the previous commit .
 
 5.B- folder : metrics data mining results for latest modified commit and the latest exisiting commit in the project : contains the metrics collected to compare the commit with latest modified dependency and the latest commit available for the project , the results of the comparaison is available at comparaison folder.
 
