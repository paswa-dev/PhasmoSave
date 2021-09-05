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
sg.set_options()

layout = [
    [sg.Text('Please enter stats')],
    [sg.Text('Level', size =(15, 1)), sg.InputText()],
    [sg.Text('Money', size =(15, 1)), sg.InputText()]

]

layout2 =[
    [sg.Text('Please enter item stats')],
    [sg.Text('Item Amounts', size=(15,1)), sg.InputText()]

]

tab_manager = [
    [sg.TabGroup([
        [sg.Tab('Main Stats', layout, title_color='Red',border_width=10,tooltip='Main Stats', element_justification= 'center')],
        [sg.Tab('Item Stats', layout2, title_color='Red',border_width=10,tooltip='Item Stats')]
    ],
    border_width=5
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

    

    window = sg.Window('PhasmoSave : Paswa',tab_manager, icon=r'asset/icon.ico' )
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
            if Name.__contains__('Inventory'):
                _number["Value"] = values[2]
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
