
import os
import subprocess
from imagescripter.core.variable_file_getter import Variable_File_Getter
from elan import *

#Viewer.Start()
#Viewer.CloseAndClean()

Controler_Build_Location = Variable_File_Getter.getVariableFromFile('Controler_Build_Location')
Controler_IP = Variable_File_Getter.getVariableFromFile('Controller_IP')
Controler_Name = Variable_File_Getter.getVariableFromFile('Controller_Name')
Controler_Password = Variable_File_Getter.getVariableFromFile('Controller_Password')





os.chdir(Controler_Build_Location)

Build = os.listdir()[0]


#subprocess.check_call([Build])
subprocess.Popen(Build)


print('Start')
Extracting.Wait()
ElanUpgrade.Wait()
for i in range(100):
    try:
        ElanUpgrade.selectasystem.Wait()
        break
    except:
        Sleep(1)
print('ready')

for i in range(100):
    try:
        ElanUpgrade.ListBox.Select(0,Controler_IP)
        Sleep(2)
        print(Controler_Password)
        ElanUpgrade.Edit.SetText(1,Controler_Password)
        Sleep(1)
        ElanUpgrade.RadioButton.Click('Skip Backup')
        Sleep(1)
        ElanUpgrade.Edit.SetText(1, Controler_Password)
        ElanUpgrade.PushButton.Click('Start')
        break
    except:
        Sleep(1)
        pass

for i in range(100):
    try:
        HlUpgrade.warninghardwire2.Wait()
        break
    except:
        Sleep(1)
HlUpgrade.PushButton.Click('Yes')
for i in range(100):
    try:
        UpgradingSystem.totalprogressitemprogress.Wait()
    except:
        Sleep(1)
UpgradingSystem.totalprogressitemprogress.WaitVanish()

HlUpgrade.PushButton.Click('Yes')
HlUpgrade.finished.Wait()
HlUpgrade.PushButton.Click('OK')








'''
"""

def Upgrade(self):
    from elan import ElanUpgrade
    from elan import HlConfig
    #############################################
    def Upgrade():
        Say("Upgrading Configurator")
        from elan import Configurator
        from elan import ElanUpgrade as EU
        from elan import HlUpgrade
        Configurator.WaitForControllerToComeBackOnline()
        try:
            EU.Close()
        except:
            pass
        EU.Start()
        sleep(5)
        print("EU.SelectController()")
        EU.SelectController()
        sleep(3)
        # password
        EU.Edit.SetText(1, ElanSettings.ControllerPassword)
        print("EU.PushButton.Click('Start')")
        sleep(3)
        EU.SelectController()
        EU.PushButton.Click('Start')
        print("HlUpgrade.warning.Wait()")
        sleep(10)
        try:
            HlUpgrade.warninghardwire2.Wait(seconds=20)
        except:
            HlUpgrade.warninghardwire.Wait()
        # HlUpgrade.warning.Wait()
        print("HlUpgrade.PushButton.Click('Yes')")
        HlUpgrade.PushButton.Click('Yes')
        try:
            HlUpgrade.yes.Click()
        except:
            pass
        sleep(1)
        # HlUpgrade.warning2.Wait(seconds=300)
        try:
            HlUpgrade.warningthesoftwareupdatehasbeensent2.Wait(seconds=300)
        except:
            HlUpgrade.warningthesoftwareupdatehasbeensent.Wait()
        sleep(5)
        HlUpgrade.PushButton.Click('OK')
        # print("HlUpgrade.controllercomplete.Wait(seconds=300)")
        # HlUpgrade.controllercomplete.Wait(seconds=300)
        # print("HlUpgrade.PushButton.Click('OK')")
        # HlUpgrade.PushButton.Click('OK')
        # print("EU.waitForControllerToComeBackOnline()")
        EU.waitForControllerToComeBackOnline()
        print('done')

    #######################################################################
    x = 0
    while True:
        try:
            print("####################Update Controller#########################")
            Upgrade()
            break
        except Exception as e:
            print('Could not upgrade controller')
            print(e)
            raise

            try:
                ElanUpgrade.Close()
                HlConfig.Close()
            except:
                pass
            sleep(x)
            x += 1
            pass

"""
'''