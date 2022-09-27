#This is the Studying part of the Flashcards Program
#It will read files containing example sentences, definitions, and words
#Uses pyttsx3 for text to speech software
input('Press Enter to Continue')
import pyttsx3
import os
import sys
import random
#Get all directories and read them
directory = os.path.dirname(os.path.abspath (__file__))
groupname = input('What file do you want to open? ')
ff = open(directory + '\\sites\\' + groupname + 'front.txt','r')
fb = open(directory + '\\sites\\'  + groupname + 'back.txt','r')
fs = open(directory + '\\sites\\' + groupname + 'sentences.txt','r')
reins = fs.read()
reins3 = reins.split('\n')
rein = ff.read()
reinw2 = rein.split('\n')
length = len(reinw2)
wrin = fb.read()
wrinlst2 = wrin.split('\n')
#incorrect words
ic = []
d = 1
z = 0
times = int(input('How many times do you want to study: '))
#pyttsx3 setup
#Starts the engine and allows for speed congifuration
#Speed configuration stored in speed.txt
#Once set, the speed will not be changed
engine = pyttsx3.init()
engine.setProperty('rate',100)
sp = open(directory + '\\sites\\speed.txt','r')
c = sp.read()
if c == '0':
    while z == 0:
        x = int(input('Set your preferred speech speed '))
        engine.setProperty("rate", x)
        engine.say('Speed Test')
        engine.runAndWait()
        ok = input('Is this speed good (y or n)')
        ok = ok.lower()
        if ok == 'y' or ok == 'yes':
            spw = open(directory + '\\sites\\speed.txt','w')
            spw.write(str(x))
            z += 1
        else:
            pass
else:
    engine.setProperty('rate', int(c))
#Sets voice tone
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Running
while d <= times:
    reinw = reinw2[:]   
    wrinlst = wrinlst2[:]
    voice2 = reinw[:]
    reins2 = reins3[:]
    voice = []
    #Removes the Part of Speech from the word
    for c in voice2:
        c = c.split(' ')
        for v in c:
            if '(' and ')' in v:
                c.remove(v)
                voice.append(''.join(c))
            else:
                pass
    #The engine will say the word, example sentence, and word
    #It will then prompt the user to give the spelling and part of speech
    for i in range(length):
        x = random.choice(range(len(reinw)))
        engine.say(voice[x])
        engine.say(reins2[x])
        engine.say(voice[x])
        engine.runAndWait()
        word = input('What is the word ')
        if word in reinw[x] and len(word) > 1:
            print('Correct')
        else:
            print('incorrect')
            ic.append(reinw[x])
        pos = input('What is the part of speech(abbreviation)')
        if pos in reinw[x] and len(pos) >= 1:
            print('Correct')
        else:
            print('incorrect')
        print(reinw[x])
        print(wrinlst[x])
        wrinlst.remove(wrinlst[x])
        reinw.remove(reinw[x])
        voice.remove(voice[x])
        reins2.remove(reins2[x])
    print('Study these words:',' '.join(ic))
    d+=1

input('Press Enter to Exit')
