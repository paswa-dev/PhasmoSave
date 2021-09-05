from getpass import getpass
import urllib.request 
from colorama import init
init()
from colorama import Fore, Back, Style


import os
import sys

os.system('pip install requests')
os.system('pip install PySimpleGui')

import requests




area = os.getcwd()
print(area)
file_area = f'asset\\Save Crypter.exe'
path = os.path.join(area, file_area)
print(path)
file = path



relative = os.getcwd()
folder = 'asset'
new_relative = f'{relative}/' + folder

sys.path.insert(0, new_relative)

import asset.Finder
from asset.Finder import searchFile
from time import sleep
import subprocess
import getpass
user = getpass.getuser()


print('This message is only appearing for 4 seconds. Please make sure lastest verison of Python is installed!')
print('This doesnt mean u have the wrong version btw this is just a to notify people')
sleep(4)


url = 'https://phasmosave.com/saveData.txt'



fileName2 = 'SaveFile.es3'
fileName3 = 'SaveFile.es3.tmp.bak'

print('This may take some time. Please be patient')

searchFile('saveData.txt')

joinedFile = asset.Finder.filePATH
fileArea = os.path.dirname(asset.Finder.filePATH)

delete1 = os.path.join(fileArea, fileName2)
delete2 = os.path.join(fileArea, fileName3)

if os.path.exists(delete1):
    print('Found SaveFile.es3') 
    os.remove(delete1)
    print('Removed')
else:
    print('Skipping Step 2...')

if os.path.exists(delete2):
    print('Found SaveFile.es3.tmp') 
    os.remove(delete2)
    print('Removed')
else:
    print('Skipping Step 3...')

if os.path.exists(joinedFile):
    print('Found old saveData.txt') 
    os.remove(joinedFile)
    print('Removing old saveData')
else:
    print('Skipping Step 4...')

r = requests.get(url)
full = r.content

with open(joinedFile, 'wb') as f:
    f.write(full)

print(f'Wrote file into {fileArea}')
print('Checking file is there....')

if os.path.exists(joinedFile):
    print('Success!')
    print('You may now continue')
    print('')
    print('')
    print('')
    print(Fore.MAGENTA + 'Please press enter!')
    print('')
    print('')
    print('')
    print(Style.RESET_ALL)
    subprocess.call([file])
    os.system('python Edit.py')

else: 
    print('Failed?')

