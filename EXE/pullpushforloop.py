from paths import *
import os
import shutil, errno
from dirsync import sync
print('Git Repo -> ',gitProject)
os.chdir(gitProject)
os.system(git + ' pull')
os.system(git + ' add --all')
os.system(git + ' commit -a -m "auto update"')
os.system(git + ' push')
os.system(git + ' status')


