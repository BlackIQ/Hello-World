"""
This script create a table from people who contribute and added Hello World language
for this repository. Which first column is name and second one is how may language
contributer added to this repo and also if contributer added more than 5 language
contrubuter will receive a badge after his name
"""

import os
import json
import re

output = """
## List of people who contribute on this repository

| Name | Added languegse |
|------|-----------------|
"""

def main(project_dir = None):
    if project_dir == None:
        project_dir = os.path.dirname(os.path.abspath(__file__))

    # loading list of languages
    global output
    items = os.listdir(project_dir)
    items.sort()

    contributers = []
    
    for item in items:
        if item[0] not in ['.','_'] and os.path.isdir(project_dir + '/' + item):
            try:
                with open(project_dir + '/' + item + '/info.json') as json_file:
                    contributer = json.load(json_file)
                    
                    contributers.append(contributer['creator']['title'])
                    badge = "🏅" if contributers.count(contributer['creator']['title']) > 5 else ""
                    output += "| [" + contributer['creator']['title'] + badge + "](" + contributer['creator']['link'] + ')|'  + str(contributers.count(contributer['creator']['title'])) +"|"
                    output += '\n'
            except:
                print("file not founded or info.js has't valid data")
    ct = open(project_dir + "/CONTRIBUTERS.md", 'w')
    ct.write(output)
    ct.close()
if __name__ == '__main__':
    main()