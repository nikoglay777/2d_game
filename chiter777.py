from tkinter import *


def show_quistion():
        question = quiz[qNumber]
        q_Label.config(text = question['quistion'])

def check():
        ans=enter.get()
        if ans == quiz[qNumber]["anser"]:
                correct_Label.config(text="corect!")

        else:
                correct_Label.config(text="wrong ):")
        but2.config(state="active")
        but1.config(state="disabled")

def next():
        global qNumber
        qNumber += 1
        if qNumber > len(quiz):
                but2.config(state="disabled")
        else:
                show_quistion()
                but1.config(state="active")
                but2.config(state="disabled")


quiz = [{"quistion": "In what year was Spain became a country?",
        "anser": "1479"},

        {"quistion": "In what year Madrid became a capital city?",
         "anser": " 1562 "}]
qNumber = 0

window = Tk()
window.title("quiz")
window.geometry("1920x1080")
but1 = Button(window, text="Check your answer", font=("Courier", 11), height=5, width=25, command=check)
but1.place(x=200, y=100)

but2 = Button(window, text="Next", font=("Courier", 11), command=next, height=5, width=25, state="disabled")
but2.place(x=900, y=100)

enter = Entry(window)
enter.place(x=600, y=300)

q_Label = Label(window, text="Mesater Bist", font=("Courier", 20))
q_Label.place(x=340, y=200)

score_Label = Label(window, text="Score0.5")
score_Label .place(x=1221, y=0)

correct_Label = Label(window, text="")
correct_Label.place(x=0, y=0)

show_quistion()

window.mainloop()
