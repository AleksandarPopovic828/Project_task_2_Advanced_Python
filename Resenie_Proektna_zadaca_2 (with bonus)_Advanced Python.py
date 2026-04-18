import tkinter as tk
import mysql.connector
from tkinter import ttk, messagebox

#Povrzuvanje so bazata
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='game_store'
)

cursor=conn.cursor()
print("Connected succesfuly to database")

#INSERT game
def insert_game():
    title=entry_title.get()
    genre=entry_genre.get()
    prine=entry_prine.get()
    stock=entry_stock.get()

    sql="""
    INSERT INTO games (title, genre, prine, stock)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(sql, (title,genre,prine,stock))
    conn.commit()

    result_label.config(text="Game was inserted succesfuly!")

# Update game
def update_game():
    title=entry_title.get()
    genre=entry_genre.get()
    prine=entry_prine.get()
    stock=entry_stock.get()

    sql="""
    UPDATE games
    SET genre=%s,
        prine=%s,
        stock=%s
    WHERE title=%s
    """

    cursor.execute(sql, (genre,prine,stock,title))
    conn.commit()

    result_label.config(text="Game was updated succesfuly")

def delete_game():
    title=entry_delete.get()

    sql="""
    DELETE from games where title=%s
    """

    cursor.execute(sql, (title,))
    conn.commit()

    result_label.config(text="Game was succesfuly deleted")

#Show all games
def show_all_games():
    cursor.execute("Select * FROM games")
    rows=cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

#GUI
root=tk.Tk()
root.title("Game management")

#Add and Update
tk.Label(root, text="Title").pack()
entry_title=tk.Entry(root)
entry_title.pack()

tk.Label(root, text="Genre").pack()
entry_genre=tk.Entry(root)
entry_genre.pack()

tk.Label(root, text="Price").pack()
entry_prine=tk.Entry(root)
entry_prine.pack()

tk.Label(root, text="Stock").pack()
entry_stock=tk.Entry(root)
entry_stock.pack()

tk.Button(root, text="Insert Game", command=insert_game).pack()
tk.Button(root, text="Update Game", command=update_game).pack()


#Delete
tk.Label(root, text="Title").pack()
entry_delete=tk.Entry(root)
entry_delete.pack()

tk.Button(root, text="Delete Game", command=delete_game).pack()

# Treeview widget to display records
columns = ("title", "genre", "price", "stock")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=20)

#Lista igri
tk.Button(root, text="Show all Games", command=show_all_games).pack()

#Procisti gi podatocite
result_label=tk.Label(root, text="")
result_label.pack()

root.mainloop()

cursor.close()
conn.close()