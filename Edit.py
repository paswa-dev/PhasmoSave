import os
import json
import getpass
import subprocess
from time import sleep


user = getpass.getuser()

file = f'C:\\Users\\{user}\\Desktop\\Money Changer\\asset\\Save Crypter.exe'


def workStart():
    print('Below is the list of items. Change accordingly.')
    with open(f"C:\\Users\\{user}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\saveData.txt", "r", encoding="utf-8") as f3:
        data = json.load(f3)
        print('')
        print('')
        print('If not sure of something CHECK Current stuff above')
        print('')
        print('')

    print('Please note that the current level is the max. Do not go above 60 on tools. And keep money below 5k.\n If any value is set as 2, 1, 0 DO NOT CHANGE IT AND SET TO ORIGINAL')
    for _number in data['IntData']:
            Number = _number['Value']
            Name = _number['Key']
            print(f'Original: {Name}|> {Number}')
            change = input('| - |  Set :> ')
            print('\n')

            _number["Value"] = int(change)
    print('Done')
    with open(f"C:\\Users\\{user}\\AppData\\LocalLow\\Kinetic Games\\Phasmophobia\\saveData.txt", "w", encoding="utf-8") as f3:
        json.dump(data , f3)
        
    print(data)           
    sleep(4)
    print('Enabling Encrypter... DONT CLOSE')
    subprocess.call([file])

workStart()



