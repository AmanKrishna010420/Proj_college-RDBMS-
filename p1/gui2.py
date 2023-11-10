import mysql.connector as msq
import csv as c
import tkinter as tk
from tkinter import ttk, messagebox

# Establish a database connection
cn = msq.connect(host="localhost", user="root", passwd="root", database="gym")
cr = cn.cursor()

# Create a Tkinter window
root = tk.Tk()
root.title("Gaming Arcade Management")

# Open the CSV file for reading and writing
fl = open("data.csv", "a+", newline="")
rit = c.writer(fl)
dat = list(c.reader(fl))

# Create a Treeview widget to display the data in a tabular form
tree = ttk.Treeview(root, columns=("GameID", "GameName", "Storage", "RAM", "GraphicReq", "Genre", "DateOfLaunch"))
tree.heading("#1", text="Game ID")
tree.heading("#2", text="Game Name")
tree.heading("#3", text="Storage")
tree.heading("#4", text="RAM")
tree.heading("#5", text="Graphic Req")
tree.heading("#6", text="Genre")
tree.heading("#7", text="Date Of Launch")
tree.pack()

# Function to display data
def display_data():
    for record in tree.get_children():
        tree.delete(record)
    cmd = "SELECT * FROM GMAC"
    cr.execute(cmd)
    data = cr.fetchall()
    for row in data:
        tree.insert("", "end", values=row)

# Function to search for a game
def search_game():
    # Create a new window for the search form
    search_window = tk.Toplevel(root)
    search_window.title("Search for a Game")

    # Create a label and entry for the game name
    search_label = tk.Label(search_window, text="Enter Game Name:")
    search_entry = tk.Entry(search_window)

    # Function to execute the search
    def execute_search():
        search_text = search_entry.get()
        cmd = "SELECT * FROM GMAC WHERE GAME_NAME = %s"
        cr.execute(cmd, (search_text,))
        search_result = cr.fetchall()
        display_search_result(search_result)

    search_button = tk.Button(search_window, text="Search", command=execute_search)
    search_label.pack()
    search_entry.pack()
    search_button.pack()

# Function to display the search results
def display_search_result(results):
    for record in tree.get_children():
        tree.delete(record)
    for row in results:
        tree.insert("", "end", values=row)

# Function to remove a game
def remove_game():
    # Create a new window for the remove form
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove a Game")

    # Create a label and entry for the game name
    remove_label = tk.Label(remove_window, text="Enter Game Name:")
    remove_entry = tk.Entry(remove_window)

    # Function to execute the removal
    def execute_removal():
        remove_text = remove_entry.get()
        cmd = "DELETE FROM GMAC WHERE GAME_NAME = %s"
        cr.execute(cmd, (remove_text,))
        cn.commit()

        # Filter out the game to be deleted from the list
        global dat
        dat = [row for row in dat if row[1] != remove_text]

        # Write the updated data to the CSV file
        with open("data.csv", "w", newline="") as new_file:
            writer = c.writer(new_file)
            writer.writerows(dat)

        messagebox.showinfo("Success", "Game removed successfully!")
        display_data()
        remove_window.destroy()

    remove_button = tk.Button(remove_window, text="Remove", command=execute_removal)
    remove_label.pack()
    remove_entry.pack()
    remove_button.pack()
def donate_game():
    game_name = entry_game_name.get()
    storage = entry_storage.get()
    ram = entry_ram.get()
    graphic_req = entry_graphic_req.get()
    genre = entry_genre.get()
    date_of_launch = entry_date_of_launch.get()
    
# Function to update a game
def update_game():
    # Create a new window for the update form
    update_window = tk.Toplevel(root)
    update_window.title("Update a Game")

    # Create a label and entry for the game name
    update_label = tk.Label(update_window, text="Enter Game Name:")
    update_entry = tk.Entry(update_window)

    # Function to execute the update
    def execute_update():
        update_text = update_entry.get()
        cmd = "SELECT * FROM GMAC WHERE GAME_NAME = %s"
        cr.execute(cmd, (update_text,))
        update_result = cr.fetchall()

        if not update_result:
            messagebox.showerror("Error", "Game not found!")
        else:
            update_game_details(update_result)

    update_button = tk.Button(update_window, text="Update", command=execute_update)
    update_label.pack()
    update_entry.pack()
    update_button.pack()

# Function to update the game details
def update_game_details(game_details):
    update_game_window = tk.Toplevel(root)
    update_game_window.title("Update Game Details")

    game_id_label = tk.Label(update_game_window, text="Game ID")
    game_id_entry = tk.Entry(update_game_window)
    game_id_entry.insert(0, game_details[0][0])
    game_name_label = tk.Label(update_game_window, text="Game Name")
    game_name_entry = tk.Entry(update_game_window)
    game_name_entry.insert(0, game_details[0][1])
    storage_label = tk.Label(update_game_window, text="Storage")
    storage_entry = tk.Entry(update_game_window)
    storage_entry.insert(0, game_details[0][2])
    ram_label = tk.Label(update_game_window, text="RAM")
    ram_entry = tk.Entry(update_game_window)
    ram_entry.insert(0, game_details[0][3])
    graphic_req_label = tk.Label(update_game_window, text="Graphic Req")
    graphic_req_entry = tk.Entry(update_game_window)
    graphic_req_entry.insert(0, game_details[0][4])
    genre_label = tk.Label(update_game_window, text="Genre")
    genre_entry = tk.Entry(update_game_window)
    genre_entry.insert(0, game_details[0][5])
    date_label = tk.Label(update_game_window, text="Date of Launch (yy-mm-dd)")
    date_entry = tk.Entry(update_game_window)
    date_entry.insert(0, game_details[0][6])

    def save_changes():
        new_game_id = int(game_id_entry.get())
        new_game_name = game_name_entry.get()
        new_storage = storage_entry.get()
        new_ram = ram_entry.get()
        new_graphic_req = graphic_req_entry.get()
        new_genre = genre_entry.get()
        new_date = date_entry.get()

        cmd = "UPDATE GMAC SET GAME_NAME = %s, STORAGE = %s, RAM = %s, GRAPHIC_REQ = %s, GENRE = %s, DATE_OF_LAUNCH = %s WHERE GAME_ID = %s"
        cr.execute(cmd, (new_game_name, new_storage, new_ram, new_graphic_req, new_genre, new_date, new_game_id))
        cn.commit()

        for row in dat:
            if row[0] == new_game_id:
                row[1] = new_game_name
                row[2] = new_storage
                row[3] = new_ram
                row[4] = new_graphic_req
                row[5] = new_genre
                row[6] = new_date

        # Write the updated data to the CSV file
        with open("data.csv", "w", newline="") as new_file:
            writer = c.writer(new_file)
            writer.writerows(dat)

        messagebox.showinfo("Success", "Game details updated successfully!")
        update_game_window.destroy()

    save_button = tk.Button(update_game_window, text="Save Changes", command=save_changes)

    game_id_label.pack()
    game_id_entry.pack()
    game_name_label.pack()
    game_name_entry.pack()
    storage_label.pack()
    storage_entry.pack()
    ram_label.pack()
    ram_entry.pack()
    graphic_req_label.pack()
    graphic_req_entry.pack()
    genre_label.pack()
    genre_entry.pack()
    date_label.pack()
    date_entry.pack()
    save_button.pack()

# Create buttons for various functions
donate_button = tk.Button(root, text="Donate a Game", command=donate_game)
search_button = tk.Button(root, text="Search for a Game", command=search_game)
remove_button = tk.Button(root, text="Remove a Game", command=remove_game)
update_button = tk.Button(root, text="Update a Game", command=update_game)
show_data_button = tk.Button(root, text="Show Data", command=display_data)

donate_button.pack()
search_button.pack()
remove_button.pack()
update_button.pack()
show_data_button.pack()

# Display the initial data
display_data()

# Start the Tkinter main loop
root.mainloop()

# Close the CSV file and database connection when the application is closed
fl.close()
cn.close()
