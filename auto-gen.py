#!/usr/bin/env python3

""" This script generates lot of things automatically """

import os.path
from os import listdir, rename, mkdir
from sys import exit as sys_exit
from json import loads as json_loads
from json.decoder import JSONDecodeError
from pathlib import Path
from itertools import islice

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

for letter in letters:
    readme_content += '[' + letter + '](#' + letter + ')'

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

        creator_title = None
        creator_link = None
        if os.path.isfile(project_dir + '/' + item + '/info.json'):
            try:
                f = open(project_dir + '/' + item + '/info.json', 'r')
                content = f.read()
                f.close()
                content = json_loads(content)
                try:
                    creator_title = content['creator']['title']
                    try:
                        creator_link = content['creator']['link']
                    except KeyError:
                        pass
                except KeyError:
                    pass
            except JSONDecodeError:
                print(f'Error: invalid json data in {item}/info.json. ignored...')
                exit_code = 1

        if creator_title is not None:
            if creator_link is not None:
                readme_content += f'- [{item}](/{item}) - Added By'\
                f' <img src="{creator_link}.png?size={str(user_img_size)}"'\
                f' width="{str(user_img_size)}" height="{str(user_img_size)}" /> '\
                f'[' + creator_title + '](' + creator_link + ')\n'
            else:
                readme_content += f'- [{item}](/{item}) - Added By {creator_title}\n'
        else:
            readme_content += '- [' + item + '](/' + item + ')\n'
    readme_content += '\n'

# write content on readme.md
f = open(project_dir + '/README.md', 'w')
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
            if not str(item).replace('\\', '/').split('/')[-1].startswith('.')]
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

if exit_code != 0:
    print("Warning: some of info.json files are not valid. Process will be exited with 1 exit code")

sys_exit(exit_code)
