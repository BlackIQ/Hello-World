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

| Name | Added languages |
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
                print(item + ": file not found or info.js has not valid syntax")

    # sort the loaded list
    counts = [contributors[c]['count'] for c in contributors]
    counts.sort()
    new_list = []
    added_items = []
    while len(counts) > 0:
        for k in contributors:
            if contributors[k]['count'] >= counts[-1]:
                if k not in added_items:
                    new_list.append(contributors[k])
                    added_items.append(k)
        counts.remove(counts[-1])
    contributors = new_list

    # generate table of loaded contributors
    for contributor in contributors:
        badge = "🏅" if contributor['count'] > 5 else ""
        output += "| [" + contributor['title'] + badge + "](" + contributor['link'] + ')|'  + str(contributor['count']) +"|"
        output += '\n'

    ct = open(project_dir + "/CONTRIBUTORS_LIST.md", 'w')
    ct.write(output)
    ct.close()

    print('Contributors table generated!')
if __name__ == '__main__':
    main()