#This is the registering part of the Flashcards program
#This program checks for a license code
import os
import sys
directory = os.path.dirname(os.path.abspath (__file__))
#license code
license = 'afhui3y7123u8aef127389qweiuhfdsiuh284huidasfhui'
#Checks the file for the license code
f = open(directory+'\\sites\\license1.txt','r')
c = f.read()
c = c.split('n')
#Removes originial zip file used to send the code
file_path = directory+'\\programtest.zip'
if os.path.isfile(file_path):
  os.remove(file_path)
else:
  pass
#Matches license
if license == c[0]:
    print('Welcome. We are setting up.')
    #Creates directory.txt which stores user directory and use times
    x = open(directory+'\\sites\\license1.txt','w')
    d = open(directory+'\\sites\\directory.txt','w')
    d.write(directory)
    d.write('\n0')
    print('Setup Complete')
else:
    #if the license is invalid, the program will exit
    print('INVALID LICENSE')
    input('Press Enter to Exit')
    exit()
