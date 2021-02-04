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
