import tkinter as tk

# Predefined list of medicine names
medicine_list = ["Paracetamol", "Aspirin", "Ibuprofen", "Asoxicillin", "Lisinopril", "Metformin", "Atorvastatin", "Levothyroxine"]

def on_entry_change(event):
    search_term = medicine_entry.get().lower()
    if search_term:
        relevant_medicines = [medicine for medicine in medicine_list if medicine.lower().startswith(search_term)]
        update_medicine_display(relevant_medicines)
    else:
        clear_medicine_display()

def update_medicine_display(relevant_medicines):
    clear_medicine_display()
    medicine_display.config(text='\n'.join(relevant_medicines))
    for i, medicine in enumerate(relevant_medicines):
        label = tk.Label(medicine_display, text=medicine, fg="blue", cursor="hand2")
        label.grid(row=i, column=0, sticky="w")
        label.bind("<Button-1>", lambda event, med=medicine: select_medicine(med))

def clear_medicine_display():
    medicine_display.config(text="")
    for widget in medicine_display.winfo_children():
        widget.destroy()

def select_medicine(medicine):
    medicine_entry.delete(0, tk.END)
    medicine_entry.insert(tk.END, medicine)
    clear_medicine_display()

# Create Tkinter window
root = tk.Tk()
root.title("Medicine Search")

# Create entry widget for medicine name
medicine_label = tk.Label(root, text="Medicine:")
medicine_label.grid(row=0, column=0)
medicine_entry = tk.Entry(root)
medicine_entry.grid(row=0, column=1)

# Create frame to hold medicine display labels
medicine_display_frame = tk.Frame(root)
medicine_display_frame.grid(row=1, column=0, columnspan=2)

# Create label to display relevant medicine names
medicine_display = tk.Label(medicine_display_frame, text="", justify="left")
medicine_display.grid(row=0, column=0)

# Bind entry widget to detect text changes
medicine_entry.bind("<KeyRelease>", on_entry_change)

# Run Tkinter event loop
root.mainloop()
