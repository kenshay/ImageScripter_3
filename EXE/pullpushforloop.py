from paths import *
import os
import shutil, errno
from dirsync import sync


print('Git Repo -> ',gitProject)
os.chdir(gitProject)




os.system(git + ' pull')
os.system(git + ' add --all')
os.system(git + ' commit -a -m "auto update"')
#os.system(git + ' fetch --all')
#os.system(git + ' reset --hard origin/master')
#os.system(git + ' clean -f')
#os.system(git + ' status')
#print('Please do not close this window.')

