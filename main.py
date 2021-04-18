"""
Name: AstonOS
Date: April 7, 2021
Authour: Aston Cheng
Purpose: To imitate an operating system
"""

loading = 0
hardware = 0
software = 0
coding = 0

times_internet = 0
times_file = 0
times_calculator = 0
google_stuff_count = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
google_object = ["spines", "barrels", "noses", "legs", "eyes", "appendages", "arms", "strings", "swords"]
answered = False
done = False

first_name = input("What is your first name?\n: ")
last_name = input("What is your last name?\n: ")
while first_name == "" or last_name == "":
  print("You cannot input no name")
  first_name = (input("What is your first name?\n: "))
  last_name = input("What is your last name?\n: ")
print("\nWelcome: " + first_name + " " + last_name)
print("\n\n--------------------------AstonOS--------------------------")

while done == False:
  print("\n-----Applications-----\n-System\n-File\n-Internet Explorer\n-Calculator\n")
  selection = str.lower(input("Select an option: "))
  if selection == "system" or selection == "1":
    print("\n:Power Off\n:Task Manager\n:Change Name")
    selection = str.lower(input("Select an option: "))
    if selection == "power off":
      done == True
      break
    if selection == "setting" or selection == "settings":
      print("\nplaceholder\n")
    if selection == "task manager":
      print("\n------------------Task Manager------------------\nShows how many times an application has been opened.\n" + "Internet Explorer: " + str(times_internet) + "\nFiles: " + str(times_file) + "\nCalculator: " + str(times_calculator))
    if selection == "change name":
      first_name = (input("What is your first name?\n: "))
      last_name = input("What is your last name?\n: ")
      while first_name == "" or last_name == "":
        print("You cannot input no name")
        first_name = (input("What is your first name?\n: "))
        last_name = input("What is your last name?\n: ")
      print("Welcome: " + first_name + " " + last_name)
  if selection == "files" or selection == "file" or selection == "2":
    times_file = times_file + 1
    print("\nList of Files:\n\n-Downloads\n-Documents")
    selection = str.lower(input("Select an option: "))
    if selection == "downloads" or selection == "download":
      print("\nList of Downloads\n\n-doge.png")
      selection = str.lower(input("Select an option: "))
      if selection == "doge.png":
        print("\n░░░░░░░░░▄░░░░░░░░░░░░░░▄\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌\n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌\n▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀")
    if selection == "documents" or selection == "document":
      print("\nList of Documents\n\n-README.txt\n-essay template.docx")
      selection = input("Select an option: ")
      if selection == "README.txt" or selection == "README":
        print("\nWe're no strangers to love\nYou know the rules and so do I\nA full commitment's what I'm thinking of\nYou wouldn't get this from any other guy\nI just wanna tell you how I'm feeling\nGotta make you understand\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you")
      if selection == "essay template" or selection == "essay template.docx":
        print("\nAston Cheng\nApril 6/2020\nEric Fabroa\nICS2O\nLorum Ibsum\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
  if selection == "internet explorer" or selection == "Internet Explorer" or selection == "3":
    times_internet = times_internet + 1
    print("\n------------------Google Search------------------\n")
    google_search = str.lower(input(":"))
    if len(google_search)%2 == 0: 
      print("The " + str(google_search) + " has " + google_stuff_count[len(first_name)] + " " + google_object[len(last_name)] + ".")
    if not len(google_search)%2 == 0:
      if google_search[0] == "a" or  google_search[0] == "e" or google_search[0] == "o" or  google_search[0] == "i" or google_search[0] == "u":
        print("An " + str(google_search) + " has " + google_stuff_count[len(first_name)] + " " + google_object[(len(last_name))//2] + ".")
      else:
        print("A " + str(google_search) + " has " + google_stuff_count[len(first_name)] + " " + google_object[(len(last_name))//2] + ".")
  if selection == "calculator" or selection == "4":
    times_calculator = times_calculator + 1
    value_1 = float(input("Enter in the first value: "))
    notation = str.lower(input("Enter in an Algebraic Symbol: "))
    value_2 = float(input("Enter in the second value: "))
    if notation == "+" or notation == "plus":
      value_3 = value_1 + value_2
      print("The sum of " + str(value_1) + " added to " + str(value_2) + " is equal to " + str(value_3) + ".")
    if notation == "-" or notation == "minus":
      value_3 = value_1 - value_2
      print("The difference of " + str(value_1) + " subtracted by " + str(value_2) + " is equal to " + str(value_3) + ".")
    if notation == "*" or notation == "multiply" or notation == "multiplication":
      value_3 = value_1 * value_2
      print("The product of " + str(value_1) + " multiplied by " + str(value_2) + " is equal to " + str(value_3) + ".")
    if notation == "/" or notation == "divide":
      value_3 = value_1 / value_2
      print("The quotient of " + str(value_1) + "and " + str(value_2) + "is equal to " + str(value_3) + ".")
    if notation == "^" or notation == "square" or notation == "**":
      value_3 = int(value_1) ** int(value_2)
      print("The square of " + str(value_1) + " by " + str(value_2) + " is equal to " + str(value_3) + ".")
