password = input("Enter password")

while (password != "password"):
    password = input("password")
    
print('''
      1. add member
      2. remove member
      3. search member
      ''')

choise = input("select choise")

if (choise == 1):
    print('''
          1. new member
          2. new coach
          ''')
    category = input("select category")
    if (category == 1):
        new_id = input("new id")
        new_name = input("new name")
    elif (category == 2):
        new_id = input("new id")
        new_name = input("new name")
elif (choise == 2):
    print("remove member")
elif (choise == 3):
    print("search member")