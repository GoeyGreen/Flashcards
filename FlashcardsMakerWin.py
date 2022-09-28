#This is the creation part of the Flashcards program
#Run this to make your flashcards
#Uses wordnet and omw from nltk.corpus
input('Press Enter to Continue')
import os
#Checks if the directory is the same as the one created by the RunThisFirst program
#If the directory is different, it will not run
directory = os.getcwd()

fd = open(directory + '\\sites\\directory.txt','r')
c = fd.read()
x = c.split('\n')
v =  x
if x[0] != directory or int(x[1])>20:
    exit()
else:
    pass
fc = open(directory + '\\sites\\directory.txt','w')
x[1] = int(x[1])+1
fc.write(os.getcwd())
fc.write('\n'+str(x[1]))

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
#Creates files that store the word, POS, definition, and example sentences
groupname = input('What do you want to name your flashcards ')
ff = open(directory + '\\sites\\' + groupname + 'front.txt','w')
fb = open(directory + '\\sites\\'  + groupname + 'back.txt','w')
fs = open(directory + '\\sites\\' + groupname + 'sentences.txt','w')

sentence = []
front = []
back = []
numofitems = int(input('How many flashcards do you have? '))
whichone = input('Do you want to type it out or search the definition(May be inaccurate)?(type t or s)')
whichone = whichone.lower()
#Gives user the ability to either type the words, sentences, and definition or to use wordnet
if whichone == 't':
    for i in range(numofitems):
        flashcontentf = input('Please write the contents of the flashcard(front) ')
        confirm = input('Is this correct:'+ flashcontentf+'(y or n)')
        if confirm == 'y':
            front.append(flashcontentf)
        else:
            flashcontentb = input('Please write the contents of the flashcard(front) ')
            front.append(flashcontentf)
        flashcontentb = input('Please write the contents of the flashcard(back) ')
        confirm = input('Is this correct:'+ flashcontentb+'(y or n)')
        if confirm == 'y':
            back.append(flashcontentb)
        else:
            flashcontentb = input('Please write the contents of the flashcard(back) ')
            back.append(flashcontentb)
        flashcontents = input('Please write the contents of the flashcard(sentence) ')
        confirm = input('Is this correct:'+ flashcontents+'(y or n)')
        if confirm == 'y':
            sentence.append(flashcontents)
        else:
            flashcontents = input('Please write the contents of the flashcard(sentence) ')
            sentence.append(flashcontents)
else:
    for i in range(numofitems):
        tmpdef = []
        word = input('what word are you looking for ')
        from nltk.corpus import wordnet as wn
        y = 0
        #Gets all the definitions of a word
        for synset in list(wn.synsets(word)):
            y = str(y+1)
            tmpdef.append(synset)
            print(y+'. '+synset.definition())
            y = int(y)
        #If there are multiple definitions, it will ask the user which definition they want
        if len(tmpdef) > 1:
            whichdef = int(input('Which definition do you want?(Type the number) '))
            wordf = word +' ('+tmpdef[whichdef-1].pos() + '.)'
            wordb = tmpdef[whichdef-1].definition()
            if len(tmpdef[whichdef-1].examples()) > 0:
                words = tmpdef[whichdef-1].examples()[0]
                sentence.append(words)
            else:
                print('Sorry, this word doesn\'t have an example sentence')
                flashcontents = input('Please write the contents of the flashcard(sentence) ')
                confirm = input('Is this correct:'+ flashcontents+'(y or n)')
                if confirm == 'y':
                    sentence.append(flashcontents)
                else:
                    flashcontents = input('Please write the contents of the flashcard(sentence) ')
                    sentence.append(flashcontents)
            front.append(wordf)
            back.append(wordb)
        #If there is one definition, it automatically adds the definition
        else:
            wordf = word +' ('+tmpdef[0].pos() + '.)'
            wordb = tmpdef[0].definition()
            if len(tmpdef[0].examples()) > 0:
                words = tmpdef[0].examples()[0]
                sentence.append(words)
            else:
                print('Sorry, this word doesn\'t have an example sentence')
                flashcontents = input('Please write the contents of the flashcard(sentence) ')
                confirm = input('Is this correct:'+ flashcontents+'(y or n)')
                if confirm == 'y':
                    sentence.append(flashcontents)
                else:
                    flashcontents = input('Please write the contents of the flashcard(sentence) ')
                    sentence.append(flashcontents)
            front.append(wordf)
            back.append(wordb)


print('RUN THE READING PROGRAM TO USE.')
ff.write('\n'.join(front))
fb.write('\n'.join(back))
fs.write('\n'.join(sentence))
input('Press Enter to Exit')
