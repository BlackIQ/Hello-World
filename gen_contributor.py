#!/usr/bin/env python3

"""
This script create a table from people who contribute and added Hello World language
for this repository. Which the first column is the name and the second one is how many language
contributor added to this repo and also if a contributor added more than 5 language
contributor will receive a badge after his name
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

    contributors = {}
    
    for item in items:
        if item[0] not in ['.','_'] and os.path.isdir(project_dir + '/' + item):
            try:
                with open(project_dir + '/' + item + '/info.json') as json_file:
                    contributor = json.load(json_file)

                    try:
                        contributors[contributor['creator']['link']]
                    except KeyError:
                        contributors[contributor['creator']['link']] = contributor['creator']
                        contributors[contributor['creator']['link']]['count'] = 0
                    contributors[contributor['creator']['link']]['count'] += 1
            except:
                print("file not founded or info.js has't valid data")

    # generate table of loaded contributors
    for k in contributors:
        contributor = contributors[k]
        badge = "🏅" if contributor['count'] > 5 else ""
        output += "| [" + contributor['title'] + badge + "](" + contributor['link'] + ')|'  + str(contributor['count']) +"|"
        output += '\n'

    ct = open(project_dir + "/CONTRIBUTORS.md", 'w')
    ct.write(output)
    ct.close()

    print('Contributors table generated!')
if __name__ == '__main__':
    main()
