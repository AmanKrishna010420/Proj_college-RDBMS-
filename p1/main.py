import mysql.connector as msq
import tkinter as tk
from tkinter import ttk, messagebox

# Database connection and cursor
cn = msq.connect(host='localhost', user='root', passwd='root', database='gym')
cr = cn.cursor()

# Create a table to display game data
def create_table(parent_frame):
    columns = ("GAME_NAME", "STORAGE", "RAM", "GRAPHIC_REQ", "GENRE", "DATE_OF_LAUNCH")
    tree = ttk.Treeview(parent_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True)
    return tree

# Function to donate a game
def donate_game():
    game_name = entry_game_name.get()
    storage = entry_storage.get()
    ram = entry_ram.get()
    graphic_req = entry_graphic_req.get()
    genre = entry_genre.get()
    date_of_launch = entry_date_of_launch.get()

    try:
        # Insert game information into the database
        st = "INSERT INTO GMAC (GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (game_name, storage, ram, graphic_req, genre, date_of_launch)
        cr.execute(st, values)
        cn.commit()
        messagebox.showinfo("Success", "Game donated successfully.")
        update_table()
    except msq.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to search for a game
def search_game():
    search_page = ttk.Frame(main_notebook)
    main_notebook.add(search_page, text="Search Game")

    options_label = tk.Label(search_page, text="Select search options:")
    options_label.pack()

    # Create and pack entry fields for searching game specifications
    ram_label = tk.Label(search_page, text="RAM")
    ram_label.pack()
    entry_ram = tk.Entry(search_page)
    entry_ram.pack()

    storage_label = tk.Label(search_page, text="Storage")
    storage_label.pack()
    entry_storage = tk.Entry(search_page)
    entry_storage.pack()

    graphic_label = tk.Label(search_page, text="Graphic Card (Y/N)")
    graphic_label.pack()
    entry_graphic_req = tk.Entry(search_page)
    entry_graphic_req.pack()

    # Create and pack a search button
    search_button = tk.Button(search_page, text="Search", command=perform_search)
    search_button.pack()

    main_notebook.select(search_page)

# Function to perform the search based on specifications
def perform_search():
    search_term_ram = entry_ram.get()
    search_term_storage = entry_storage.get()
    search_term_graphic_req = entry_graphic_req.get()

    cmd = "SELECT * FROM GMAC WHERE RAM >= %s AND STORAGE >= %s AND GRAPHIC_REQ = %s"
    cr.execute(cmd, (search_term_ram, search_term_storage, search_term_graphic_req))
    result = cr.fetchall()

    search_table.delete(*search_table.get_children())
    for row in result:
        search_table.insert("", "end", values=row)

# Function to remove a game
def remove_game():
    game_name = entry_remove_game_name.get()
    cmd = "DELETE FROM GMAC WHERE GAME_NAME=%s"
    cr.execute(cmd, (game_name,))
    cn.commit()
    messagebox.showinfo("Game Removed", "Game removed successfully.")
    update_table()

# Function to update a game
def update_game():
    game_name = entry_update_game_name.get()
    update_field = combo_update_field.get()
    update_value = entry_update_value.get()

    if update_field == "Name":
        cmd = "UPDATE GMAC SET GAME_NAME=%s WHERE GAME_NAME=%s"
    elif update_field == "Genre":
        cmd = "UPDATE GMAC SET GENRE=%s WHERE GAME_NAME=%s"
    else:
        cmd = "UPDATE GMAC SET STORAGE=%s WHERE GAME_NAME=%s"

    cr.execute(cmd, (update_value, game_name))
    cn.commit()
    messagebox.showinfo("Game Updated", "Game information updated successfully.")
    update_table()

# Function to display all data
def update_table():
    exc = "SELECT * FROM GMAC"
    cr.execute(exc)
    dat = cr.fetchall()

    table.delete(*table.get_children())
    for row in dat:
        table.insert("", "end", values=row)

# Create the main application window
root = tk.Tk()
root.title("Gaming Arcade Management")
root.geometry("800x600")

# Create a notebook to manage pages
main_notebook = ttk.Notebook(root)
main_notebook.pack(fill="both", expand=True)

# Create a frame to contain the table
table_frame = ttk.Frame(root)
table_frame.pack(fill="both", expand=True)

# Create and pack the table
table = create_table(table_frame)

# Create and pack frames for different options
donate_frame = ttk.Frame(main_notebook)
search_frame = ttk.Frame(main_notebook)
remove_frame = ttk.Frame(main_notebook)
update_frame = ttk.Frame(main_notebook)

# Add frames to the notebook
main_notebook.add(donate_frame, text="Donate Game")
main_notebook.add(search_frame, text="Search Game")
main_notebook.add(remove_frame, text="Remove Game")
main_notebook.add(update_frame, text="Update Game")

# Input fields and labels for donating a game
label_game_name = tk.Label(donate_frame, text="Game Name")
label_game_name.pack()
entry_game_name = tk.Entry(donate_frame)
entry_game_name.pack()

storage_label = tk.Label(donate_frame, text="Storage")
storage_label.pack()
entry_storage = tk.Entry(donate_frame)
entry_storage.pack()

ram_label = tk.Label(donate_frame, text="RAM")
ram_label.pack()
entry_ram = tk.Entry(donate_frame)
entry_ram.pack()

graphic_label = tk.Label(donate_frame, text="Graphic Card (Y/N)")
graphic_label.pack()
entry_graphic_req = tk.Entry(donate_frame)
entry_graphic_req.pack()

genre_label = tk.Label(donate_frame, text="Genre")
genre_label.pack()
entry_genre = tk.Entry(donate_frame)
entry_genre.pack()

date_label = tk.Label(donate_frame, text="Date of Launch (yy-mm-dd)")
date_label.pack()
entry_date_of_launch = tk.Entry(donate_frame)
entry_date_of_launch.pack()

# Create and pack a donate button
donate_button = tk.Button(donate_frame, text="Donate Game", command=donate_game)
donate_button.pack()

# Input fields and labels for removing a game
remove_game_name_label = tk.Label(remove_frame, text="Game Name to Remove")
remove_game_name_label.pack()
entry_remove_game_name = tk.Entry(remove_frame)
entry_remove_game_name.pack()

# Create and pack a remove button
remove_button = tk.Button(remove_frame, text="Remove Game", command=remove_game)
remove_button.pack()

# Input fields and labels for updating a game
update_game_name_label = tk.Label(update_frame, text="Game Name to Update")
update_game_name_label.pack()
entry_update_game_name = tk.Entry(update_frame)
entry_update_game_name.pack()

update_field_label = tk.Label(update_frame, text="Field to Update")
update_field_label.pack()
update_options = ["Name", "Genre", "Storage"]
combo_update_field = tk.StringVar()
combo_update_field.set(update_options[0])
update_field = tk.OptionMenu(update_frame, combo_update_field, *update_options)
update_field.pack()

update_value_label = tk.Label(update_frame, text="New Value")
update_value_label.pack()
entry_update_value = tk.Entry(update_frame)
entry_update_value.pack()

# Create and pack an update button
update_button = tk.Button(update_frame, text="Update Game", command=update_game)
update_button.pack()

# Start the GUI application
root.mainloop()
