import tkinter as tk

# --- Window Setup ---
root = tk.Tk()
root.title("Dark Mode Calculator")
root.geometry("320x450")
root.config(bg="#0F172A")  # Dark background

# --- Entry Display ---
entry = tk.Entry(
    root,
    font=("Helvetica", 28, "bold"),
    justify="right",
    bg="#1E293B",
    fg="#F9FAFB",
    bd=0,
    relief="flat",
    highlightthickness=2,
    highlightbackground="#334155",
    highlightcolor="#3B82F6"
)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=20, padx=10)


# --- Button Function ---
def on_click(char):
    if char == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)


# --- Button Style Function ---
def make_button(parent, text, bg="#1E293B", fg="#E2E8F0", special=False):
    color = "#2563EB" if special else bg  # blue for special keys
    hover = "#3B82F6" if special else "#334155"
    button = tk.Button(
        parent,
        text=text,
        font=("Helvetica", 18, "bold"),
        bg=color,
        fg=fg,
        activebackground=hover,
        activeforeground=fg,
        bd=0,
        relief="flat",
        command=lambda x=text: on_click(x)
    )
    button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
    return button


# --- Button Layout ---
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root, bg="#0F172A")
    frame.pack(expand=True, fill="both", padx=10)
    for btn_text in row:
        special = btn_text in ["=", "+", "-", "*", "/", "C"]
        make_button(frame, btn_text, special=special)

# --- Run App ---
root.mainloop()


