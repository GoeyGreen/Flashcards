import os
import PySimpleGUI as sg
from nltk.corpus import wordnet as wn
directory = os.getcwd()
print(directory)
fd = open(directory + '\\sites\\directory.txt','r')
fp = open(directory + '\\sites\\color.txt','r')
g = fp.read()
if g != '':
    sg.theme(g)
else:
    sg.theme('LightGray')
c = fd.read()
x = c.split('\n')

if x[0] != directory or int(x[1])>20:
    exit()
else:
    pass
print(x)
fc = open(directory + '\\sites\\directory.txt','w')
x[1] = int(x[1])+1
fc.write(os.getcwd())
fc.write('\n'+str(x[1]))
fc.close()
#Checks for a connection
import urllib.request
def connect(host='https://google.com/'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
#If there is a connection, it will download the necessary packages nltk
x = connect()
print(x)
if x == True:
    import nltk
    nltk.download('omw')
    nltk.download('omw-1.4')
    nltk.download('wordnet')
else: 
    pass
layout = [
[sg.Text('What do you want to name your flashcards ')],
[sg.Input(default_text = '',)],
[sg.Text('How many flashcards do you have? ')],
[sg.Input(default_text = '',)],
[sg.Text('Do you want to type it out or search the \ndefinition(May be inaccurate)?(type t or s)')],
[sg.Input(default_text = '',)],
[sg.Button(button_text = 'Submit'), sg.Button(button_text = 'EXIT'), sg.Button(button_text = 'Pick Color')]]
sentence = []
front = []
back = []
def typing( numofitems):
    global front, back, sentence
    layout = [
        [sg.Text('Words left: '), sg.Text(key = '//WL')],
        [sg.Text('Please write the front of the flashcard\n Write the word and tense(ex. hello (n.))')],
        [sg.Input(default_text = '',key='///W---')],
        [sg.Text('Please write the back of the flashcard\n Write the definition')],
        [sg.Input(default_text = '',key = '///D---')],
        [sg.Text('Please write the an example sentence for the word')],
        [sg.Input(default_text = '',key = '///S---')],
        [sg.Button(button_text = 'Submit'),sg.Button(button_text = 'EXIT')]]
    window = sg.Window(title = 'Flashcards',layout = layout, margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT )
    i = 0
    while i < numofitems:
        event, value = window.read()
        if event == 'Submit':
            window['//WL'].update(str(numofitems-i-1))
            value = list(value.values())
            flashcontentf = value[0]
            front.append(flashcontentf)
            flashcontentb = value[1]
            back.append(flashcontentb)
            flashcontents = value[2]
            sentence.append(flashcontents)
            window.find_element('///W---').Update('')
            window.find_element('///D---').Update('')
            window.find_element('///S---').Update('')
        if event == 'EXIT':
            break
        i+=1
def searching(numofitems):
    global front, back, sentence
    layout = [
        [sg.Text('Words left: '), sg.Text(key = '//WL')],
        [sg.Text('Please write the word you want to search')],
        [sg.Input(default_text = '',key = '///W---')],
        [sg.Button(button_text = 'Submit'),sg.Button(button_text = 'EXIT')]]
    i = 0
    window = sg.Window(title = 'Flashcards',layout = layout, margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, )       # start off with 1 window open
    while i < numofitems:             # Event Loop
        event, value = window.read()
        tmpdef = []
        word = value['///W---']
        y = 0
        #Gets all the definitions of a word
        for synset in list(wn.synsets(word)):
            y = str(y+1)
            tmpdef.append(synset)
            y = int(y)
        if event == 'Submit' and len(tmpdef)>1:
            which_def(tmpdef, word)
        #If there is one definition, it automatically adds the definition
        else:
            wordf = word +' ('+tmpdef[0].pos() + '.)'
            wordb = tmpdef[0].definition()
            if len(tmpdef[0].examples()) > 0:
                words = tmpdef[0].examples()[0]
                sentence.append(words)
            else:
                x = no_sentence()
                sentence.append(x)
            front.append(wordf)
            back.append(wordb)

        if event == 'Submit':
            window['//WL'].update(str(numofitems-i-1))
            window.find_element('///W---').Update('')
        if event == 'EXIT':
            break
        i+=1


def which_def(tmpdef,word):
    global front, back, sentence
    layout = [
        [sg.Text('Please type number of the definition you want: ')],
        [sg.Input(default_text = '',key = '///WD---')],
        [sg.Button(button_text = 'Submit'),sg.Button(button_text = 'EXIT')]]
    y = 0
    #Gets all the definitions of a word
    for synset in list(wn.synsets(word)):
            y = str(y+1)
            tmpdef.append(synset)
            layout.insert(int(y)-1,[sg.Text(y+'. '+synset.definition())])
            y = int(y)
    window2 = sg.Window(title = 'Sentence', margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, finalize = True ).Layout(layout)
    elements, values = window2.Read()
    if elements == 'Submit':
        whichdef = int(values['///WD---'])
        wordf = word +' ('+tmpdef[whichdef-1].pos() + '.)'
        wordb = tmpdef[whichdef-1].definition()
        if len(tmpdef[whichdef-1].examples()) > 0:
            if word in tmpdef[whichdef-1].examples():
                words = tmpdef[whichdef-1].examples()[0]
                sentence.append(words)
            else:
                x = no_sentence()
                sentence.append(x)
        else:
            x = no_sentence()
            sentence.append(x)
    if elements == 'EXIT' or elements == sg.WIN_CLOSED:
        window2.Close()
        exit()        

    front.append(wordf)
    back.append(wordb)
    window2.Close()

def no_sentence():
    layout = [
        [sg.Text('Sorry. This word does not have an example sentence. \nPlease type an example sentence')],
        [sg.Input(default_text = '',key = '///S---')],
        [sg.Button(button_text = 'Submit'),sg.Button(button_text = 'EXIT')]]
    window = sg.Window(title = 'Sentence',layout = layout, margins=(100, 50), right_click_menu  = sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT )
    event, value = window.read()
    if event == 'Submit':
        value = list(value.values())
        flashcontents = value[0]
        window.find_element('///S---').Update('')
        window.Close()
        return flashcontents

    elif event == 'EXIT' or event == sg.WIN_CLOSED:
        window.Close()
        exit()

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
            [sg.Button('Exit')]]
    
    window = sg.Window('Background Choice', layout)
    
    while True:  
        event, values = window.read()
        
        if event in (None, 'Exit'):
            break
        sg.theme(values['-LIST-'][0])
        sg.popup()
    color = values[0]   
    fp = open(directory+'\\sites\\color.txt','w')
    fp.write(color)
    fp.close()
    # Close
    window.close()


window = sg.Window(title="StartPage", layout = layout, margins=(100, 50))

#numofitems = int(input('How many flashcards do you have? '))
#whichone = input('Do you want to type it out or search the definition(May be inaccurate)?(type t or s)')
event, values = window.read()
if event == "Pick Color":
    color_choice()
if event == "EXIT" or event == sg.WIN_CLOSED:
    exit()
if event == 'Submit':
    groupname = values[0]
    numofitems = int(values[1])
    whichone = values[2]
    ff = open(directory + '\\sites\\' + groupname + 'front.txt','w')
    fb = open(directory + '\\sites\\'  + groupname + 'back.txt','w')
    fs = open(directory + '\\sites\\' + groupname + 'sentences.txt','w')
    if whichone == 't' or whichone == 'type':
        typing(numofitems)
    else:
        searching(numofitems)
    sg.popup('USE THE READING PROGRAM TO STUDY')
ff.write('\n'.join(front))
fb.write('\n'.join(back))
fs.write('\n'.join(sentence))
ff.close()
fb.close()
fs.close()
