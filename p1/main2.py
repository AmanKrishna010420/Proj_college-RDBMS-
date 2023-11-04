import mysql.connector as msq

# Database connection and cursor
cn = msq.connect(host='localhost', user='root', passwd='root', database='gym')
cr = cn.cursor()

# Function to donate a game
def donate_game():
    var = int(input("Enter the number of games to be added: "))
    for _ in range(var):
        v1 = int(input('Enter the gameID: '))
        v2 = input('Enter the game name: ')
        v3 = int(input('Enter the space it will acquire: '))
        v4 = int(input('Enter the RAM required: '))
        v5 = input('Graphic card required (Y/N): ')
        v6 = input('Enter the game genre: ')
        v7 = input('Enter the date of launch (yy-mm-dd): ')
        st = "INSERT INTO GMAC values('{}','{}','{}','{}','{}','{}','{}')".format(v1, v2, v3, v4, v5, v6, v7)
        cr.execute(st)
    cn.commit()

# Function to search for a game
def search_game():
    v1 = int(input('''Enter the aspect by which you want game suggestions:
1. Name
2. Genre
3. Compatibility\n'''))
    
    if v1 == 1:
        qr = input("Enter the name of the game: ")
        cmd = "SELECT * FROM GMAC WHERE GAME_NAME='{}'".format(qr)
    elif v1 == 2:
        qr = input("Enter genre of game: ")
        cmd = "SELECT * FROM GMAC WHERE GENRE='{}'".format(qr)
    elif v1 == 3:
        q1 = int(input("Enter the RAM required: "))
        q2 = input("Enter if graphic card is required (Y/N): ")
        q3 = int(input("Enter the storage required: "))
        cmd = "SELECT * FROM GMAC WHERE STORAGE<={} AND RAM<={} AND GRAPHIC_REQ='{}'".format(q3, q1, q2)

    cr.execute(cmd)
    result = cr.fetchall()
    print("[GAME_ID, GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH]")
    for row in result:
        print(row)

# Function to remove a game
def remove_game():
    var = input("Enter the game's name to be deleted: ")
    cmd = "DELETE FROM GMAC WHERE GAME_NAME='{}'".format(var)
    cr.execute(cmd)
    cn.commit()
    print("Game Deleted :(")

# Function to update a game
def update_game():
    cc = int(input('''
Enter what to update:
1. Name
2. Genre
3. Storage
4. RAM
5. Graphic Card
6. Date of launch\n'''))
    
    v1 = input("Enter the name of the game: ")
    if cc == 1:
        v2 = input("Enter the name to be updated: ")
        cmd = "UPDATE GMAC SET GAME_NAME='{}' WHERE GAME_NAME='{}'".format(v2, v1)
    elif cc == 2:
        v2 = input("Enter the genre to be updated: ")
        cmd = "UPDATE GMAC SET GENRE='{}' WHERE GAME_NAME='{}'".format(v2, v1)
    elif cc == 3:
        v2 = int(input("Enter the storage to be updated: "))
        cmd = "UPDATE GMAC SET STORAGE={} WHERE GAME_NAME='{}'".format(v2, v1)
    elif cc == 4:
        v2 = int(input("Enter the RAM to be updated: "))
        cmd = "UPDATE GMAC SET RAM={} WHERE GAME_NAME='{}'".format(v2, v1)
    elif cc == 5:
        v2 = input("Enter if GRAPHIC CARD is required (Y/N): ")
        cmd = "UPDATE GMAC SET GRAPHIC_REQ='{}' WHERE GAME_NAME='{}'".format(v2, v1)
    elif cc == 6:
        v2 = input("Enter the date to be updated: ")
        cmd = "UPDATE GMAC SET DATE_OF_LAUNCH='{}' WHERE GAME_NAME='{}'".format(v2, v1)

    cr.execute(cmd)
    cn.commit()

# Function to display all data
def show_data():
    exc = "SELECT * FROM GMAC"
    cr.execute(exc)
    dat = cr.fetchall()
    for row in dat:
        print(row)

while True:
    for _ in range(20):
        print("x-x", end=' ')
    print("                        ", "WELCOME TO GAMING ARCADE", "                          ")
    for _ in range(20):
        print("x-x", end=' ')
    
    chc = int(input(''' What is your choice
1. Donate a game
2. Search a game
3. Remove a game
4. Update a game
5. Show Data
6. Exit\n'''))
    
    if chc == 1:
        donate_game()
    elif chc == 2:
        search_game()
    elif chc == 3:
        remove_game()
    elif chc == 4:
        update_game()
    elif chc == 5:
        show_data()
    elif chc == 6:
        break
    else:
        print("Invalid choice. Please try again.")
