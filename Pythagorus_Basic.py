import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
from tkinter import *
import time
import os

#This is a project, (originally) created by kingdomkind and dapawa on github. You can modify the code, and ask us to make it publicly avaivable on our github https://github.com/kingdomkind/Pythagoras
#You cannot upload it without our consent but you can do anything for personal use. Enjoy

textcheck = ""
keyword = ""
r = sr.Recognizer()
engine = pyttsx3.init()
contacts = {}
root = Tk()

#The """ code below is to make a window appear, which displays a gif. However, to make this work you would need to rewrite at least half of the code to make it asynchronous, which is no small feat.
#I have left it here if you want to make it work. To change the gif, just replace the direcory. If you do make it asynchronous and wish for us to post it on the github we will gladly do so. Whoever
#contributes will have their name in the list of credits (to make the code for the gif play just simply remove the """ as everything else has already been imported).
"""
root.title("Pythagoras")

frames = [PhotoImage(file='C:\\Users\\sabha\\source\\repos\\Window\\pythag.gif',format = 'gif -index %i' %(i)) for i in range(80)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == len(frames):
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
"""

#This is the speechlist. These are the words that trigger py's speech recognition
speechlist = ["pie", "pi", "py", "pythag", "pythug", "pythagoras", "pythugarus", "pai", "paypal", "bye", "ie", "rip", "if", "i", "reply", "hi"]

#This function takes the keyword from speechrec() and applies it to the commands
def bigbrain():
    commandcontactlist()
    commmandcreatecontact()
    commandsearch()
    simplekeywordcontact()
    simplekeywordhelp()
    simplekeywordcredit()

#This is the function for speech recognition. What you say, it turns it into a keyword, which then bigbrain() handles
def speechrec():
    #print ("Listening")
    global keyword
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        textcheck = text.lower().split()
        print("I'm always here")
        check =  any(item in speechlist for item in textcheck)
        if check is True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                keyword = text
                print (keyword)
                bigbrain()
        else:
            speechrec()
    except Exception as e:
        #print("Let's try again")
        print(e)
        speechrec()

#This function is the greeting you get when the program restarts and when it restarts
def greeting2():
    global contacts
    print("\n""What shall i do? (say hey py, then help for a list of commands)")
    engine.say("What shall i do?")
    engine.runAndWait()
    speechrec()
    #keyword = input("")

#This splits search off the words you're searching
def createUrlTerm(keyword, splitter):
    searchTerm = keyword.split()[1::1]
    urlTerm = ""
    for i in searchTerm:
        urlTerm += i + str(splitter)
    return urlTerm

#This creates your contact by asking you to input the details
def contactcreator():
    name = input("Please write the name: ")
    number = input("Please write the phone number: ")
    email = input("Please write the email: ")
    return {"name": name, "number": number, "email": email}

#This recalls your contact, which you created
def listOfDetails():
    global contacts
    detailList = ""
    for name, dictionary in contacts.items():
        for key, value in dictionary.items():
            detailList += str(key) + ": " + str(value) + "\n"
        detailList += "\n"
    print(detailList)

#This simple function prints out the list of commnds
def help():
    print ("Here are the list of commands")
    engine.say("Here are the list of commands")
    engine.runAndWait()
    print ("Help - Gives a list of commands")
    print ("Search (words) - This command allows you to search a word on a webbrowser")
    print ("create contact - This command allows you to create a contact")
    print ("contact list - This command show contacts")
    print ("credits - Gives a list of credits")

#This prints out the credits
def credits():
    print ("This was made by kingdomkind and DaPawa")

#This is the function to make the program continue after one command
def restart():
    restart = ("yes")
    if restart in ["yes", "Yes"]:
        mainstuff()
    else:
        sys.exit(0)

#This function calls listOfDetails if the words are in the requirements
def commandcontactlist():
    if keyword in ("contact list", "show contacts", "contacts"):
        listOfDetails()
        restart()

#This calls the previous contact maker and prints it if the word is create contact
def commmandcreatecontact():
    if keyword in ("create contact"):

        newContact = contactcreator()
        contacts[newContact["name"]] = newContact
        print ("You have created a contact")
        engine.say("You have created a contact")
        engine.runAndWait()
        for key, value in newContact.items():
            print(str(key) + ": " + str(value))
        restart()

#This is the search function. It opens your webbrowser with the query in it
def commandsearch():
    if keyword.startswith("search"):
        urlTerm = createUrlTerm(keyword, "+")
        noTerm = createUrlTerm(keyword, " ")
        url = ("https://www.google.com/search?source=&q={}&oq={}").format(urlTerm, urlTerm)
        webbrowser.open(url)
        print ("Here are the search results for: " + noTerm)
        restart()

#This calls list of details
def simplekeywordcontact():
    if keyword in ("contact"):
        listOfDetails()
        restart()

#this calls the help function if the word is help
def simplekeywordhelp():
    if keyword in ("help"):
        help()
        restart()

#This calls the credits function if the keyword is credit
def simplekeywordcredit():
    if keyword in ("credits"):
        credits()
        restart()

#This is the first greeting you see when booting up the program. It is not repeated
print ("Hello, i am Pythagoras Basic, a general-purpose bot.")
engine.say("Hello, i am Pythagoras Basic, a general-purpose bot.")
engine.runAndWait

#This calls all the functions and runs the program
def mainstuff():
    greeting2()
    restart()
    commandcontactlist()
    commmandcreatecontact()
    commandsearch()
    simplekeywordcontact()
    simplekeywordhelp()
    simplekeywordcredit()

mainstuff()

