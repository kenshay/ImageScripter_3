
print("RESET IMAGESCRIPTER 2!\n")
import os
git = r"C:\Elan_Tools\Sync\bin\git.exe"
gitProject = r'C:\ImageScripter_2'
#gitProject = alist[0] + 'Elan_Tools\ImageScripter'
#git = "C:\Elan_Tools\Sync\cmd\git.exe"
os.chdir(gitProject)
os.system(git + ' reset --hard origin/master')
os.system(git + ' fetch --all')
os.system(git + ' reset --hard origin/master')
os.system(git + ' status')
input("Finished Reset")
