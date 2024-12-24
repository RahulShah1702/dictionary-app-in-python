import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import ttk

# Function to fetch the word's meaning
def get_meaning():
    word = entry.get().strip()
    if not word:
        messagebox.showwarning("Input Error", "Please enter a word.")
        return

    # Disable the search button while waiting for the response
    search_button.config(state=tk.DISABLED)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Loading...\n")

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        meanings = data[0]["meanings"]

        result_text.delete(1.0, tk.END)
        for meaning in meanings:
            part_of_speech = meaning["partOfSpeech"]
            for definition in meaning["definitions"]:
                result_text.insert(tk.END, f"{part_of_speech.capitalize()}: {definition['definition']}\n\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error fetching data: {str(e)}")
    finally:
        # Re-enable the search button after the request
        search_button.config(state=tk.NORMAL)

# Function to clear the input and results
def clear_results():
    entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Dictionary App")
root.geometry("650x700")
root.configure(bg="#f0f4f8")

# Header Frame with Gradient Background
header_frame = tk.Frame(root, bg="#6200ea", bd=0)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Dictionary App", font=("Helvetica Neue", 24, "bold"), fg="white", bg="#6200ea")
header_label.pack(pady=15)

# Input Frame with Shadow Effect
input_frame = tk.Frame(root, bg="#f0f4f8", bd=0)
input_frame.pack(pady=30)
label = tk.Label(input_frame, text="Enter a word:", font=("Helvetica Neue", 14), bg="#f0f4f8", fg="#333")
label.pack(side=tk.LEFT, padx=10)
entry = tk.Entry(input_frame, font=("Helvetica Neue", 14), width=25, bd=0, relief=tk.GROOVE, highlightthickness=2, highlightbackground="#6200ea", highlightcolor="#6200ea")
entry.insert(0, "Type a word...")
entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END))  # Clear placeholder text on focus
entry.pack(side=tk.LEFT, padx=10)

# Adding a Shadow Effect to Search Button
search_button = tk.Button(input_frame, text="Search", font=("Helvetica Neue", 14), bg="#6200ea", fg="white", relief=tk.FLAT, command=get_meaning)
search_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

# Adding a Shadow Effect to Clear Button
clear_button = tk.Button(input_frame, text="Clear", font=("Helvetica Neue", 14), bg="#ff4081", fg="white", relief=tk.FLAT, command=clear_results)
clear_button.pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

# Result Label with Gradient Background
result_label = tk.Label(root, text="Meaning:", font=("Helvetica Neue", 14, "bold"), bg="#f0f4f8", fg="#333")
result_label.pack(pady=10)

# Result Text Box with Rounded Corners and Drop Shadow Effect
result_frame = tk.Frame(root, bg="#f0f4f8", bd=0)
result_frame.pack(pady=5)
result_text = tk.Text(result_frame, font=("Helvetica Neue", 12), wrap=tk.WORD, height=12, width=70, bg="#ffffff", fg="#333", bd=0, relief=tk.GROOVE, highlightthickness=2, highlightbackground="#6200ea", highlightcolor="#6200ea")
result_text.pack(padx=10, pady=10)

# Footer Frame with Gradient Background
footer_frame = tk.Frame(root, bg="#6200ea", bd=0)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
footer_label = tk.Label(footer_frame, text="Developed By Rahul", font=("Helvetica Neue", 10), fg="white", bg="#6200ea")
footer_label.pack(pady=5)

# Hover effects for buttons with subtle transition
def on_enter(button):
    button.config(bg="#3700b3")

def on_leave(button):
    button.config(bg="#6200ea")

def on_clear_enter(button):
    button.config(bg="#c2185b")

def on_clear_leave(button):
    button.config(bg="#ff4081")

search_button.bind("<Enter>", lambda event, btn=search_button: on_enter(btn))
search_button.bind("<Leave>", lambda event, btn=search_button: on_leave(btn))
clear_button.bind("<Enter>", lambda event, btn=clear_button: on_clear_enter(btn))
clear_button.bind("<Leave>", lambda event, btn=clear_button: on_clear_leave(btn))

# Start the GUI loop
root.mainloop()
