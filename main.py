import tkinter as tk
from tkinter import messagebox
import csv
from contact_module_BA import Contact_BA, format_contact_for_display_BA

root = tk.Tk()
root.title("Simple Contact Book - Bernscherer Antal")
root.geometry("500x500")

contacts = []
app_name = "ContactBookApp"

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone and email:
        new_contact = Contact_BA(name, phone, email)
        contacts.append(new_contact)
        update_contact_listbox()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")
        messagebox.showinfo("Info", "Please fill in all contact details.")
        if not messagebox.askyesno("Question", "Do you want to try again?"):
            root.destroy()

def update_contact_listbox():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        display_text = format_contact_for_display_BA(contact)
        listbox_contacts.insert(tk.END, display_text)

def save_contacts_to_file():
    with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email'])
        for contact in contacts:
            writer.writerow([contact.name, contact.phone, contact.email])
    messagebox.showinfo("Success", "Contacts have been saved to contacts.csv")

frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame_input, text="Phone:").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(frame_input, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(frame_input, text="Email:").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_input, width=30)
entry_email.grid(row=2, column=1, pady=5)

add_button = tk.Button(frame_input, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

save_button = tk.Button(frame_input, text="Save to File", command=save_contacts_to_file)
save_button.grid(row=4, column=0, columnspan=2)

frame_display = tk.Frame(root, padx=10, pady=10)
frame_display.pack()

tk.Label(frame_display, text="Contact List:").pack()
listbox_contacts = tk.Listbox(frame_display, width=60, height=15)
listbox_contacts.pack()

root.mainloop()