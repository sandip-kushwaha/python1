# logine authentication using conditional statement. Assume you have a predefined username and password.
# write a program that prompts the user to enter a username and password and checks whether they match.
#provide appropriate messege for the following cases.
# Both username and password is correct.
# Both username correct but  password is incorrect.
# Username is incorrect.

predefined_username = 'sandip'
predefined_password = 'sandip123'
username = input("Enter your username: ")
password = input("Enter your password: ")

if (predefined_username == username) and (predefined_password == password):
    print("Both username and password is correct.\n Welcome login was successful.")
elif (predefined_username == username) and (predefined_password != password):
    print("Username is correct but password is incorrect.")    

else: 
    print(" username is incorrect.")

