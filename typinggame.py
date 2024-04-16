from tkinter import *
import random

win = Tk()
win.title("Typing Game")
win.geometry("650x250")

win.configure(bg="blue")

sentences = ['The sun rose gently, warming the earth.',
 'Leaves rustled softly in the breeze.',
 'A cat stretched out, seeking sunlight.',
 'Rain tapped lightly against the window.',
 'Birds sang joyfully at dawn.',
 'Clouds floated lazily across the sky.',
 'The moon glowed, illuminating the night.',
 'Stars sparkled like distant diamonds.',
 'A frog croaked near the pond.',
 'Flowers bloomed, adding color to the garden.',
 'The wind whispered secrets through the trees.',
 'A dog barked excitedly in the distance.',
 'Ice cracked as it began to melt.',
 'Snowflakes swirled in the winter air.',
 'Bees buzzed around the blossoms.',
 'Waves crashed against the shore.',
 'Lightning illuminated the stormy sky.',
 'Thunder echoed, rumbling ominously.',
 'A door creaked open slowly.',
 'Fireflies lit up the night with their glow.']

score = 0
time = 120

cursen = random.choice(sentences)

welcomelbl = Label(text="Welcome to the typing game! Just type sentenses for 2 minutes and gain score.", fg="white", bg="blue", font=('Tahoma', 12))
welcomelbl.pack()

startlbl = Label(text="Hit <enter> to start the game!", fg="white", bg="blue", font=("Tahoma", 11))
startlbl.pack()

scorelbl = Label(text="Score: 0", fg="white", bg="blue", font=("Tahoma", 11))
scorelbl.pack()

timelbl = Label(text="Time Left: 120 seconds", fg="white", bg="blue", font=("Tahoma", 11))
timelbl.pack()

blanklbl = Label(text="", height=1, bg="blue")
blanklbl.pack()

senlbl = Label(text="Start the game!", fg="white", bg="blue", font=("Tahoma", 20))
senlbl.pack()

senentry = Entry(win, width=100)
senentry.place(x=25, y=200)

def countdown():
    global time
    if time > 0:
        time -= 1
        timelbl.configure(text=f"Time Left: {str(time)} seconds")
        timelbl.after(1000, countdown)
    else:
        senlbl.configure(text=f"Game Over! Your score is {score}!", bg="blue", fg="green")
        timelbl.configure(text="Game Over", fg="red", bg="blue")
        win.unbind('<Return>')

def start(event):
    if time == 120:
        countdown()
        startlbl.configure(text="Start typing!")
    ransen()

def ransen():
    global score
    global cursen

    if senentry.get() == cursen:
        score += 1
        scorelbl.configure(text=f"Score: {score}")

    senentry.delete(0, END)
    cursen = random.choice(sentences)
    print(cursen)
    senlbl.configure(text=cursen)

win.bind("<Return>", start)

win.mainloop()
