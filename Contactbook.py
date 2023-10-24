import tkinter as tk
from tkinter import messagebox


class ContactList:
    def __init__(self, Name, Phone, Email, Address):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email
        self.Address = Address


class Contact:
    def __init__(self, root):
        self.root = root
        self.root.title("CONTACT BOOK")
        self.contacts = []
        self.Layout()

    def Layout(self):
        # TEXT-FIELDS
        self.NameLabel = tk.Label(root, text="NAME : ")
        self.NameField = tk.Entry(root)
        self.NameLabel.grid(row=0, column=0)
        self.NameField.grid(row=0, column=2)

        self.PhoneLabel = tk.Label(root, text="PHONE : ")
        self.PhoneField = tk.Entry(root)
        self.PhoneLabel.grid(row=1, column=0)
        self.PhoneField.grid(row=1, column=2)

        self.EmailLabel = tk.Label(root, text="EMAIL : ")
        self.EmailField = tk.Entry(root)
        self.EmailLabel.grid(row=2, column=0)
        self.EmailField.grid(row=2, column=2)

        self.AddressLabel = tk.Label(root, text="ADDRESS : ")
        self.AddressField = tk.Entry(root)
        self.AddressLabel.grid(row=3, column=0)
        self.AddressField.grid(row=3, column=2)

        Empty = tk.Label(root, text="")
        Empty.grid(row=6, column=3)

        #  BUTTONS
        self.AddButton = tk.Button(root, text="ADD CONTACT", command=self.Add, bg="blue", fg="white")
        self.AddButton.grid(row=0, column=4)

        self.ViewButton = tk.Button(root, text="VIEW CONTACT", command=self.View, bg="blue", fg="white")
        self.ViewButton.grid(row=1, column=4)

        self.SearchButton = tk.Button(root, text="SEARCH CONTACT", command=self.Search, bg="blue", fg="white")
        self.SearchButton.grid(row=0, column=6)

        self.UpdateButton = tk.Button(root, text="UPDATE CONTACT", command=self.Update, bg="blue", fg="white")
        self.UpdateButton.grid(row=1, column=6)

        self.DeleteButton = tk.Button(root, text="DELETE CONTACT", command=self.Delete, bg="blue", fg="white")
        self.DeleteButton.grid(row=3, column=5)

    def Add(self):
        Name = self.NameField.get()
        Phone = self.PhoneField.get()
        Email = self.EmailField.get()
        Address = self.AddressField.get()
        contact = ContactList(Name, Phone, Email, Address)
        self.contacts.append(contact)
        self.Clear()
        messagebox.showinfo("Message", ">>CONTACT ADDED<<")

    def View(self):
        if not self.contacts:
            messagebox.showinfo("ERROR", ">>NOT CONTACT IN LIST<<")
        else:
            list = "CONTACT LIST :: \n"
            for contact in self.contacts:
                list += f"Name : {contact.Name}  Phone:{contact.Phone}\n"

        messagebox.showinfo("Contacts : ", list)

    def Search(self):
        Name = self.NameField.get()
        found = []
        for contact in self.contacts:
            if Name in contact.Name:
                found.append(contact)
        if found:
            list = "Searched Contacts \n "
            for contact in found:
                list += f"Name : {contact.Name}  Phone:{contact.Phone}\n"
        else:
            messagebox.showinfo("ERROR", ">>NOT FOUND<<")

    def Update(self):
        Email = self.EmailField.get()
        found = None
        for contact in self.contacts:
            if Email in contact.Email:
                found = contact
                break

        if found:
            Name = self.NameField.get()
            Phone = self.PhoneField.get()
            Email = self.EmailField.get()
            Address = self.AddressField.get()

            found.Name = Name
            found.Phone = Phone
            found.Email = Email
            found.Address = Address

            self.Clear()
            messagebox.showinfo("Message", ">>CONTACT UPDATED<<")
        else:
            messagebox.showinfo("ERROR", ">>NOT FOUND<<")

    def Delete(self):
        Email = self.EmailField.get()
        found = None

        for contact in self.contacts:
            if Email in contact.Email:
                found = contact
                break

        if found:
            self.contacts.remove(found)
            self.Clear()
            messagebox.showinfo("Message", ">>CONTACT    DELETED<<")
        else:
            messagebox.showinfo("ERROR", ">>NOT FOUND<<")

    def Clear(self):
        self.NameField.delete(0, tk.END)
        self.PhoneField.delete(0, tk.END)
        self.EmailField.delete(0, tk.END)
        self.AddressField.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Contact(root)
    root.geometry("530x200")
    root.mainloop()