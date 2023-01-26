import time
import sys
import termcolor

print("               ___________")
print("             _| _________ |_")
print("           _| _|         |_ |_")
print("         _| _|              |_ |_")
print("       _|  _|                 |_ |_")
print("      |  |______________________|  |")
print("      |                            |")
print("      |           _____            |")
print("      |          |     |           |")
print("      |          |_   _|           |")
print("      |           |   |            |")
print("      |           |   |            |")
print("      |           |   |            |")
print("      |           |_ _|            |")
print("      |             -              |")
print("      |                            |")
print("      ------------------------------")

print("PASSWORD STOARGE")
usercorrect = False
passwordcorrect = False
users = [[],[]]

f = open("users.txt", "r")
for line in f:
  temporary = line.split(", ")
  temporary[1] = temporary[1].rstrip('\n')
  users[0].append(temporary[0])
  users[1].append(temporary[1])

print("")
print("")
currentuser = ""
while usercorrect == False or passwordcorrect == False:
  time.sleep(1)
  username = input("[*] USERNAME: ")
  time.sleep(1)
  for i in range(len(users[0])):
    if username == users[0][i]:
      usercorrect = True
      currentuser = users[0][i]
      password = input("[*] PASSWORD: ")
      if password == users[1][i]:
        passwordcorrect = True
        break
  if usercorrect == False:
    termcolor.cprint("User does not exist", "red")
  elif usercorrect == True and passwordcorrect == False:
    termcolor.cprint("Incorrect Password", "red")

animation = ["Loading Profile... [■□□□□□□□□□]","Loading Profile... [■■□□□□□□□□]", "Loading Profile... [■■■□□□□□□□]", "Loading Profile... [■■■■□□□□□□]", "Loading Profile... [■■■■■□□□□□]", "Loading Profile... [■■■■■■□□□□]", "Loading Profile... [■■■■■■■□□□]", "Loading Profile... [■■■■■■■■□□]", "Loading Profile... [■■■■■■■■■□]", "Loading Profile... [■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.5)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
t = time.localtime()
hour = time.strftime("%H", t)
if int(hour) > 24:
  extra = int(hour) - 24
  hour = extra
else:
  hour = int(hour) + 16
minute = time.strftime(":%M:", t)
second = time.strftime("%S", t)
termcolor.cprint("Logged in at: [" + str(hour) + minute + second + "]", "green")


cipherKey = input("[*] KEY: ")
cipherKey = int(cipherKey)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwords = []

def findlocation(element):
  element = element.upper()
  i=0
  for letter in letters:
    #print(element +  " == " + letter)
    if element == letter:
      return i
    i = i+1
    
def decode(string, key):
  decoded = ""
  for letter in string:
    if letter.isalpha():
      if letter.islower():
        postion = findlocation(letter)
        postion = postion - key
        decoded = decoded + letters[postion].lower()
      else:
        postion = findlocation(letter)
        postion = postion - key
        decoded = decoded + letters[postion]
    else:
      decoded = decoded + letter  
  return decoded
def encode(string, key):
  encoded = ""
  for letter in string:
    if letter.isalpha():
      if letter.islower():
        postion = findlocation(letter)
        postion = postion + key
        encoded = encoded + letters[postion].lower()
      else:
        postion = findlocation(letter)
        postion = postion + key
        encoded = encoded + letters[postion]
    else:
      encoded = encoded + letter
  return encoded
  
f = open("passwords.txt", "r")
for line in f:
  temporary = line.split(":")
  decoded = decode(temporary[0], cipherKey)
  if decoded == currentuser:
    print("Username: " + decoded)
    temporary[1] = temporary[1].split(", ")
    for element in temporary[1]:
      passwords.append(decode(element, cipherKey))
f.close()
j = 1
print("Passwords:")
for password in passwords:
  print(str(j) + ":" + password)
  j = j+1

loggedIn = True
while loggedIn == True:
  option = input("[*] Options (1:Change key, 2:add password, 3:log out): ")  
  if int(option) == 1:
    newKey = input("Enter New Key (under 5): ")
    newKey = int(newKey) 
    if newKey > 5:
      newKey = input("Enter New Key (under 5): ")
    else:
      tempFile = []
      newline = encode(currentuser, newKey) + ":"
      g = 1
      for password in passwords:
        newline = newline + encode(password, newKey)
        if g != len(passwords):
          newline = newline + ", "
        g = g + 1
      count = len(open("passwords.txt").readlines())
      f = open("passwords.txt", "r")
      s=1
      for line in f:
        temporary = line.split(":")
        decoded = decode(temporary[0], cipherKey)
        if decoded == currentuser:
          tempFile.append(newline)
          tempFile.append("\n")
        else:
          tempFile.append(line)
          if s != count:
            tempFile.append("\n")
        s=s+1
      f.close()
      with open("passwords.txt", "w") as file:
        for i in range(len(tempFile)):
          file.write(tempFile[i])
      cipherKey = newKey
  elif int(option) == 2:
    count = len(open("passwords.txt").readlines())
    print(count)
    tempFile = []
    newPassword = input("[*] Enter a new password: ")
    newPassword = encode(newPassword, cipherKey)
    print(newPassword)
    f = open("passwords.txt", "r")
    s = 1
    for line in f:
      temporary = line.split(":")
      decoded = decode(temporary[0], cipherKey)
      if decoded == currentuser:
        line = line.rstrip('\n')
        newline = line + ", " + newPassword
        tempFile.append(newline)
        tempFile.append("\n")
      else:
        tempFile.append(line)
        if s != count:
          tempFile.append("\n")
      s=s+1
    f.close()
    print(newline)
    print(tempFile)
    with open("passwords.txt", "w") as file:
      for i in range(len(tempFile)):
        file.write(tempFile[i])
    
  elif int(option) == 3:
    break
