from collections import namedtuple
import pyttsx3
import os
import random
import PySimpleGUI as sg
from sys import exit
directory = os.getcwd()
fp = open(directory + '\\sites\\color.txt','r')
g = fp.read()
if g != '':
    sg.theme(g)
else:
    sg.theme('LightGray')
engine = pyttsx3.init()
layout = [
[sg.Text('What Flashcards do you want to open')],
[sg.Input(default_text = '',)],
[sg.Text('How many times do you want to study')],
[sg.Input(default_text = '',)],
[sg.Button(button_text = 'Submit'), sg.Button(button_text = 'EXIT'), sg.Button(button_text = 'Pick Color'), sg.Button(button_text = 'Speed')]]

def speed():
    layout = [
    [sg.Text('What speed do you want to try(Higher = Faster)(Max 300)')],
    [sg.Input(default_text = '', key = 'ST')],
    [sg.Button(button_text = 'Submit'), sg.Button(button_text = 'Test Speed'), sg.Button(button_text = 'EXIT')]]
    engine.setProperty('rate',100)
    sp = open(directory + '\\sites\\speed.txt','r')
    n = sp.read()
    window = sg.Window(title = 'Set Speed',layout = layout, margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT )
    event, values = window.read()
    x = values['ST']
    if event == 'Test Speed':
        engine.setProperty("rate", x)
        engine.say('Speed Test')
        engine.runAndWait()
        window.find_element('ST').Update('')
        window.Close()
        speed()
    if event == 'Submit':
        spw = open(directory + '\\sites\\speed.txt','w')
        spw.write(str(x))
    window.Close()
    #Sets voice tone
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return n

def color_choice():
    global color
    sg.theme('Reddit')
    layout = [
            [sg.Text('Please Choose Your Favorite Color')],
            [sg.Listbox(values = sg.theme_list(),
                        size =(25, 15),
                        key ='-LIST-',
                        enable_events = True)],
            [sg.Text('Type in your favorite color')],
            [sg.Input('')],
            [sg.Button('Submit'),sg.Button('EXIT')]]
    
    window = sg.Window('Background Choice', layout)
    event, values = window.read()
    if event == '-LIST-':
        sg.theme(values['-LIST-'][0])
        sg.popup()
        window.Close()
        color_choice()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        color = values[0]   
        fp = open(directory+'\\sites\\color.txt','w')
        fp.write(color)
        fp.close()
    window.Close()
    return color





window = sg.Window(title="StartPage", layout = layout, margins=(100, 50))

#numofitems = int(input('How many flashcards do you have? '))
#whichone = input('Do you want to type it out or search the definition(May be inaccurate)?(type t or s)')
while True:
    event, values = window.read()
    if event == 'Speed':
        speed()
    if event == "Pick Color":
        color_choice()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        groupname = values[0]
        times = int(values[1])
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
        sp = open(directory + '\\sites\\speed.txt','r')
        speed1 = sp.read()
        engine.setProperty('rate', speed1)
        window.Close()
        layout = [
        [sg.Text('What is the word'), sg.Text('', key = 'C')],
        [sg.Input(default_text = '', key = 'W')],
        [sg.Text('What is the part of speech'), sg.Text('', key = '2C')],
        [sg.Input(default_text = '', key = 'POS')],
        [sg.Button(button_text = 'Submit'), sg.Button(button_text = 'EXIT'), sg.Button(button_text = 'Say Word'), sg.Button(button_text = 'Say All')]]
        ic = []
        window = sg.Window(title = 'Set Speed',layout = layout, margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT )
        for d in range(times):
            z = 0
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
                x = random.choice(range(len(voice)))
                while True:
                    event, values = window.Read()
                    if event == 'Say All':
                        engine.say(voice[x])
                        engine.say(reins2[x])
                        engine.say(voice[x])
                        engine.runAndWait()
                    if event == 'Say Word':
                        engine.say(voice[x])
                        engine.runAndWait()
                    word = values['W']
                    pos = values['POS']
                    if event  == 'Submit':
                        window.find_element('W').Update('')
                        window.find_element('POS').Update('')
                        if word in reinw[x] and len(word) > 1:
                            window.find_element('C').Update(' Correct ')
                        else:
                            window.find_element('C').Update(' Incorrect ')
                            if reinw[x] not in ic:
                                ic.append(reinw[x])        
                        if pos in reinw[x] and len(pos) >= 1:
                            window.find_element('2C').Update(' Correct ')
                        else:
                            window.find_element('2C').Update(' Incorrect ')
                            if reinw[x] not in ic:
                                ic.append(reinw[x])
                        sg.popup(reinw[x]+'\n'+wrinlst[x])
                        window.find_element('C').Update('')
                        window.find_element('2C').Update('')
                        wrinlst.remove(wrinlst[x])
                        reinw.remove(reinw[x])
                        voice.remove(voice[x])
                        reins2.remove(reins2[x])
                        break
                    if event == "EXIT" or event == sg.WIN_CLOSED:
                        exit()
        sg.popup('Study these words: ',' '.join(ic))
        window.Close()




