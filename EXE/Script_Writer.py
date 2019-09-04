
try:
    import os
    from paths import *
    path = Python_Exe_Location + ' ' + ImageScripter_Location + "Lib\site-packages\Script_Writer\script_writer.py"
    ##os.system(r"C:\ImageScripter_2\python.exe C:\ImageScripter_2\Lib\site-packages\Script_Writer\script_writer.py")
    os.system(path)

except Exception as e:
    print(e)
    input()


#C:\ImageScripter_3\EXE\Script_Writer.exeLib\site-packages\Script_Writer\script_writer.py