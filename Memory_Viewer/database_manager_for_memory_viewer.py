import sqlite3
import shutil
import os
import time
from ssh_manager_for_memory_viewer import *

fresh_data_base = r"C:\ImageScripter_2\Memory_Viewer\Fresh\memory_viewer_fresh.db"

class Database_Manager_Class():
    def __init__(self,database_location):
        self.database_location_file = database_location
        self.database_folder_location = os.path.dirname(self.database_location_file)
        self.database_name = os.path.basename(self.database_location_file)
        self.database_name_without_db = self.database_name.strip('.db')
        if os.path.isfile(self.database_location_file) == False:
            self.Create_New_Database()
        else:
            print('Fount Database -> ',self.database_location_file)

    def Log_Memory_Into_database(self):
        print("Logging Memory Data Into Database")
        SSH_Manager = SSH_Manager_Class(ipaddress='192.168.0.104', port=2199, username='root', password='elanscX')
        Index_Time = get_index_time()
        Controller_Name = SSH_Manager.get_Controller_Name()
        Time_Date_Year = getTime()
        Controller_Version = SSH_Manager.get_Build()
        Memory_In_Use = SSH_Manager.get_percent_of_memory_In_Use()
        Memory_Free = SSH_Manager.get_percent_of_memory_free()
        CPU_Usage = SSH_Manager.get_percent_of_cpu_usage_used()
        Controller_Startup_Time = SSH_Manager.get_Start_Date_Of_GateWay()
        conn = sqlite3.connect(self.database_location_file)
        c = conn.cursor()
        c.execute('''INSERT INTO Reports(Index_Time,Controller_Name,Time_Date_Year,Controller_Version,Memory_In_Use,Memory_Free,CPU_Usage,Controller_Startup_Time)
                                  VALUES(?,?,?,?,?,?,?,?)''',
                  (Index_Time,Controller_Name,Time_Date_Year,Controller_Version,Memory_In_Use,Memory_Free,CPU_Usage,Controller_Startup_Time))
        conn.commit()
        conn.close()
        print("Memory Has Been Logged Into Database")

    def Create_New_Database(self):
        print("Creating New Database -> ",self.database_location_file)
        lastcmd = os.getcwd()
        Folder = self.database_folder_location
        os.chdir(Folder)
        shutil.copy(fresh_data_base,self.database_location_file)
        os.chdir(lastcmd)
        print("New Database Created -> ", self.database_location_file)

if __name__ == "__main__":
    database_location = r"C:\ImageScripter_2\Memory_Viewer\memory_viewer.db"  # name of the sqlite database file
    Database_Manager = Database_Manager_Class(database_location)
    Database_Manager.Log_Memory_Into_database()