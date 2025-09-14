class Contact_BA:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

def format_contact_for_display_BA(contact):

    return f"Contact: {contact.name} | {contact.phone} | {contact.email}"