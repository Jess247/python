from pathlib import Path
import os
# find attributes from file path
p = Path('/Users/Jess/Desktop/python/python/atbsPy/filesFolders/paths_2.py')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)  # empty string on linux and mac
# parents
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])
print(Path.cwd().parents[3])
# os examples
calcFilePath = '/atbsPy/filesFolders/paths_2.py'
print('basename: ', os.path.basename(calcFilePath))
print('dirname: ', os.path.dirname(calcFilePath))
# tupel of both strings
print('split: ', os.path.split(calcFilePath))
print('tupel: ', (os.path.basename(calcFilePath),
      os.path.dirname(calcFilePath)))  # split is best practice
# return string list of path
print(calcFilePath.split(os.sep))
# check paths
print('exists: ', p.exists())
print('is file: ', p.is_file())
print('is dir: ', p.is_dir())
print('os exists: ', os.path.exists(p))
print('os is file: ', os.path.isfile(p))
print('os is dir: ', os.path.isdir(p))
