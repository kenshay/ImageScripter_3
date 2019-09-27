
try:
    import os
    LaunchPath = os.getcwd()
    #LaunchPath = r'C:\Eluminate'

    #print(LaunchPath)

    python = LaunchPath + r"\System\ImageScripter\python.exe"
    hub = LaunchPath + r"\System\ImageScripter\Lib\site-packages\Hub\hub.py"


    path = python + ' ' + hub
    ##os.system(r"C:\ImageScripter_2\python.exe C:\ImageScripter_2\Lib\site-packages\Script_Writer\script_writer.py")
    os.system(path)

except Exception as e:
    print(e)
    input()


#C:\ImageScripter_3\EXE\Script_Writer.exeLib\site-packages\Script_Writer\script_writer.py