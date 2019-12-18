import os
from paths import *
import socket
import pickle
HOST = '127.0.0.1'
PORT = 65432
import time
import subprocess
import os
def isProgramRunning():
    try:
        already_opened = True
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((HOST,PORT))
        #print(result)
        if result == 0:
           sock.close()
           print('ScriptRunner is already running, skipping')
           return True

        else:
           sock.close()
           print('ScriptRunner is not running, starting')
           return False
    except Exception as e:
        try:
            sock.close()
        except Exception as e:
            print(e)

try:
    if not isProgramRunning():
        print('Sleeping 10')
        time.sleep(10)
        if not isProgramRunning():
            print('Sleeping 10')
            time.sleep(10)
            if not isProgramRunning():
                print('Sleeping 10')
                time.sleep(10)
                try:
                    isRunning = False
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((HOST, PORT))
                        #s.sendall(b'close()')
                        s.sendall(b'isRunning()')
                        data = s.recv(1024)
                        #msg = data.decode()
                        msg = data
                        isRunning = pickle.loads(msg)
                except Exception as e:
                    print(e)
                    isRunning = False

                if isRunning == False:
                    print('Script Runner is not running, starting,')
                    #os.system(Python_Exe_Location + ' ' + Script_Runner_Gui_Location + ' True ' + '&')
                    p = subprocess.Popen([Python_Exe_Location,Script_Runner_Gui_Location,'True','&'])
                    print(p.pid)

                else:
                    print('Script Runner is already running, ignoring.')
except Exception as e:
    print(e)

#os.chdir('C:\Eluminate\System\ImageScripter\Scripts')
#os.system('pyinstaller --onefile --noconsole C:\Eluminate\System\ImageScripter\EXE\Script_Runner_GUI_On_Startup.py')