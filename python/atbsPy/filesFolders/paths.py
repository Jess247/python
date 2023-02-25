from pathlib import Path
import os
# create paths
print(Path('spam', 'bacon', 'egg'))
# concatenate paths
print(Path('spam') / 'bacon' / 'eggs')
print(Path('dog')/Path('cat/hamster'))
print(Path('bird')/Path('plane', 'helicopter'))
homeFolder = Path('/Users/Jess')
subfolder = Path('spam')
print(homeFolder / subfolder)
# current working directory
print(Path.cwd())
# change current working directory
os.chdir('/User/sample')  # throws error because folder doesn't exist
# user directory
print(Path.home)
# make multiple directories
os.makedirs('/Users/sample/test/foldr')
# single directory
Path('/User/sample').mkdir()
# absolute path true/false
Path.cwd().is_absolute()
