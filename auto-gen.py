#!/usr/bin/env python3

""" This script generates lot of things automatically """

import os
import sys
import json
import platform

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

This repository contains a big list of programming languages and some **examples** for them. Also there are some **descriptions** about them. If you want to learn a programming language, the decriptions and examples for that language in this repo might be helpful.
Also there is list of useful **Courses** and **Books** about the programming languages in this repository. You can check different languages, see the examples and syntax of the language, then you can see courses list and books list of each language and starting learning one!

## Contributing
If you want to contribute to this project, read [Contributing Guide](CONTRIBUTING.md).

Total Languages in This Repository: {count}.

'''

user_img_size = 25
""" Width and Height of user profile img in readme """

exit_code = 0
""" Will be changed to 1 when some of info.json files are not valid """

for letter in letters:
    readme_content += '\n### ' + letter.upper() + '\n\n---\n\n'
    for item in letters[letter]:
        if ' ' in item:
            old_name = item
            item = item.replace(' ', "-")
            os.rename(old_name, item)

        required_files = ['courses.md', 'books.md', 'README.md', 'resources.md']
        for required_file in required_files:
            if not os.path.isfile(project_dir + '/' + item + '/' + required_file):
                tmp_f = open(project_dir + '/' + item + '/' + required_file, 'w')
                content = ''
                if required_file == 'README.md':
                    content = '# ' + item + '\n'
                elif required_file == 'books.md':
                    content = '# Useful Books for ' + item + '\n'
                elif required_file == 'courses.md':
                    content = '# Useful Tutorial courses for ' + item + '\n'
                elif required_file == 'resources.md':
                    content = '# Useful Resources for ' + item + '\n'
                tmp_f.write(content)
                tmp_f.close()
        if not os.path.isdir(project_dir + '/' + item + '/examples'):
            os.mkdir(project_dir + '/' + item + '/examples')
            tmp_f = open(project_dir + '/' + item + '/examples/.gitkeep', 'w')
            tmp_f.write('')
            tmp_f.close()

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
                exit_code = 1

        if creator_title != None:
            if creator_link != None:
                readme_content += '- [' + item + '](/' + item + ') - Added By <img src="' + creator_link + '.png?size=' + str(user_img_size) + '" width="' + str(user_img_size) + '" height="' + str(user_img_size) + '" /> [' + creator_title + '](' + creator_link + ')\n'
            else:
                readme_content += '- [' + item + '](/' + item + ') - Added By ' + creator_title + '\n'
        else:
            readme_content += '- [' + item + '](/' + item + ')\n'
    readme_content += '\n'

# write content on readme.md
f = open(project_dir + '/README.md', 'w')
f.write(readme_content.strip() + '\n')
f.close()

# autogen tree.txt
if platform.system() != 'Windows':
    os.system('tree > tree.txt')

print('Done!')

if exit_code != 0:
    print("Warning: some of info.json files are not valid. Process will be exited with 1 exit code")

sys.exit(exit_code)
