import tkinter as tk
from tkinter import scrolledtext

def generate_prompt():
    # Eingaben aus den Textboxen abrufen
    system_prompt = system_text.get("1.0", "end-1c").strip()
    user_prompt = user_text.get("1.0", "end-1c").strip()
    
    # Kombinierten Prompt erzeugen. Hier wird ein Format gewählt, das ChatGPT optimal instruieren kann.
    final_prompt = f"System: {system_prompt}\n\nUser: {user_prompt}"
    
    # Ausgabe-Textbox aktualisieren
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, final_prompt)
    output_text.config(state='disabled')

# Hauptfenster initialisieren
root = tk.Tk()
root.title("ChatGPT Prompt Generator")
root.geometry("600x500")

# Beschriftung und Textfeld für den System-Prompt
system_label = tk.Label(root, text="System Prompt:")
system_label.pack(pady=(10, 0))

system_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5)
system_text.pack(pady=(0, 10))

# Beschriftung und Textfeld für den normalen Prompt
user_label = tk.Label(root, text="User Prompt:")
user_label.pack(pady=(10, 0))

user_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5)
user_text.pack(pady=(0, 10))

# Button zum Erzeugen des kombinierten Prompts
generate_button = tk.Button(root, text="Prompt generieren", command=generate_prompt)
generate_button.pack(pady=10)

# Beschriftung und Textfeld für den kombinierten Prompt
output_label = tk.Label(root, text="Kombinierter Prompt:")
output_label.pack(pady=(10, 0))

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=7, state='disabled')
output_text.pack(pady=(0, 10))

# Hauptloop starten
root.mainloop()
