#!/usr/bin/env python3

""" This script generates README.md automaticaly """

import os

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

readme_content = '''
<p>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/BlackIQ/Hello-World">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/BlackIQ/Hello-World">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/BlackIQ/Hello-World">
<img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/BlackIQ/Hello-World">
<img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/BlackIQ/Hello-World">
</p>

# Hello World in different languages

> You can fork this repository and add your Hello World

'''

for letter in letters:
    readme_content += '\n# ' + letter.upper() + '\n\n---\n\n'
    for item in letters[letter]:
        readme_content += '- [' + item + '](/' + item + ')\n'
    readme_content += '\n'

# write content on readme.md
f = open(project_dir + '/README.md', 'w')
f.write(readme_content.strip())
f.close()
