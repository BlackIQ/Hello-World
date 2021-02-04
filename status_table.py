#!/usr/bin/env python3

"""
This script generates a table from languages and progress status of them.
We can see that in this table with languages READNE, books, resources and courses list are completed.
And writes generated table to the todo.md file
"""

import os

output = """
## Current status of languages

| Language | Readme Completed | Books (minimal 2 items) | Courses (minimal 2 items) | Resources (minimal 2 items) |
|----------|------------------|-------------------------|---------------------------|-----------------------------|
"""

def main(project_dir=None):
    if project_dir == None:
        project_dir = os.path.dirname(os.path.abspath(__file__))

    # load list of languages
    global output
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
        output += "| [" + item['name'] + "](/" + item['name'] + ") |"
        output += ('Done!' if item['readme'] else '[Edit it!](/' + item['name'] + '/README.md)') + ' | '
        output += ('Done!' if item['books'] else '[Add one!](/' + item['name'] + '/books.md)') + ' | '
        output += ('Done!' if item['courses'] else '[Add one!](/' + item['name'] + '/courses.md)') + ' | '
        output += ('Done!' if item['resources'] else '[Add one!](/' + item['name'] + '/resources.md)') + ' | '
        output += '\n'

    # write generated table
    spliter = '\n---\n'
    todo = open(project_dir + '/TODO.md', 'r')
    current_todo = todo.read()
    todo.close()
    current_todo = current_todo.strip().split(spliter, 1)[0].strip()
    new_todo = current_todo + '\n\n---\n' + output
    todo = open(project_dir + '/TODO.md', 'w')
    todo.write(new_todo)
    todo.close()

    print('TODO generated!')

if __name__ == '__main__':
    main()
