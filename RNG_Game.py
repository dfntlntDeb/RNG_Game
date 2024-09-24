import mysql.connector 
import tkinter as tk
from tkinter import *
import random
import datetime as dati

# Establish connection
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rng_rolls"
    )
except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
    db_connection = None  # If the connection fails, set it to None

def on_close():
    if db_connection:
        db_connection.close()
    window.destroy()

def chnc_wndw():
    chance_wndw = tk.Toplevel()
    chance_wndw.title("Anime Defenders Lucky Trait Draw - Chances")
    chance_wndw.geometry("600x400")
    chance_wndw.iconphoto(False, logo)

    # Create a canvas and a vertical scrollbar linked to it
    canvas = tk.Canvas(chance_wndw)
    scrollbar = tk.Scrollbar(chance_wndw, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    #For the scrollbar
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    header_trait = tk.Label(scrollable_frame, text="Trait", font=("Segoe UI", 18, "bold"))
    header_trait.grid(row=0, column=0, padx=10, pady=5)

    header_info = tk.Label(scrollable_frame, text="Info", font=("Arial", 18, "bold"))
    header_info.grid(row=0, column=1, padx=10, pady=5)

    header_chance = tk.Label(scrollable_frame, text="Chance", font=("Arial", 18, "bold"))
    header_chance.grid(row=0, column=2, padx=10, pady=5)

    #To get the table for Traits and Chances
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT Trait, Info, Chance FROM chances")
        data = cursor.fetchall()

        
        for i, row in enumerate(data, start=1):
            trait, info, chance = row

            tk.Label(scrollable_frame, text=trait, font=("Segoe UI", 12,"bold")).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(scrollable_frame, text=info, wraplength=300, font=("Segoe UI", 12,"bold")).grid(row=i, column=1, padx=10, pady=5)
            tk.Label(scrollable_frame, text=chance, font=("Segoe UI", 12,"bold")).grid(row=i, column=2, padx=10, pady=5)

    #If the table can't be retreived
    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")

    
    center_window(chance_wndw)



def show_history():
    history = tk.Toplevel()
    history.title("Anime Defenders Lucky Trait Draw - Rolls History")
    history.geometry("450x600")
    history.iconphoto(False, logo)

    def clear_history():
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM rolls")
        print("Clearing history...")
        history.destroy()

    def load_history():
        try:
            cursor = db_connection.cursor()
            cursor.execute("SELECT Rolled_Trait, Date_Rolled FROM rolls")
            data = cursor.fetchall()

        
            for i, row in enumerate(data, start=1):
                rolled_trait, date_rolled = row

                tk.Label(scrollable_frame, text=rolled_trait, font=("Segoe UI", 12,"bold")).grid(row=i, column=0, padx=10, pady=5)
                tk.Label(scrollable_frame, text=date_rolled, wraplength=300, font=("Segoe UI", 12,"bold")).grid(row=i, column=1, padx=10, pady=5)

        except mysql.connector.Error as err:
           print(f"Error fetching data: {err}")


    canvas = tk.Canvas(history)
    scrollbar = tk.Scrollbar(history, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    header_rolled = tk.Label(scrollable_frame, text="Trait", font=("Segoe UI", 18, "bold"))
    header_rolled.grid(row=0, column=0, padx=10, pady=5)

    header_daterolled = tk.Label(scrollable_frame, text="Info", font=("Segoe UI", 18, "bold"))
    header_daterolled.grid(row=0, column=1, padx=10, pady=5)
    
    clear_Button = tk.Button(scrollable_frame, text="Clear Rolls", font=("Segoe UI", 12, "bold"), command=clear_history)
    clear_Button.grid(row=0, column=2, padx=5, pady=5)

    load_history()

    center_window (history)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def roll_trait():
    global cntr
    increment = 1
    rolled_trait = roll_trait_once()
    result_var.set(rolled_trait)
    set_trait_color(rolled_trait)
    cntr.set(cntr.get() + increment)
    counter.config(text=f"You rolled {cntr.get()} times.")
    send_sql()

def send_sql():
    if db_connection is None:
        print("No active database connection.")
        return

    now = dati.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor = db_connection.cursor()
        query = f"INSERT INTO rolls (Rolled_Trait, Date_Rolled) VALUES (%s, %s)"
        cursor.execute(query, (result_var.get(), date_time))
        db_connection.commit()
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")

def roll_trait_once():
    roll = random.random()
    cumulative_probability = 0.0
    for trait, chances in traits.items():
        cumulative_probability += chances["chances"]
        if roll < cumulative_probability:
            return trait
    return "No Trait"

def set_trait_color(rolled_trait):
    rarity_colors = {
        "Normal": "black",
        "Epic": "purple",
        "Legendary": "orange",
        "Mythical": "red"
    }
    trait_rarity = next((r for r, rarity_list in rarity_list.items() if rolled_trait in rarity_list), None)
    if trait_rarity:
        result_entry.config(fg=rarity_colors.get(trait_rarity, "black"))

cursor = db_connection.cursor()
cursor.execute("SELECT * FROM traits")
query_result = cursor.fetchall()

traits = {}
for row in query_result:
    trait, rarity, chances = row
    traits[trait] = {"rarity": rarity, "chances": chances}

rarity_list = {
    "Normal": ["Brawler 1", "Brawler 2", "Brawler 3", "Swiftness 1", "Swiftness 2", "Swiftness 3", "Hunter 1", "Hunter 2", "Hunter 3", "Critical 1", "Critical 2", "Critical 3", "Prodigy 1"],
    "Epic": ["Midas Touch 1","Bullseye 1"],
    "Legendary": ["Sonic 1", "Precision 1"],
    "Mythical": ["Requiem 1", "Almighty 1"]
}
window = tk.Tk()
window.geometry("700x500")
logo = PhotoImage(file=r"C:\Users\chibi\Python Codes\RNG_Game\RR_Logo.png")
window.iconphoto(False, logo)
window.title("Anime Defenders Lucky Trait Draw")
window.config(bg="black")
center_window(window)

result_var = tk.StringVar()
result_entry = tk.Entry(window, font=("Segoe UI", 33, "bold"), textvariable=result_var, state="readonly", justify="center")


result_entry.pack(pady=(150,50), padx="50")

buttFrame = tk.Frame(window, bg="black")

chnc_Button = tk.Button(buttFrame, text="Chances", font=("Segoe UI", 13, "bold"), fg="black", pady=10, padx=20, borderwidth=3, bg="white", command=chnc_wndw, activebackground="grey", activeforeground="darkgrey")
chnc_Button.grid(column=0,row=0, padx=25)

reroll_button = tk.Button(buttFrame, text="Reroll Trait", font=("Segoe UI", 13, "bold"), fg="black", pady=10, padx=20, borderwidth=3, bg="white", command=roll_trait, activebackground="grey", activeforeground="darkgrey")
reroll_button.grid(column=1,row=0, padx=25)

rolh_Button = tk.Button(buttFrame, text="Rolls History", font=("Segoe UI", 13, "bold"), fg="black", pady=10, padx=20, borderwidth=3, bg="white", command=show_history, activebackground="grey", activeforeground="darkgrey")
rolh_Button.grid(column=2,row=0, padx=25)

buttFrame.pack()

cntr = tk.IntVar()
counter = tk.Label(window, text=f"You rolled {cntr.get()} times.", font=("Segoe UI", 32, "bold"), bg="black", fg="white")
counter.pack(padx=20, pady=20)

window.protocol("WM_DELETE_WINDOW", on_close)

window.mainloop()
