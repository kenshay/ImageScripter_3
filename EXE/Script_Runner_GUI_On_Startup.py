import os
from paths import *




try:
    import socket
    import pickle
    HOST = '127.0.0.1'
    PORT = 65432
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
    os.system(Python_Exe_Location + ' ' + Script_Runner_Gui_Location + ' True ' + '&')
    #subprocess.Popen([Python_Exe_Location, "-r", "some.file"])
    print('TEST')
else:
    print('Script Runner is already running, ignoring.')


