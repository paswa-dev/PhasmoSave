import os
import json
import sys
import PySimpleGUI as sg

if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation') # Arbitrary string



import getpass
import subprocess
from time import sleep
from colorama import init
init()
from colorama import Fore, Back, Style




sg.theme('DarkAmber')

layout = [
    [sg.Text('Stats')],
    [sg.Text('Level', size =(20, 1)), sg.InputText()],
    [sg.Text('Money', size =(20, 1)), sg.InputText()]

]

layout2 =[
    [sg.Text('Items')],
    [sg.Column([
    [sg.Text('EMF Reader', size=(20,1)), sg.InputText()],
    [sg.Text('Flashlight', size=(20,1)), sg.InputText()],
    [sg.Text('Photo Camera', size=(20,1)), sg.InputText()],
    [sg.Text('Lighter', size=(20,1)), sg.InputText()],
    [sg.Text('Candle', size=(20,1)), sg.InputText()],
    [sg.Text('UV Light', size=(20,1)), sg.InputText()],
    [sg.Text('Crucifx', size=(20,1)), sg.InputText()],
    [sg.Text('Video Camera', size=(20,1)), sg.InputText()],
    [sg.Text('Spirit Box', size=(20,1)), sg.InputText()],
    [sg.Text('Salt', size=(20,1)), sg.InputText()],
    [sg.Text('Smudge Sticks', size=(20,1)), sg.InputText()],
    [sg.Text('Tripod', size=(20,1)), sg.InputText()],
    [sg.Text('Strong Flashlight', size=(20,1)), sg.InputText()],
    [sg.Text('Motion Sensor', size=(20,1)), sg.InputText()],
    [sg.Text('Sound Sensor', size=(20,1)), sg.InputText()],
    [sg.Text('Thermometer', size=(20,1)), sg.InputText()],
    [sg.Text('Sanity Pills', size=(20,1)), sg.InputText()],
    [sg.Text('Ghost Writing Book', size=(20,1)), sg.InputText()],
    [sg.Text('Infared Light Sensor', size=(20,1)), sg.InputText()],
    [sg.Text('Parabolic Microphone', size=(20,1)), sg.InputText()],
    [sg.Text('Glowstick', size=(20,1)), sg.InputText()],
    [sg.Text('Head Mounted Camera', size=(20,1)), sg.InputText()],
    ])]

]

tab_manager = [
    [sg.TabGroup([
        [sg.Tab('Main Stats', layout, title_color='Red',border_width=10,tooltip='Main Stats', element_justification= 'center')],
        [sg.Tab('Item Stats', layout2, title_color='Red',border_width=10,tooltip='Item Stats')]
    ],
    border_width=8
    ),
    sg.Button('Submit')
    ]]




user = getpass.getuser()

area = os.getcwd()
file_area = f'asset\\Save Crypter.exe'
path = os.path.join(area, file_area)
file = path


def workStart():
    print('Below is the list of items. Change accordingly.')
    with open(f"C:\\Users\\{user}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\saveData.txt", "r", encoding="utf-8") as f3:
        data = json.load(f3)

    #Xp = int(input('What level do you want?\n> '))
    #Xp = Xp * 100
    #Money = int(input('How much money would you like?\n> '))
    #InventoryNumber = int(input('What amount of items would you like?\n> '))

    

    window = sg.Window('PhasmoSave : Paswa',tab_manager, icon=r'asset/icon.ico').finalize()
    
    event, values = window.read()
    window.close()
    
    

    print('Please note that the current level is the max. Do not go above 60 on tools. And keep money below 5k.\n If any value is set as 2, 1, 0 DO NOT CHANGE IT AND SET TO ORIGINAL')
    for _number in data['IntData']:
            Number = _number['Value']
            Name = _number['Key']
            print('\n')

            Xp = int(values[0]) * 100

            if Name == 'myTotalExp':
                _number['Value'] = Xp
            if Name == 'PlayersMoney':
                _number['Value'] = values[1]
            if Name == 'EMFReaderInventory':
                _number["Value"] = values[2]
            if Name == 'FlashlightInventory':
                _number["Value"] = values[3]
            if Name == 'CameraInventory':
                _number["Value"] = values[4]
            if Name == 'CameraNnventory':
                _number["Value"] = values[4]
            if Name == 'KighterInventory':
                _number["Value"] = values[5]
            if Name == 'LighterInventory':
                _number["Value"] = values[5]
            if Name == 'CandleInventory':
                _number["Value"] = values[6]
            if Name == 'UVFlashlightInventory':
                _number["Value"] = values[7]
            if Name == 'CrucifixInventory':
                _number["Value"] = values[8]
            if Name == 'DSLRCameraInventory':
                _number["Value"] = values[9]
            if Name == 'EVPrecorderInventory':
                _number["Value"] = values[10]
            if Name == 'EVPRecorderInventory':
                _number["Value"] = values[10]
            if Name == 'Saltinventory':
                _number["Value"] = values[11]
            if Name == 'SaltInventory':
                _number["Value"] = values[11]
            if Name == 'sageInventory':
                _number["Value"] = values[12]
            if Name == 'SageInventory':
                _number["Value"] = values[12]
            if Name == 'TripodInventory':
                _number["Value"] = values[13]
            if Name == 'StrongFlashlightInventory':
                _number["Value"] = values[14]
            if Name == 'MotionSensorInventory':
                _number["Value"] = values[15]
            if Name == 'SoundSensorInventory':
                _number["Value"] = values[16]
            if Name == 'SanityPillsInventory':
                _number["Value"] = values[17]
            if Name == 'ThermometerInventory':
                _number["Value"] = values[18]
            if Name == 'GhostWritingBookInventory':
                _number["Value"] = values[19]
            if Name == 'IRLightSensorInventory':
                _number["Value"] = values[20]
            if Name == 'ParabolicMicrophoneInventory':
                _number["Value"] = values[21]
            if Name == 'GlowstickInventory':
                _number["Value"] = values[22]
            if Name == 'HeadmountedCameraInventory':
                _number["Value"] = values[23]
            if Name == 'HeadMountedCameraInventory':
                _number["Value"] = values[23]
            #-------
            #-------    
            if Name == 'istutorial':
                _number['Value'] = 0
            if Name == 'isTutorial':
                _number['Value'] = 0
            if Name == 'setupPhase':
                _number['Value'] = 0
            if Name == 'StayInServerRoom':
                _number['Value'] = 0
            if Name == 'completeSraining':
                _number['Value'] = 1
            if Name == 'PlayerDied':
                _number['Value'] = 0
            if Name == 'MissionsStatus':
                _number['Value'] = 0
            if Name == 'LevelDifficulty':
                _number['Value'] = 4
            if Name == 'CompletedTraining':
                _number['Value'] = 1
            
    print(Fore.GREEN + 'Done')
    print('\n')
    with open(f"C:\\Users\\{user}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\saveData.txt", "w", encoding="utf-8") as f3:
        json.dump(data , f3)
    print(data)
    print(Style.BRIGHT + Fore.RED + 'Enabling Encrypter... DONT CLOSE')  
    print(Style.BRIGHT + Fore.RED + 'Enabling Encrypter.. DONT CLOSE')  
    print(Style.BRIGHT + Fore.RED + 'Enabling Encrypter. DONT CLOSE')
    sleep(2)
    print(Style.RESET_ALL)
    subprocess.call([file])


workStart()
