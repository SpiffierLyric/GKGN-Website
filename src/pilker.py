import tkinter as tk
import random
from tkinter import messagebox

# This part ensures the window is sharp on high-resolution monitors
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass  # Non-Windows systems or older versions will skip this


def generate_pilk():
    p_liquids = [
        "Pepsi", "Pool Chlorine", "Prune Juice", "Pickle Juice",
        "Pineapple Soda", "Pomegranate Juice", "Peach Schnapps",
        "Pink Lemonade", "Paint Thinner", "Punch", "Powerade", "Propel",
        "Palm oil", "Panthenol", "Papaya juice", "Paraffin oil",
        "Paraldehyde", "Patchouli oil", "Peach nectar", "Peanut oil",
        "Pear juice", "Pentane", "Peppermint oil", "Peracetic acid",
        "Perchloric acid", "Perfume", "Petroleum", "Phenol",
        "Phosphoric acid", "Pickle juice", "Pine oil", "Pineapple juice",
        "Pinot Noir", "Pisco", "Plasma", "Plum wine", "Polyethylene glycol",
        "Pomegranate juice", "Potash", "Propane (liquid state)",
        "Propanol", "Propionic acid", "Propylene glycol", "Punch", "Pyridine"
    ]

    milks = [
        # Standard Dairy & Processed
        "Whole Milk", "Skim Milk", "Low-fat Milk", "Condensed Milk",
        "Evaporated Milk", "Buttermilk", "Raw Milk", "Malted Milk",
        "Powdered Milk", "Acidophilus Milk", "Lactose-free Milk",

        # Plant-Based (Nuts, Seeds, Grains, Legumes)
        "Almond Milk", "Oat Milk", "Soy Milk", "Cashew Milk",
        "Coconut Milk", "Pistachio Milk", "Rice Milk", "Hemp Milk",
        "Macadamia Milk", "Pea Milk", "Hazelnut Milk", "Tiger Nut Milk",
        "Walnut Milk", "Spelt Milk", "Quinoa Milk", "Flax Milk",
        "Sesame Milk", "Peanut Milk", "Sunflower Seed Milk",

        # Animal Sources (Mammalian)
        "Breast Milk", "Goat Milk", "Sheep Milk", "Camel Milk",
        "Buffalo Milk", "Donkey Milk", "Yak Milk", "Reindeer Milk",
        "Horse Milk", "Moose Milk", "Rat Milk",

        # Flavored & Specific Use
        "Chocolate Milk", "Strawberry Milk", "Coffee Milk",
        "Vanilla Milk", "Banana Milk", "Golden Milk"
    ]

    liquid = random.choice(p_liquids)
    milk = random.choice(milks)

    result_label.config(text=f"{liquid} + {milk}", fg="#2ecc71")


# --- GUI Setup ---
root = tk.Tk()
root.title("The Ultimate Pilk Generator (High-Res)")

# Set window size for 2k monitor
root.geometry("800x600")
root.configure(bg="#2c3e50")

# Title Label - Increased Font Size
title_label = tk.Label(
    root,
    text="Pilk Combination Generator",
    font=("Helvetica", 32, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1",
    pady=40
)
title_label.pack()

# Result Display Area - Increased Font and Wraplength
result_label = tk.Label(
    root,
    text="Press the button to begin...",
    font=("Helvetica", 28, "italic"),
    bg="#2c3e50",
    fg="#bdc3c7",
    wraplength=700,  # Increased to match window width
    pady=60
)
result_label.pack()

# Generate Button - Larger size and padding
generate_button = tk.Button(
    root,
    text="Generate Pilk",
    command=generate_pilk,
    font=("Helvetica", 24, "bold"),
    bg="#e74c3c",
    fg="white",
    padx=40,
    pady=20,
    cursor="hand2",
    activebackground="#c0392b"
)
generate_button.pack(pady=20)

root.mainloop()