#password_mngr.py

"""
This is a simple password keeper where you can save 
or view your login info for different accounts. 
You just type your master password to start, then 
choose if you wanna add new stuff or look at what 
you’ve saved. 
Now, you won't forget your passwords anymore!
"""

from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")


# def write_key():
#   key = Fernet.generate_key()
#   with open("key.key", "wb") as key_file:
#     key_file.write(key)

def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      data = (line.rstrip())
      user, passw = data.split("|")
      print("User:", user, "|| Password:", passw)

def add():
  name = input("Account Name: ")
  pwd = input("Password: ")

  with open('passwords.txt', 'a') as f:
    f.write(name + "|" + pwd + "\n") 


while True: 
    mode = input("Would you like to add a new password or view existing ones? (view, add), press q to quit: ").lower()
    if mode == "q":
      break
    elif mode == "view":
      view()
    elif mode == "add":
      add()
    else:
      print("Invalid mode.")