import wikipedia
from tkinter import *

def on_press():
    query = get_query.get()
    if query:
        result = wikipedia.summary(query)
        text.delete(1.0, END) 
        text.insert(END, result)
    else:
        text.delete(1.0, END)
        text.insert(END, "Please enter a query.")

root = Tk()
root.title("Wikipedia Search")
question = Label(root, text="Pertanyaan: ")
question.pack()
get_query = Entry(root, bd=5)
get_query.pack()
submit_button = Button(root, text="Search", command=on_press)
submit_button.pack()
text = Text(root)
text.pack()

root.mainloop()
