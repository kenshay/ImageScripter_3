# -*- coding: utf-8 -*-
import paramiko
from scp import SCPClient
from datetime import datetime
import time
import io
from paths import *

##destination_File2 = r"C:\Elan_Tools\Data\Build_Raw_File.txt"
##destination_File3 = r"C:\Elan_Tools\Data\Name_Raw_File.txt"


def getTime():
    now = datetime.now()
    return now.strftime("%c")
def get_day_of_week():
    datet = getTime()
    List = datet.split(' ')
    return List[0]
def get_month_and_day():
    datet = getTime()
    List = datet.split(' ')
    return List[1] + ' ' + List[2]
def get_time_of_day():
    datet = getTime()
    List = datet.split(' ')
    return List[3]
def get_year():
    datet = getTime()
    List = datet.split(' ')
    return List[4]
def get_index_time():
    return time.time()


class SSH_Manager_Class():
    def __init__(self,ipaddress,port,username,password):
        self.ipadress = ipaddress
        self.port = port
        self.username = username
        self.password = password
    def get_percent_of_memory_In_Use(self):
        print('Getting Memory In Use')
        for i in range(2):
            try:
                #print('get_percent_of_memory_In_Use')
                nbytes = 4096
                command = """free | grep Mem | awk '{print $3/$2 * 100.0}'"""
                def createSSHClient():
                    client = paramiko.SSHClient()
                    #client.load_system_host_keys()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(self.ipadress, self.port, self.username, self.password)
                    return client
                client = paramiko.Transport((self.ipadress, self.port))
                client.connect(username=self.username, password=self.password)
                stdout_data = []
                stderr_data = []
                session = client.open_channel(kind='session')
                session.exec_command(command)
                while True:
                    if session.recv_ready():
                        data = session.recv(nbytes)
                        stdout_data.append(data)
                        #print(data)
                    if session.recv_stderr_ready():
                        dataer = session.recv_stderr(nbytes)
                        stderr_data.append(dataer)
                        raise ValueError(dataer)
                    if session.exit_status_ready():
                        break
                session.close()
                string = str(stdout_data[0])
                break
            except IndexError:
                pass
        string = str(stdout_data[0])
        string = string.replace("b'",'')
        string = string.replace("\\n",'')
        string = string.replace("'",'')
        Float = float(string)
        print(Float)
        return Float
    def get_percent_of_memory_free(self):
        print('Getting Memory Free')
        nbytes = 4096
        command = """free | grep Mem | awk '{print $4/$2 * 100.0}'"""
        def createSSHClient():
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ipadress, self.port, self.username, self.password)
            return client
        client = paramiko.Transport((self.ipadress, self.port))
        client.connect(username=self.username, password=self.password)
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')
        session.exec_command(command)
        while True:
            if session.recv_ready():
                data = session.recv(nbytes)
                stdout_data.append(data)
                #print(data)
            if session.recv_stderr_ready():
                dataer = session.recv_stderr(nbytes)
                stderr_data.append(dataer)
                raise ValueError(dataer)
            if session.exit_status_ready():
                break
        session.close()
        string = str(stdout_data[0])
        string = string.replace("b'",'')
        string = string.replace("\\n",'')
        string = string.replace("'",'')
        Float = float(string)
        print(Float)
        return Float
    def get_percent_of_cpu_usage_used(self):
        print('Getting CPU Usage')
        #print('get_percent_of_cpu_usage_used')
        nbytes = 4096
        command = """grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage ""}'"""
        def createSSHClient():
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ipadress, self.port, self.username, self.password)
            return client
        client = paramiko.Transport((self.ipadress, self.port))
        client.connect(username=self.username, password=self.password)
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')
        session.exec_command(command)
        while True:
            if session.recv_ready():
                data = session.recv(nbytes)
                stdout_data.append(data)
                #print(data)
            if session.recv_stderr_ready():
                dataer = session.recv_stderr(nbytes)
                stderr_data.append(dataer)
                raise ValueError(dataer)
            if session.exit_status_ready():
                break
        session.close()
        stdout_data[0]
        string = str(stdout_data[0])
        string = string.replace("b'",'')
        string = string.replace("\\n",'')
        string = string.replace("'",'')
        Float = float(string)
        print(Float)
        return Float
    def get_GateWayProcessID(self):
        print('Getting GATEWAY PID')
        #print('get_GateWayProcessID')
        nbytes = 4096
        command = """pidof GATEWAY"""
        def createSSHClient():
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ipadress, self.port, self.username, self.password)
            return client
        client = paramiko.Transport((self.ipadress, self.port))
        client.connect(username=self.username, password=self.password)
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')
        session.exec_command(command)
        while True:
            if session.recv_ready():
                data = session.recv(nbytes)
                stdout_data.append(data)
                #print(data)
            if session.recv_stderr_ready():
                dataer = session.recv_stderr(nbytes)
                stderr_data.append(dataer)
                #print(dataer)
            if session.exit_status_ready():
                break
        session.close()
        string = str(stdout_data[0])
        string = string.replace("b'",'')
        string = string.replace("\n",'')
        string = string.replace("'",'')
        string = string.replace("\\n",'')
        pid = int(string)
        #print(pid)
        print(pid)
        return pid
    def get_Start_Date_Of_GateWay(self):
        print('Getting GATEWAY Start Date')
        pid = str(self.get_GateWayProcessID())
        for i in range(13):
            try:
                #print('trying -> ',i)
                #print('get_Start_Date_Of_GateWay')
                nbytes = 4096
                command = """ls -ltrh /proc | grep #pid#"""
                command = command.replace('#pid#',pid)
                def createSSHClient():
                    client = paramiko.SSHClient()
                    #client.load_system_host_keys()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(self.ipadress, self.port, self.username, self.password)
                    return client
                client = paramiko.Transport((self.ipadress, self.port))
                client.connect(username=self.username, password=self.password)
                stdout_data = []
                stderr_data = []
                session = client.open_channel(kind='session')
                session.exec_command(command)
                while True:
                    if session.recv_ready():
                        data = session.recv(nbytes)
                        stdout_data.append(data)
                        #print(data)
                    if session.recv_stderr_ready():
                        dataer = session.recv_stderr(nbytes)
                        stderr_data.append(dataer)
                        raise ValueError(dataer)
                    if session.exit_status_ready():
                        break
                session.close()
                string = str(stdout_data[0])
                break
            except IndexError as e:
                #print(e)
                pass
        string = str(stdout_data[0])
        string = string.replace("b'",'')
        List = string.split(' 0 ')
        date = List[1]
        List = date.split('           0 ')

        date = List[0]

        List = date.split(' ')

        date = List[0] + ' ' + List[1] + ' ' + List[2]


        return date
    def get_Build(self):
        print('Getting Controller Build')
        def createSSHClient():
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ipadress, self.port, self.username, self.password)
            return client
        ssh = createSSHClient()
        scp = SCPClient(ssh.get_transport())
        scp.get('/ELAN/CONFIG/SYSTEM.DAT', destination_File2)
        junk_list = []
        with io.open(destination_File2, 'r', encoding='cp1252', errors='ignore') as f:
            for line in f:
                junk_list.append(line)
        whole_string = junk_list[0]
        #whole_string = whole_string.encode('utf-8')

        whole = whole_string.split('Build')
        left = whole[0]
        right = "Build" + whole[1]
        Build = left[-4:] + right[:15]
        Build = Build.replace(" Re", '')
        Build = Build.replace('', '')
        Build = Build.replace(' ', '')
        Build = Build.replace('Build', '.')
        Build = Build.replace("l", '')
        Build = Build.rstrip('\x00')
        print(Build)
        return Build
    def get_Controller_Name(self):
        print('Getting Controller Name')
        def createSSHClient():
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.ipadress, self.port, self.username, self.password)
            return client
        ssh = createSSHClient()
        scp = SCPClient(ssh.get_transport())
        scp.get('/ELAN/CONFIG/SECURE.DAT', destination_File3)
        junk_list = []
        with io.open(destination_File3, 'r', encoding='cp1252', errors='ignore') as f:
            for line in f:
                junk_list.append(line)
        whole_string = junk_list[0]
        whole_string = str(whole_string.encode('utf-8'))
        List = whole_string.split('SC')
        print(List)
        Build = 'SC' + List[1]
        Build = str(Build)
        print(type(Build))
        print(Build)
        return Build

if __name__ == "__main__":
    SSH_Manager = SSH_Manager_Class(ipaddress='192.168.0.121', port=2199, username='root', password='elanscX')

    #Index_Time = get_index_time()
    #Controller_Name = 'Default'
    #Time_Date_Year = getTime()
    #Controller_Version = SSH_Manager.get_Build()
    Memory_In_Use = SSH_Manager.get_percent_of_memory_In_Use()
    Memory_Free = SSH_Manager.get_percent_of_memory_free()
    CPU_Usage = SSH_Manager.get_percent_of_cpu_usage_used()
    #Controller_Startup_Time = SSH_Manager.get_Start_Date_Of_GateWay()
    #Controller_Name = SSH_Manager.get_Controller_Name()



