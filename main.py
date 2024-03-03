import tkinter
import secrets

def pick_another_name():
    names = ["Ishaq", "Dibas", "Suman", "Narayan", "Pika", "Onda", "Komi"]
    random_name.config(text=secrets.choice(names))

window = tkinter.Tk()
window.title("Random Name Picker")
window.geometry('250x60')
window.attributes('-topmost', True)

frame = tkinter.Frame(window)

random_name = tkinter.Label(frame, text="Dibas", font=("Arial", 15), pady=15)
generate_btn = tkinter.Button(frame, text="Pick another", padx=8, command=pick_another_name)

random_name.grid(row=0, column=0)
generate_btn.grid(row=0, column=1, padx=(10,0))

frame.pack()

window.mainloop()