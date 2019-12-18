from imagescripter.core.windows_service import SMWinservice

import time
import random
from pathlib import Path
import os
from paths import *

class PythonCornerExample(SMWinservice):
    _svc_name_ = "ScriptRunner Monitor Service"
    _svc_display_name_ = "ScriptRunner Monitor Service"
    _svc_description_ = "This keeps ScripRunner Running"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while self.isrunning:
            try:
                import socket
                import pickle
                HOST = '127.0.0.1'
                PORT = 65432
                isRunning = False
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    # s.sendall(b'close()')
                    s.sendall(b'isRunning()')
                    data = s.recv(1024)
                    # msg = data.decode()
                    msg = data
                    isRunning = pickle.loads(msg)
            except Exception as e:
                print(e)
                isRunning = False
            if isRunning == False:
                print('Script Runner is not running, starting,')
                os.system(Python_Exe_Location + ' ' + Script_Runner_Gui_Location + ' True ' + '&')
                # subprocess.Popen([Python_Exe_Location, "-r", "some.file"])
                print('TEST')
            else:
                print('Script Runner is already running, ignoring.')


if __name__ == '__main__':
    PythonCornerExample.parse_command_line()

    #C:\Eluminate\System\ImageScripter\python.exe C:\Eluminate\System\ImageScripter\EXE\Script_Runner_Monitor_Service.py install