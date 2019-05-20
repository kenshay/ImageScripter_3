import os
print("Starting Reset")
gitProject = r"C:\ImageScripter_2"
git = "C:\Elan_Tools\Sync\cmd\git.exe"
os.chdir(gitProject)
os.system(git + ' reset --hard origin/master')
os.system(git + ' fetch --all')
os.system(git + ' reset --hard origin/master')
os.system(git + ' clean -f')
os.system(git + ' status')
input("Finished Reset")

