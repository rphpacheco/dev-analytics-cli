import os
from .tree import tree

folders = [
    'stage/extract',
    'stage/transform',
    'stage/load',
]

def build():
    print('build project structure')
    path = os.getcwd()

    for folder in folders:
        os.makedirs(os.path.join(path, folder))
    
    tree(path)