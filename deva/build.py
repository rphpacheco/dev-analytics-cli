import os
from .tree import tree

folders = [
    ['app/prd',[
        'application.pbix'
    ]],
    ['app/qa',[
        'application.pbix'
    ]],
    ['loads/extract', [
        'extract.qvs',
        'extract.qvw',
    ]],
    ['loads/transform', [
        'transform.qvs',
        'transform.qvw',
    ]],
    ['loads/model', [
        'model.qvs',
        'model.qvw',
    ]],
    ['config', [
        'config.qvs'
    ]],
]

def build():
    print('build project structure')
    rootPath = os.getcwd()

    for folder in folders:
        path = os.path.join(rootPath, folder[0])
        if os.path.exists(path):
            print(f'directory {folder[0]} has exists!')
        else:
            os.makedirs(path)
        
        for file in folder[1]:
            fileName = os.path.join(path, file)
            if os.path.exists(fileName):
                print(f'file {file} has exists')
            else:
                with open(fileName, 'a'):
                    os.utime(fileName, None)
    
    tree(rootPath)