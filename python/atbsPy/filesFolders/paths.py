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
# os.chdir('/User/sample')  # throws error because folder doesn't exist
# user directory
print(Path.home)
# make multiple directories
# os.makedirs('/Users/sample/test/foldr')
# single directory
# Path('/User/sample').mkdir()
# absolute path true/false
Path.cwd().is_absolute()  # True
Path('spa,/bacon/eggs').is_absolute()  # False
# os functions
print(os.path.abspath('.'))
print(os.path.abspath('./scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('/user/mac', '/user'))
print(os.path.relpath('/user', '/user/spam/eggs'))
