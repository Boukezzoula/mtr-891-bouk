# MTR891 - the impact of Outdated libraries impact on softwares
## Boukezzoula

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

this readme will explain all the steps i made in my research.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## folders

- #### check_versions_for_project_updated_or_outdate :
contains the results of comparaison between the dependencies versions in the pom file and the latest available version online to decide if the project is updated or outdated.
- #### dependencies_changes_in_pom_file :
contains all detected dependencies changes in all the commits .
- #### metrics_dataframes :
contains the commit with modified dependency hash and the previous commit hash
- #### metrics data mining results ( current modifierd commit and previous commit ) : 
contains the metrics collected for all the commits with dependency modification and the previous commit .
- #### metrics report : 
contains the resuls of the mean of the metrics for all commits for each project
- #### metrics data mining results for latest modified commit and the latest exisiting commit in the project
contains the metrics collected to compare the commit with latest modified dependency and the latest commit available for the project.
- #### comparaison :
the results of the comparaison between the latest modified dependency and the latest commit available for the project.



## Scripts

this is the list of all scripts i have created :

- [checkVersions_to_confirm_project_updated_outdated.py](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/checkVersions_to_confirm_project_updated_outdated.py) - to check all github project and retrieve the version of dependencies in the pom file and the latest available version of the dependency online.
- [POMXMLPARSER](https://github.com/Boukezzoula/PomXmlParser) - to parse all github project and extract all the changes in the dependencies.
- [countChanges.py](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/countChanges.py) - to clean the data collected from script 1 and 2 , to generate csv files which contains all the dependencies changes in our projects.
- [data_cleaning.py](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/data_cleaning.py) -  clean the data and collect information about number of added lines,deleted lines,modified files, and total number of changed dependencies.
- [previous_current_commits.py](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/previous_current_commits.py) - to prepare the commits we will use in sci-tools understand , i have generated csv file for each project and saved it on "metrics_dataframes" folder
- [Scitools-Understand-software-metrics-collector](https://github.com/Boukezzoula/Scitools-Understand-software-metrics-collector) - shell script i have developed to use understand from the terminal on mac to generate the metrics.
- [metrics-report-generator.py](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/metrics-report-generator.py) - to generate the mean of the metrics for all commits for each project and saved it on metrics report folder
- [datafinding.ipynb](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/datafinding.ipynb) - jupyter notebok to generate boxplots,p-values and compare the metrics


## Usage 

to generate same results you can follow the order of the scripts .
and you access the dataset of projects i have studies from here [dataset](https://github.com/Boukezzoula/mtr-891-bouk/blob/main/dataset.xlsx)


## Software you need 

| pycharme ide | [https://www.jetbrains.com/pycharm/download/] |
| sci tools understand | [https://licensing.scitools.com/download] |
| jupyter notebook | [https://jupyter.org/install] |
