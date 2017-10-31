userDetails = [["bob","123"],["sarah","234"],["nigel","567"]]

def login():
    global userDetails
    username = input("please enter your username: \n").lower()
    password = input("please enter your password: \n")

    match = False
    for user in userDetails:
        if username == user[0] and password == user[1]:
            match = True
            break

    if match == True:
        print("Access Granted")
    else:
        print("Access Denied")
        
def signup():
    global userDetails
    newUsername = input("please enter your desired username: \n").lower()

    #checks to see if username already exists
    userExists = False
    for user in userDetails:
        if user[0] == newUsername:
            userExists = True
    #continues to add user if username is available        
    if userExists == False:
        newPassword = input("please enter your new password: \n")
        newUser = [newUsername, newPassword]
        userDetails.append(newUser)
        print("User added successfully")
        menu()
    else:
        #prints a message and reruns signup if username exists
        print("I am sorry but that username has already been taken. \n Please try again.")
        signup()

def menu():
    menuSelection = input("Please choose a menu option below: \n 1. Login \n 2. Signup \n")

    if menuSelection == "1":
        login()
    elif menuSelection == "2":
        signup()
    else:
        print("This is not a valid menu number.")
        menu()

#main code starts here

menu()
