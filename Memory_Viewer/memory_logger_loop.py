SSH_Manager_Class = ''

from database_manager_for_memory_viewer import Database_Manager_Class







if __name__ == "__main__":
    while True:
        try:
            print("Start")
            database_location = r"C:\ImageScripter_2\Memory_Viewer\memory_viewer.db"  # name of the sqlite database file
            Database_Manager = Database_Manager_Class(database_location)
            Database_Manager.Log_Memory_Into_database()
            print("Finish")
        except Exception as e:
            print("Something Has Gone Wrong, Trying Again")
            print(e)

