from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(height=100, width=400)
window.config(padx=60, pady=20)


entry = Entry(width=10)
entry.grid(row=0, column=1, padx=5)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

text_is_equal_to = Label(text="is equal to")
text_is_equal_to.grid(row=1, column=0)

answer = Label(text="0")
answer.grid(row=1, column=1)

Km = Label(text="Km")
Km.grid(row=1, column=2)


def convert_miles_to_km():
    user_input = entry.get()
    kilometer = float(user_input) * 1.6093
    answer.config(text=f"{round(kilometer, 4)}")


calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()
