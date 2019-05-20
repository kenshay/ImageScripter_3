import os
import shutil, errno

elan_folder = r"C:\ImageScripter_2\Lib\site-packages\elan"
old_elan = r"C:\Settings\elan"

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

print("Starting Reset")
gitProject = r"C:\ImageScripter_2"
git = "C:\Elan_Tools\Sync\cmd\git.exe"
os.chdir(gitProject)
os.system(git + ' reset --hard origin/master')
os.system(git + ' fetch --all')
os.system(git + ' reset --hard origin/master')
os.system(git + ' clean -f')
os.system(git + ' status')

try:
    shutil.rmtree(old_elan)
except Exception as e:
    print(e)
print('Please Wait...')
copyanything(elan_folder, old_elan)
input("Finished Reset")

