# import mysql.connector as msq
# import csv
# import tkinter as tk
# from tkinter import ttk, messagebox

# # Database connection and cursor
# cn = msq.connect(host='localhost', user='root', passwd='root', database='gym')
# cr = cn.cursor()

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Gaming Arcade Management")
# root.geometry("800x400")
# root.configure(bg="#99FFFF")

# # Open the CSV file for reading and writing
# csv_file_path = "data.csv"

# # Create a Frame for options on the left side
# options_frame = tk.Frame(root, bg="#99FFFF")
# options_frame.pack(side=tk.LEFT, padx=10, pady=10)

# # Create a Frame for the Treeview on the right side
# treeview_frame = tk.Frame(root, bg="#99FFFF")
# treeview_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# # Create a Treeview widget to display the data in a tabular form
# tree = ttk.Treeview(treeview_frame, columns=("GameName", "Storage", "RAM", "GraphicReq", "Genre", "DateOfLaunch"))
# tree.heading("#1", text="Game Name")
# tree.heading("#2", text="Storage")
# tree.heading("#3", text="RAM")
# tree.heading("#4", text="Graphic Req")
# tree.heading("#5", text="Genre")
# tree.heading("#6", text="Date Of Launch")
# tree.pack()

# # Function to display data in the Treeview
# def display_data_in_treeview():
#     for record in tree.get_children():
#         tree.delete(record)
#     cmd = "SELECT * FROM GMAC"
#     cr.execute(cmd)
#     data = cr.fetchall()
#     for row in data:
#         tree.insert("", "end", values=row)

# # Function to donate a game
# def donate_game():
#     donate_window = tk.Toplevel(root)
#     donate_window.title("Donate a Game")

#     labels = ["Game Name", "Storage", "RAM", "Graphic Req", "Genre", "Date of Launch"]
#     entries = []

#     for label_text in labels:
#         label = tk.Label(donate_window, text=label_text)
#         label.pack()

#         entry = tk.Entry(donate_window)
#         entry.pack()

#         entries.append(entry)

#     def submit():
#         try:
#             game_data = [entry.get() for entry in entries]
#             st = "INSERT INTO GMAC VALUES('{}','{}','{}','{}','{}','{}')".format(*game_data)
#             cr.execute(st)

#             cn.commit()
#             display_data_in_treeview()
#             write_to_csv()
#             donate_window.destroy()
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid values.")

#     submit_button = tk.Button(donate_window, text="Submit", command=submit)
#     submit_button.pack()

# # Function to search for a game
# def search_game():
#     search_window = tk.Toplevel(root)
#     search_window.title("Search for a Game")

#     def open_search_by_name():
#         search_page = tk.Toplevel(search_window)
#         search_page.title("Search by Name")

#         label_name = tk.Label(search_page, text="Enter the name of the game:")
#         entry_name = tk.Entry(search_page)
#         label_name.pack(pady=10)
#         entry_name.pack(pady=10)

#         def execute_search():
#             try:
#                 name = entry_name.get()
#                 query = "SELECT * FROM GMAC WHERE GAME_NAME='{}'".format(name)
#                 cr.execute(query)
#                 result = cr.fetchall()
#                 print("[GAME_ID, GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH]")
#                 for row in result:
#                     print(row)
#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred: {str(e)}")

#         search_button = tk.Button(search_page, text="Search", command=execute_search)
#         search_button.pack(pady=10)

#     def open_search_by_genre():
#         search_page = tk.Toplevel(search_window)
#         search_page.title("Search by Genre")

#         label_genre = tk.Label(search_page, text="Enter the genre of the game:")
#         entry_genre = tk.Entry(search_page)
#         label_genre.pack(pady=10)
#         entry_genre.pack(pady=10)

#         def execute_search():
#             try:
#                 genre = entry_genre.get()
#                 query = "SELECT * FROM GMAC WHERE GENRE='{}'".format(genre)
#                 cr.execute(query)
#                 result = cr.fetchall()
#                 print("[GAME_ID, GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH]")
#                 for row in result:
#                     print(row)
#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred: {str(e)}")

#         search_button = tk.Button(search_page, text="Search", command=execute_search)
#         search_button.pack(pady=10)

#     def open_search_by_compatibility():
#         search_page = tk.Toplevel(search_window)
#         search_page.title("Search by Compatibility")

#         label_ram = tk.Label(search_page, text="Enter RAM required:")
#         entry_ram = tk.Entry(search_page)
#         label_ram.pack(pady=10)
#         entry_ram.pack(pady=10)

#         label_storage = tk.Label(search_page, text="Enter Storage required:")
#         entry_storage = tk.Entry(search_page)
#         label_storage.pack(pady=10)
#         entry_storage.pack(pady=10)

#         label_graphic_card = tk.Label(search_page, text="Enter Graphic card requirement (Y/N):")
#         entry_graphic_card = tk.Entry(search_page)
#         label_graphic_card.pack(pady=10)
#         entry_graphic_card.pack(pady=10)

#         def execute_search():
#             try:
#                 ram = int(entry_ram.get())
#                 storage = int(entry_storage.get())
#                 graphic_card = entry_graphic_card.get()
#                 query = "SELECT * FROM GMAC WHERE STORAGE<={} AND RAM<={} AND GRAPHIC_REQ='{}'".format(storage, ram, graphic_card)
#                 cr.execute(query)
#                 result = cr.fetchall()
#                 print("[GAME_ID, GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH]")
#                 for row in result:
#                     print(row)
#             except ValueError:
#                 messagebox.showerror("Error", "Please enter valid numbers for RAM and Storage.")
#             except Exception as e:
#                 messagebox.showerror("Error", f"An error occurred: {str(e)}")

#         search_button = tk.Button(search_page, text="Search", command=execute_search)
#         search_button.pack(pady=10)

#     name_button = tk.Button(search_window, text="Search by Name", command=open_search_by_name)
#     name_button.pack(pady=10)

#     genre_button = tk.Button(search_window, text="Search by Genre", command=open_search_by_genre)
#     genre_button.pack(pady=10)

#     compatibility_button = tk.Button(search_window, text="Search by Compatibility", command=open_search_by_compatibility)
#     compatibility_button.pack(pady=10) 
# # Function to remove a game
# def remove_game():
#     remove_window = tk.Toplevel(root)
#     remove_window.title("Remove a Game")

#     label_game_name = tk.Label(remove_window, text="Enter Game Name:")
#     entry_game_name = tk.Entry(remove_window)
#     label_game_name.pack()
#     entry_game_name.pack()

#     def execute_removal():
#         try:
#             game_name = entry_game_name.get()
#             cmd = "DELETE FROM GMAC WHERE GAME_NAME='{}'".format(game_name)
#             cr.execute(cmd)
#             cn.commit()
#             print("Game Deleted :(")
#             display_data_in_treeview()
#             write_to_csv()
#             remove_window.destroy()
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid number.")

#     remove_button = tk.Button(remove_window, text="Remove", command=execute_removal)
#     remove_button.pack()

# # Function to update a game
# # Function to update a game
# def update_game():
#     update_window = tk.Toplevel(root)
#     update_window.title("Update a Game")

#     # Fetch all game names from the database
#     cr.execute("SELECT GAME_NAME FROM GMAC")
#     game_names = [row[0] for row in cr.fetchall()]

#     # Dropdown menu for selecting the game
#     label_game_name = tk.Label(update_window, text="Select Game Name:")
#     selected_game_name = tk.StringVar(update_window)
#     game_name_dropdown = ttk.Combobox(update_window, textvariable=selected_game_name, values=game_names)
#     label_game_name.pack()
#     game_name_dropdown.pack()

#     # Entry fields for updating values
#     labels = ["Game Name", "Genre", "Storage", "RAM", "Graphic Req", "Date of Launch"]
#     entries = []

#     for label_text in labels:
#         label = tk.Label(update_window, text=label_text)
#         label.pack()

#         entry = tk.Entry(update_window)
#         entry.pack()

#         entries.append(entry)

#     def execute_update():
#         try:
#             selected_name = selected_game_name.get()
#             updated_info = [entry.get() for entry in entries]

#             fields = ["GAME_NAME", "GENRE", "STORAGE", "RAM", "GRAPHIC_REQ", "DATE_OF_LAUNCH"]
#             update_values = ", ".join([f"{field}='{value}'" for field, value in zip(fields, updated_info)])

#             cmd = f"UPDATE GMAC SET {update_values} WHERE GAME_NAME='{selected_name}'"
#             cr.execute(cmd)
#             cn.commit()
#             display_data_in_treeview()
#             write_to_csv()
#             update_window.destroy()
#         except ValueError:
#             messagebox.showerror("Error", "Please enter valid values.")

#     update_button = tk.Button(update_window, text="Update", command=execute_update)
#     update_button.pack()


# # GUI Buttons
# donate_button = tk.Button(options_frame, text="Donate a Game", command=donate_game, bg="#7FFFD4")
# search_button = tk.Button(options_frame, text="Search for a Game", command=search_game, bg="#7FFFD4")
# remove_button = tk.Button(options_frame, text="Remove a Game", command=remove_game, bg="#7FFFD4")
# update_button = tk.Button(options_frame, text="Update a Game", command=update_game, bg="#7FFFD4")
# show_data_button = tk.Button(options_frame, text="Show Data", command=display_data_in_treeview, bg="#7FFFD4")

# # GUI Packing
# donate_button.pack(side=tk.TOP, padx=10, pady=10)
# search_button.pack(side=tk.TOP, padx=10, pady=10)
# remove_button.pack(side=tk.TOP, padx=10, pady=10)
# update_button.pack(side=tk.TOP, padx=10, pady=10)
# show_data_button.pack(side=tk.TOP, padx=10, pady=10)

# # Display the initial data in the Treeview
# display_data_in_treeview()

# # Start the Tkinter main loop
# root.mainloop()

# # Close the CSV file and database connection when the application is closed
# cn.close()
import mysql.connector as msq
import csv
import tkinter as tk
from tkinter import ttk, messagebox

# Database connection and cursor
cn = msq.connect(host='localhost', user='root', passwd='root', database='gym')
cr = cn.cursor()

# Create a Tkinter window
root = tk.Tk()
root.title("Gaming Arcade Management")
root.geometry("800x400")
root.configure(bg="#99FFFF")

# Open the CSV file for reading and writing
csv_file_path = "data.csv"

# Create a Frame for options on the left side
options_frame = tk.Frame(root, bg="#99FFFF")
options_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a Frame for the Treeview on the right side
treeview_frame = tk.Frame(root, bg="#99FFFF")
treeview_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a Treeview widget to display the data in a tabular form
tree = ttk.Treeview(treeview_frame, columns=("GameName", "Storage", "RAM", "GraphicReq", "Genre", "DateOfLaunch"))
tree.heading("#1", text="Game Name")
tree.heading("#2", text="Storage")
tree.heading("#3", text="RAM")
tree.heading("#4", text="Graphic Req")
tree.heading("#5", text="Genre")
tree.heading("#6", text="Date Of Launch")
tree.pack()

# Function to display data in the Treeview
def display_data_in_treeview():
    for record in tree.get_children():
        tree.delete(record)
    cmd = "SELECT * FROM GMAC"
    cr.execute(cmd)
    data = cr.fetchall()
    for row in data:
        tree.insert("", "end", values=row)

# Function to donate a game
def donate_game():
    donate_window = tk.Toplevel(root)
    donate_window.title("Donate a Game")

    labels = ["Game Name", "Storage", "RAM", "Graphic Req", "Genre", "Date of Launch"]
    entries = []

    for label_text in labels:
        label = tk.Label(donate_window, text=label_text)
        label.pack()

        entry = tk.Entry(donate_window)
        entry.pack()

        entries.append(entry)

    def submit():
        try:
            game_data = [entry.get() for entry in entries]
            st = "INSERT INTO GMAC VALUES('{}','{}','{}','{}','{}','{}')".format(*game_data)
            cr.execute(st)

            cn.commit()
            display_data_in_treeview()
            write_to_csv()
            donate_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values.")

    submit_button = tk.Button(donate_window, text="Submit", command=submit)
    submit_button.pack()

# Function to search for a game
def search_game():
    search_window = tk.Toplevel(root)
    search_window.title("Search for a Game")

    label_aspect = tk.Label(search_window, text="Enter the aspect by which you want game suggestions:")
    entry_aspect = tk.Entry(search_window)
    label_aspect.pack()
    entry_aspect.pack()

    def execute_search():
        try:
            aspect = int(entry_aspect.get())
            if aspect == 1:
                qr = input("Enter the name of the game: ")
                cmd = "SELECT * FROM GMAC WHERE GAME_NAME='{}'".format(qr)
            elif aspect == 2:
                qr = input("Enter genre of game: ")
                cmd = "SELECT * FROM GMAC WHERE GENRE='{}'".format(qr)
            elif aspect == 3:
                q1 = int(input("Enter the RAM required: "))
                q2 = input("Enter if graphic card is required (Y/N): ")
                q3 = int(input("Enter the storage required: "))
                cmd = "SELECT * FROM GMAC WHERE STORAGE<={} AND RAM<={} AND GRAPHIC_REQ='{}'".format(q3, q1, q2)

            cr.execute(cmd)
            result = cr.fetchall()
            print("[GAME_ID, GAME_NAME, STORAGE, RAM, GRAPHIC_REQ, GENRE, DATE_OF_LAUNCH]")
            for row in result:
                print(row)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    search_button = tk.Button(search_window, text="Search", command=execute_search)
    search_button.pack()

# Function to remove a game
def remove_game():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove a Game")

    label_game_name = tk.Label(remove_window, text="Enter Game Name:")
    entry_game_name = tk.Entry(remove_window)
    label_game_name.pack()
    entry_game_name.pack()

    def execute_removal():
        try:
            game_name = entry_game_name.get()
            cmd = "DELETE FROM GMAC WHERE GAME_NAME='{}'".format(game_name)
            cr.execute(cmd)
            cn.commit()
            print("Game Deleted :(")
            display_data_in_treeview()
            write_to_csv()
            remove_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    remove_button = tk.Button(remove_window, text="Remove", command=execute_removal)
    remove_button.pack()

# Function to update a game
# Function to update a game
def update_game():
    update_window = tk.Toplevel(root)
    update_window.title("Update a Game")

    # Fetch all game names from the database
    cr.execute("SELECT GAME_NAME FROM GMAC")
    game_names = [row[0] for row in cr.fetchall()]

    # Dropdown menu for selecting the game
    label_game_name = tk.Label(update_window, text="Select Game Name:")
    selected_game_name = tk.StringVar(update_window)
    game_name_dropdown = ttk.Combobox(update_window, textvariable=selected_game_name, values=game_names)
    label_game_name.pack()
    game_name_dropdown.pack()

    # Entry fields for updating values
    labels = ["Game Name", "Genre", "Storage", "RAM", "Graphic Req", "Date of Launch"]
    entries = []

    for label_text in labels:
        label = tk.Label(update_window, text=label_text)
        label.pack()

        entry = tk.Entry(update_window)
        entry.pack()

        entries.append(entry)

    def execute_update():
        try:
            selected_name = selected_game_name.get()
            updated_info = [entry.get() for entry in entries]

            fields = ["GAME_NAME", "GENRE", "STORAGE", "RAM", "GRAPHIC_REQ", "DATE_OF_LAUNCH"]
            update_values = ", ".join([f"{field}='{value}'" for field, value in zip(fields, updated_info)])

            cmd = f"UPDATE GMAC SET {update_values} WHERE GAME_NAME='{selected_name}'"
            cr.execute(cmd)
            cn.commit()
            display_data_in_treeview()
            write_to_csv()
            update_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values.")

    update_button = tk.Button(update_window, text="Update", command=execute_update)
    update_button.pack()


# GUI Buttons
donate_button = tk.Button(options_frame, text="Donate a Game", command=donate_game, bg="#7FFFD4")
search_button = tk.Button(options_frame, text="Search for a Game", command=search_game, bg="#7FFFD4")
remove_button = tk.Button(options_frame, text="Remove a Game", command=remove_game, bg="#7FFFD4")
update_button = tk.Button(options_frame, text="Update a Game", command=update_game, bg="#7FFFD4")
show_data_button = tk.Button(options_frame, text="Show Data", command=display_data_in_treeview, bg="#7FFFD4")

# GUI Packing
donate_button.pack(side=tk.TOP, padx=10, pady=10)
search_button.pack(side=tk.TOP, padx=10, pady=10)
remove_button.pack(side=tk.TOP, padx=10, pady=10)
update_button.pack(side=tk.TOP, padx=10, pady=10)
show_data_button.pack(side=tk.TOP, padx=10, pady=10)

# Display the initial data in the Treeview
display_data_in_treeview()

# Start the Tkinter main loop
root.mainloop()

# Close the CSV file and database connection when the application is closed
cn.close()