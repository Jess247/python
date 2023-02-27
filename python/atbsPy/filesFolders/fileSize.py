from pathlib import Path
import os
# returns size of file in byte
print(os.path.getsize('atbsPy/filesFolders/paths_2.py'))
print(os.listdir('atbsPy/filesFolders'))
# total size of path
totalSize = 0
for fileName in os.listdir('atbsPy/filesFolders'):
    totalSize = totalSize + \
        os.path.getsize(os.path.join('atbsPy/filesFolders', fileName))
print('total size of path: ', totalSize)
# file list with glob()
p = Path('atbsPy/filesFolders')
p.glob('*')  # * stands for multiple symbols and characters and ? for a single one
print(list(p.glob('*')))
print(list(p.glob('*.py')))  # returns only files with .py
print(list(p.glob('*.?y')))
