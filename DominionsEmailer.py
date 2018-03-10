import pickle
import sys
import glob
from emailFunction import setupEmail


#function to save user data
def save_data(fileName, data):   
    #if try has an error, then the except block is written.
    try:
        print ("Saving...")
        pickle.dump(data, open(fileName, "wb") )
        print ("Saved!")
            
    except:
        print ("Oh No! Unable To Save Data.")
            
#function to load data
def load_data(fileName):
    try: 
        data = pickle.load( open( fileName, "rb" ) )
        print ("Loaded Data Correctly!")
        return data
            
    except:
        print ("Unable to Load data! Doing First Time Setup.")    
        to = input("Who is the recipient? enter their email. ")
        sender = input("Your Email address? ")
        password = input("Enter Your Password. ")
        userDirect = input("Enter The User Directory, Go into the game, User preferences, and open user dierectory and copy that. ")
        userDirect = userDirect + "\\savedgames"
        userInfo = [to, sender, password, userDirect]
        
        save_data(fileName, userInfo)
        return userInfo
    
def load_direct(fileName):
    try: 
        data = pickle.load( open( fileName, "rb" ) )
        print ("Loaded Data Correctly!")
        return data

    except:
        print("Want to start a new game, huh?")
        gameName = input("Enter the game name. EXACTLY like it is in the game. (include '_'s) ")
        save_data(fileName, gameName)
        return gameName
    
                
def main():
    print("Welcome, to the DomV emailerrr")
    userInfo = load_data("user_data")
    
    to = userInfo[0]
    sender = userInfo[1]
    password = userInfo[2]
    userDirect = userInfo[3]
    userDirect = userDirect + "\\"
    
    gameName = load_direct("game_data")
    subject = gameName
    
    attached_file = userDirect + gameName + "\*.2h"
    #search for .2h file, there will only be one in the folder so
    for name in glob.glob(attached_file):
        attached_file = name

    save_data(gameName, attached_file)
    setupEmail(to, sender, subject, attached_file)

if __name__ == '__main__':
        main()
