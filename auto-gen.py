#!/usr/bin/env python3

""" This script generates lot of things automatically """

import os.path
from os import listdir, rename, mkdir
from sys import exit as sys_exit
from json import loads as json_loads
from json import load as json_load
from json.decoder import JSONDecodeError
from pathlib import Path
from itertools import islice

"""
This script generates a table from languages and progress status of them.
We can see that in this table with languages READNE, books, resources and courses list are completed.
And writes generated table to the todo.md file
"""
def generate_status_table(project_dir=None):
    if project_dir == None:
        project_dir = os.path.dirname(os.path.abspath(__file__))

    # load list of languages
    output = """
## Current status of added languages

| Language | Readme | Books (at least 2 items) | Courses (at least 2 items) | Resources (at least 2 items) |
|----------|--------|--------------------------|----------------------------|------------------------------|
"""
    items = os.listdir(project_dir)
    items.sort()

    real_list = []

    for item in items:
        if item[0] not in ['.', '_'] and os.path.isdir(project_dir + '/' + item):
            # check which items completed

            readme = open(project_dir + '/' + item + '/README.md', 'r')
            readme_completed = '\n' in readme.read().strip()
            readme.close()

            books = open(project_dir + '/' + item + '/books.md', 'r')
            books_completed = books.read().strip().split('\n')
            books_completed = len([line for line in books_completed if line.strip().startswith('- [')]) >= 2
            books.close()

            courses = open(project_dir + '/' + item + '/courses.md', 'r')
            courses_completed = courses.read().strip().split('\n')
            courses_completed = len([line for line in courses_completed if line.strip().startswith('- [')]) >= 2
            courses.close()

            resources = open(project_dir + '/' + item + '/resources.md', 'r')
            resources_completed = resources.read().strip().split('\n')
            resources_completed = len([line for line in resources_completed if line.strip().startswith('- [')]) >= 2
            resources.close()

            # add item to the list
            real_list.append({
                'readme': readme_completed,
                'books': books_completed,
                'courses': courses_completed,
                'resources': resources_completed,
                'name': item,
            })

    # sort the loaded list
    tmp_list = {}
    for item in real_list:
        done_count = item['readme'] + item['books'] + item['courses'] + item['resources']
        if done_count < 4:
            tmp_list[str(done_count) + '-' + item['name']] = item
    keys = list(tmp_list.keys())
    keys.sort()
    new_list = []
    for k in keys:
        new_list.append(tmp_list[k])
    real_list = list(reversed(new_list))

    # generate output from loaded list
    for item in real_list:
        output += "| [🌐 " + item['name'] + "](/" + item['name'] + ") |"
        output += ('✅ Done!' if item['readme'] else '[ℹ️ Edit it!](/' + item['name'] + '/README.md)') + ' | '
        output += ('✅ Done!' if item['books'] else '[ℹ️ Add one!](/' + item['name'] + '/books.md)') + ' | '
        output += ('✅ Done!' if item['courses'] else '[ℹ️ Add one!](/' + item['name'] + '/courses.md)') + ' | '
        output += ('✅ Done!' if item['resources'] else '[ℹ️ Add one!](/' + item['name'] + '/resources.md)') + ' | '
        output += '\n'

    # write generated table
    spliter = '\n---\n'
    todo = open(project_dir + '/TODO.md', 'r')
    current_todo = todo.read()
    todo.close()
    current_todo = '\n' + current_todo.split(spliter, 1)[0].strip()
    new_todo = current_todo + '\n\n---\n' + output
    todo = open(project_dir + '/TODO.md', 'w')
    todo.write(new_todo)
    todo.close()

    print('TODO generated!')

"""
This script create a table from people who contribute and added Hello World language
for this repository. Which the first column is the name and the second one is how many language
contributor added to this repo and also if a contributor added more than 5 language
contributor will receive a badge after his name
"""
def generate_contributors_table(project_dir = None):
    if project_dir == None:
        project_dir = os.path.dirname(os.path.abspath(__file__))

    # loading list of languages
    output = """
## List of people who contribute on this repository

| Name | Added languages |
|------|-----------------|
"""
    items = os.listdir(project_dir)
    items.sort()

    contributors = {}
    
    for item in items:
        if item[0] not in ['.','_'] and os.path.isdir(project_dir + '/' + item):
            try:
                with open(project_dir + '/' + item + '/info.json') as json_file:
                    contributor = json_load(json_file)

                    creators = []

                    try:
                        creators = contributor['creators']
                        if type(creators) == dict:
                            creators = [creators]
                    except KeyError:
                        creators = []

                    for creator in creators:
                        try:
                            contributors[creator['link']]
                        except KeyError:
                            contributors[creator['link']] = creator
                            contributors[creator['link']]['count'] = 0
                        contributors[creator['link']]['count'] += 1
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

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '

project_dir = os.path.dirname(os.path.abspath(__file__))
""" The project directory path """

items = listdir(project_dir)

langs = []
""" Found languages """

for item in items:
    if os.path.isdir(item) and item[0] not in ['.', '_']:
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

Special thanks to [Parsa](https://github.com/parsampsh) & [Amirhossein](https://github.com/amireshoon)

'''

for letter in letters:
    readme_content += '[' + letter + '](#' + letter + ') '

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
            rename(old_name, item)

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
            mkdir(project_dir + '/' + item + '/examples')
            tmp_f = open(project_dir + '/' + item + '/examples/.gitkeep', 'w')
            tmp_f.write('')
            tmp_f.close()

        creators = None
        if os.path.isfile(project_dir + '/' + item + '/info.json'):
            try:
                f = open(project_dir + '/' + item + '/info.json', 'r')
                content = f.read()
                f.close()
                content = json_loads(content)
                try:
                    if type(content['creators']) == dict:
                        creators = [content['creators']]
                    elif type(content['creators']) == list:
                        creators = content['creators']
                except KeyError:
                    pass
            except JSONDecodeError:
                print(f'Error: invalid json data in {item}/info.json. ignored...')
                exit_code = 1

        readme_content += f'- [{item}](/{item})'

        if creators:
            readme_content += ' - Added By'

        if creators is not None:
            counter = 0
            for creator in creators:
                try:
                    creator_title = creator['title']
                except KeyError:
                    creator_title = None
                try:
                    creator_link = creator['link']
                except KeyError:
                    creator_link = None

                if creator_title is not None:
                    if creator_link is not None:
                        readme_content += f' <img src="{creator_link}.png?size={str(user_img_size)}"'\
                        f' width="{str(user_img_size)}" height="{str(user_img_size)}" /> '\
                        f'[' + creator_title + '](' + creator_link + ')'
                    else:
                        readme_content += creator_title
                    if counter < len(creators)-1:
                        readme_content += ', '
                counter += 1

        readme_content += '\n'
    readme_content += '\n'

# write content on readme.md
f = open(project_dir + '/README.md', 'w')
readme_content += '## Thanks to everyone who helped this repo :) \n\n'
readme_content += f'<a href="https://github.com/BlackIQ/Hello-World/graphs/contributors"><img src="https://contrib.rocks/image?repo=BlackIQ/Hello-World" /></a>'
f.write(readme_content.strip() + '\n')
f.close()

# autogen tree.txt
def tree(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
         length_limit: int=1000):
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path) # accept string coerceable to Path
    out = ''
    files = 0
    directories = 0
    def inner(dir_path: Path, prefix: str='', level=-1):
        nonlocal files, directories
        if not level:
            return # 0, stop iterating
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else:
            contents = list(dir_path.iterdir())
        # remove that items starts with `.`
        contents = [item for item in contents\
            if not str(item).replace('\\', '/').split('/')[-1][0] in ['.', '_']]
        contents.sort()
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                yield prefix + pointer + path.name
                files += 1
    out += dir_path.name + '\n'
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        out += line + '\n'
    if next(iterator, None):
        out += f'... length_limit, {length_limit}, reached, counted:' + '\n'
    out += f'\n{directories} directories' + (f', {files} files' if files else '') + '\n'
    # replace the first line with `.`
    out = '.\n' + out.split('\n', 1)[-1]
    tree_f = open(project_dir + '/tree.txt', 'w')
    tree_f.write(out)
    tree_f.close()

tree(project_dir)

print('Done!')

generate_status_table(project_dir)
generate_contributors_table(project_dir)

if exit_code != 0:
    print("Warning: some of info.json files are not valid. Process will be exited with 1 exit code")

sys_exit(exit_code)
