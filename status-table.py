#!/usr/bin/env python3

import os

output = """
| Language | Readme | Books | Courses | Resources |
|----------|--------|-------|---------|-----------|
"""

items = os.listdir()
items.sort()

for item in items:
    if item[0] != '.' and os.path.isdir(item):
        readme = open(item + '/README.md', 'r')
        readme_completed = '\n' in readme.read().strip()
        readme.close()

        books = open(item + '/books.md', 'r')
        books_completed = books.read().strip().split('\n')
        books_completed = len([line for line in books_completed if line.strip().startswith('- [')]) >= 2
        books.close()

        courses = open(item + '/courses.md', 'r')
        courses_completed = courses.read().strip().split('\n')
        courses_completed = len([line for line in courses_completed if line.strip().startswith('- [')]) >= 2
        courses.close()

        resources = open(item + '/resources.md', 'r')
        resources_completed = resources.read().strip().split('\n')
        resources_completed = len([line for line in resources_completed if line.strip().startswith('- [')]) >= 2
        resources.close()


        output += "|"+item+"|"
        output += '<ul><li>[' + ('x' if readme_completed else ' ') + ']</li></ul>|'
        output += '<ul><li>[' + ('x' if books_completed else ' ') + ']</li></ul>|'
        output += '<ul><li>[' + ('x' if courses_completed else ' ') + ']</li></ul>|'
        output += '<ul><li>[' + ('x' if resources_completed else ' ') + ']</li></ul>|'

        output += '\n'


print(output)

