import tkinter as tk
import random
import pyttsx3
import pygame
import cv2
from PIL import Image, ImageTk

# -----------------------------
# AI Voice (tweak for MJ vibe)
# -----------------------------
engine = pyttsx3.init()

# Try faster + higher pitch feel
engine.setProperty('rate', 190)

def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Background Music
# -----------------------------
pygame.mixer.init()
pygame.mixer.music.load("FUNK DE BELEZA.mp3")
pygame.mixer.music.play(-1)  # loop forever

# -----------------------------
# 100 UNIQUE Brainrot Facts
# -----------------------------
brainrot_facts = [
    "Your brain now needs three videos at once to function.",
    "You opened this app and instantly forgot why.",
    "Your humor now activates before logic loads.",
    "You don’t laugh… you exhale aggressively.",
    "Every silence now feels illegal.",
    "You expect gameplay behind every conversation.",
    "You scroll even after reaching the end.",
    "You blink less when overstimulated.",
    "Your brain thinks loud = funny.",
    "You process memes faster than speech.",
]

# auto-generate more unique-ish ones
for i in range(11, 101):
    brainrot_facts.append(f"Brainrot anomaly #{i}: reality stability decreased by {random.randint(1,99)}%.")

# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("BRAINROT GOD MODE 💀")
root.geometry("800x500")

# Background
bg_image = tk.PhotoImage(file="piccolo-aura-farming-cont-1742982517.png")
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Output text
output_label = tk.Label(root, text="", wraplength=500,
                        font=("Arial", 12, "bold"),
                        bg="black", fg="white")
canvas.create_window(400, 250, window=output_label)

# -----------------------------
# Subway Surfers Video
# -----------------------------
video = cv2.VideoCapture("Subway_surfers_1_hour_Gameplay_no_commentary_free_to_use.mp4")

video_label = tk.Label(root)
canvas.create_window(700, 400, window=video_label)

def update_video():
    ret, frame = video.read()
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        return update_video()

    frame = cv2.resize(frame, (160, 120))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk
    video_label.config(image=imgtk)

    root.after(30, update_video)

# -----------------------------
# Flashing UI
# -----------------------------
colors = ["red", "blue", "green", "purple", "yellow", "cyan"]

def flash():
    output_label.config(bg=random.choice(colors))
    root.after(150, flash)

# -----------------------------
# Functions
# -----------------------------
def show_fact():
    fact = random.choice(brainrot_facts)
    output_label.config(text=fact)
    speak(fact)

def clear():
    output_label.config(text="")
    engine.stop()

# -----------------------------
# Buttons
# -----------------------------
btn_fact = tk.Button(root, text="🔊 BRAINROT FACT", command=show_fact)
btn_clear = tk.Button(root, text="🧹 CLEAR", command=clear)
btn_exit = tk.Button(root, text="❌ EXIT", command=root.quit)

canvas.create_window(400, 350, window=btn_fact)
canvas.create_window(300, 400, window=btn_clear)
canvas.create_window(500, 400, window=btn_exit)

# -----------------------------
# Start animations
# -----------------------------
flash()
update_video()

root.mainloop()
