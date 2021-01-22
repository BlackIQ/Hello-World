#!/usr/bin/env python3

""" This script generates README.md automaticaly """

import os
import json

project_dir = os.path.dirname(os.path.abspath(__file__))
""" The project directory path """

items = os.listdir(project_dir)

langs = []
""" Found languages """

for item in items:
    if os.path.isdir(item) and item[0] != '.':
        langs.append(item)
langs.sort()


letters = {}

# split langs by first letter
for lang in langs:
    try:
        letters[lang[0]]
    except KeyError:
        letters[lang[0]] = []
    letters[lang[0]].append(lang)

count = len(langs)

readme_content = f'''
<p>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/BlackIQ/Hello-World">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/BlackIQ/Hello-World">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/BlackIQ/Hello-World">
<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/BlackIQ/Hello-World">
<img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/BlackIQ/Hello-World">
</p>

# Hello World And some Examples in different Programming Languages

This repository contains a big list of programming languages and some examples for them. Also there are some descriptions about them and some tutorials. If you want to learn a programming language, the decriptions, tutorials and examples for that language in this repo might be helpful.

## Contributing
If you want to contribute to this project, read [Contributing Guide](CONTRIBUTING.md).

Total Languages in the Repository: {count}.

'''

for letter in letters:
    readme_content += '\n### ' + letter.upper() + '\n\n---\n\n'
    for item in letters[letter]:

        if (' ' in item) == True:
            item = item.replace(' ', "-")
        
        creator_title = None
        creator_link = None
        if os.path.isfile(project_dir + '/' + item + '/info.json'):
            try:
                f = open(project_dir + '/' + item + '/info.json', 'r')
                content = f.read()
                f.close()
                content = json.loads(content)
                try:
                    creator_title = content['creator']['title']
                    try:
                        creator_link = content['creator']['link']
                    except KeyError:
                        pass
                except KeyError:
                    pass
            except:
                print(f'Error: invalid json data in {item}/info.json. ignored...')

        if creator_title != None:
            if creator_link != None:
                readme_content += '- [' + item + '](/' + item + ') - Added By [' + creator_title + '](' + creator_link + ')\n'
            else:
                readme_content += '- [' + item + '](/' + item + ') - Added By ' + creator_title + '\n'
        else:
            readme_content += '- [' + item + '](/' + item + ')\n'
    readme_content += '\n'

# write content on readme.md
# f = open(project_dir + '/README.md', 'w')
# f.write(readme_content.strip() + '\n')
# f.close()

print('Done!')
