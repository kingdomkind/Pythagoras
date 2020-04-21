import sys
import webbrowser
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
engine = pyttsx3.init()
contacts = {}

def speechrec():
    with sr.Microphone() as source:
        audio = r.listen(source)
        print("listening")
    try:
        print ("you're nearly here")
        text = r.recognize_google(audio)
        print("You're here")
        if text in ["pie", "pi", "py", "pythag", "pythug", "pythagoras", "pythugarus"]:
            with sr.Microphone() as source:
                audio = r.listen(source)
                print ("I can hear you")
            try:
                text = r.recognize_google(audio)
                #text = keyword
                print ("Right away")
            except:
                pass
        speechrec()
    except:
        print("Let's try again")
        speechrec()
        
        

def createUrlTerm(keyword, splitter):
    searchTerm = keyword.split()[1::1]
    urlTerm = ""
    for i in searchTerm:
        urlTerm += i + str(splitter)
    return urlTerm

def contactcreator():
    name = input("Please write the name: ")
    number = input("Please write the phone number: ")
    email = input("Please write the email: ")
    return {"name": name, "number": number, "email": email}

def listOfDetails():
    global contacts
    detailList = ""
    for name, dictionary in contacts.items():
        for key, value in dictionary.items():
            detailList += str(key) + ": " + str(value) + "\n"
        detailList += "\n"
    print(detailList)

def help():
    print ("Here are the list of commands")
    engine.say("Here are the list of commands")
    engine.runAndWait()
    print ("Help - Gives a list of commands")
    print ("Search (words) - This command allows you to search a word on a webbrowser")
    print ("create contact - This command allows you to create a contact")
    print ("contact list - This command show contacts")
    print ("credits - Gives a list of credits")

def credits():
    print ("This was made by Arsalan and Umar. Umar provided massive help towards the project, it would have not been possible without him.")


print ("Hello, i am Pythagoras Basic, a general-purpose bot.")
engine.say("Hello, i am Pythagoras Basic, a general-purpose bot.")
engine.runAndWait

def mainstuff():
    global contacts
    print("\n""What shall i do? (type help for commands)")
    engine.say("What shall i do?")
    engine.runAndWait()
    speechrec()
    keyword = input("")

    def restart():
        restart = ("yes")
        if restart in ["yes", "Yes"]:
            mainstuff()
        else:
            sys.exit(0)

    if keyword in ("contact list", "show contacts", "contacts"):
        listOfDetails()
        restart()

    if keyword in ("create contact"):
        newContact = contactcreator()
        contacts[newContact["name"]] = newContact
        print ("You have created a contact")
        engine.say("You have created a contact")
        engine.runAndWait()
        for key, value in newContact.items():
            print(str(key) + ": " + str(value))
        restart()

    if keyword.startswith("search"):
        urlTerm = createUrlTerm(keyword, "+")
        noTerm = createUrlTerm(keyword, " ")
        url = ("https://www.google.com/search?source=&q={}&oq={}").format(urlTerm, urlTerm)
        webbrowser.open(url)
        print ("Here are the search results for: " + noTerm)
        restart()

    if keyword in ("contact"):
        listOfDetails()
        restart()
    

    if keyword in ("help"):
        help()
        restart()

    if keyword in ("credits"):
        credits()
        restart()

mainstuff()







