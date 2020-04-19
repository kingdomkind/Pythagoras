import sys
import webbrowser
import pyttsx3

engine = pyttsx3.init()




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

def listOfDetails(contactList):
    listOfDetails = ""
    for key, value in contactList.items():
        listofDetails += str(key) + ": " + str(value) + "\n"

def help():
    print ("Here are the list of commands")
    engine.say("Here are the list of commands")
    engine.runAndWait()
    print ("Help - Gives a list of commands")
    print ("Search (words) - This command allows you to search a word on a webbrowser")
    print ("create contact - This command allows you to create a contact")
    print ("credits - Gives a list of credits")

def credits():
    print ("This was made by Arsalan and Umar. Umar provided massive help towards the project, it would have not been possible without him.")


print ("Hello, i am Pythagoras Basic, a genral-purpose bot.")
engine.say("Hello, I am Pythagoras Basic, a general-purpose bot.")
engine.runAndWait()

def mainstuff():
    print("What shall i do? (type help for commands)")
    engine.say("What shall i do?")
    engine.runAndWait()
    keyword = input("")

    def restart():
        restart = input("Do you wish to restart the program?")
        if restart in ["yes", "Yes"]:
            mainstuff()
        else:
            sys.exit(0)

    if keyword in ("contact list", "show contacts", "contacts"):
        listOfDetails(contactList())
        restart()

    if keyword in ("create contact"):    
        contactList = contactcreator()
        print ("You have created a contact")
        engine.say("You have created a contact")
        engine.runAndWait()
        for key, value in contactList.items():
            print(str(key) + ": " + str(value))
        restart()

    if keyword.startswith("search"):
        urlTerm = createUrlTerm(keyword, "+")
        noTerm = createUrlTerm(keyword, " ")
        url = ("https://www.google.com/search?source=&q={}&oq={}").format(urlTerm, urlTerm)
        webbrowser.open(url)
        print ("Here are the search results for: " + noTerm)
        engine.say("Here are the search results for " + noTerm)
        engine.runAndWait()
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






