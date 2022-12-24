import datetime
from collections import defaultdict
from urllib.request import urlopen
import xml.etree.ElementTree as etree
import csv
import requests
from datetime import datetime

# Define the structure of the data
dependency_header = ['id', 'situation', 'groupId', 'artifactId', 'version', 'release_date', 'is_updated']
dependencies_list = []


class Dependency:
    def __init__(self, id, situation, groupId, artifactId,version,release_date,is_updated):
        self.id = id
        self.situation = situation
        self.version = version
        self.groupId = groupId
        self.artifactId = artifactId
        self.release_date = release_date
        self.is_updated = is_updated


maven_url = 'https://search.maven.org/solrsearch/select'
namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}

#raw github link to pom file
repo_url = 'https://github.com/nwangtw/GrokkingStreamingSystems'
url = repo_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")+"/master/pom.xml"
filename = repo_url.split("/")[-1]+'.csv'
with urlopen(url) as response:
    tree = etree.parse(response)
    root = tree.getroot()

dependencies = root.find('{http://maven.apache.org/POM/4.0.0}dependencies')
#dependencies = root.find('{http://maven.apache.org/POM/4.0.0}dependencyManagement')
for dep in dependencies:
    print(dep.text)
    infoList = []
    for child in list(dep):
        print(child.tag, child.text)


deps = root.findall(".//xmlns:dependency", namespaces=namespaces)
currenId = 1

for d in deps:
    groupId = d.find("xmlns:groupId", namespaces=namespaces)
    artifactId = d.find("xmlns:artifactId", namespaces=namespaces)
    version = d.find("xmlns:version", namespaces=namespaces)
    try:
        if version is not None:  # The variable
            current_version = version.text
            if '$' in current_version:
                #current_version = version.text
                current_version = current_version.replace('${', '')
                current_version = current_version.replace('}', '')
                properties = tree.find('{http://maven.apache.org/POM/4.0.0}properties')
                if properties is None:
                    current_version = 'None'
                for prop in properties:
                    if prop is None:
                        current_version = 'None'
                    if current_version in prop.tag:
                        current_version = prop.text
                        print(prop.text)
                    #else:
                        #continue
            dependency = Dependency(currenId, 'current pom version', groupId.text, artifactId.text, current_version, "", "" )
            #check version for the current version:
            resp = requests.get(
                "https://search.maven.org/solrsearch/select?q=g:" + dependency.groupId + " AND a:" + dependency.artifactId + " AND v:" + current_version + "&core=gav&rows=20")
            if resp.status_code != 200:
                print("Error from server: " + str(resp.content))
            else:
                data = resp.json()
                if (data["response"]["numFound"] == 0):
                    print("no results found")
                    dependency = Dependency(currenId, 'current pom version', groupId.text, artifactId.text, current_version, 'None', 'None')
                else:
                    dependency = Dependency(currenId, 'current pom version', groupId.text, artifactId.text, current_version,
                                        datetime.fromtimestamp(data["response"]["docs"][0]["timestamp"] / 1000), "")

            dependencies_list.append(dependency)
            #writer.writerow(dependency)
            print("currenId: "+str(currenId)+" groupId: "+groupId.text+" artifactId: "+artifactId.text+" Version: "+current_version)
            params = dict(
                q="g:"+dependency.groupId+"+AND+a:"+dependency.artifactId,
                core="gav",
                rows=20,
                #wt='json'
            )
            #https://search.maven.org/solrsearch/select?q=g:software.amazon.awssdk AND a:bom&core=gav&rows=20
            resp = requests.get("https://search.maven.org/solrsearch/select?q=g:"+dependency.groupId+" AND a:"+dependency.artifactId+"&core=gav&rows=20")
            data = resp.json()  # Check the JSON Response Content documentation below
            if(data["response"]["numFound"] == 0):
                print("no results found")
                dependency = Dependency(currenId, 'latest pom version', dependency.groupId,
                                        dependency.artifactId, 'None', 'None', 'None')
            else:
                dependency = Dependency(currenId, 'latest pom version', data["response"]["docs"][0]["g"],
                                        data["response"]["docs"][0]["a"], data["response"]["docs"][0]["v"], datetime.fromtimestamp(data["response"]["docs"][0]["timestamp"]/ 1000), "")
            dependencies_list.append(dependency)
                #print(data["response"]["docs"][0])
        else:
            dependency = Dependency(currenId, 'current pom version', groupId.text, artifactId.text, "None", "", "")
            dependencies_list.append(dependency)
            #writer.writerow(dependency)
            print("currenId: "+str(currenId)+" groupId: "+groupId.text+" artifactId: "+artifactId.text+" Version: "+"None")
            respon = requests.get("https://search.maven.org/solrsearch/select?q=g:" + dependency.groupId + " AND a:" + dependency.artifactId + "&core=gav&rows=20")
            data = respon.json()  # Check the JSON Response Content documentation below
            if (data["response"]["numFound"] == 0):
                dependency = Dependency(currenId, 'latest pom version', dependency.groupId,
                                        dependency.artifactId, 'None', 'None', 'None')
            else:
                #print(data["response"]["docs"][0])
                dependency = Dependency(currenId, 'latest pom version', data["response"]["docs"][0]["g"],
                                        data["response"]["docs"][0]["a"], data["response"]["docs"][0]["v"],datetime.fromtimestamp(data["response"]["docs"][0]["timestamp"] / 1000), "")
            dependencies_list.append(dependency)
    except NameError:
        print("This variable is not defined")
    currenId += 1

with open('CheckVersions__'+filename, 'w', newline='') as f:

    # fieldnames lists the headers for the csv.
    w = csv.DictWriter(f, fieldnames=vars(dependencies_list[0]))
    w.writeheader()
    #w.writerows(dependencies_list)
    for dep in dependencies_list:
        # Build a dictionary of the member names and values...
        w.writerow({'id': dep.id, 'situation': dep.situation, 'groupId': dep.groupId, 'artifactId': dep.artifactId, 'version': dep.version, 'release_date': dep.release_date, 'is_updated': ""})

