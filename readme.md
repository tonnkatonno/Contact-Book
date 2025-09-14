# Python Project: Simple Contact Book

## [span_4](start_span)Hallgató (Student)[span_4](end_span)
Bernscherer Antal

## [span_5](start_span)Feladat leírása (Project Description)[span_5](end_span)
This is a simple graphical contact book application created for the "Szkript nyelvek Python" course. The program allows the user to enter a name, phone number, and email address. These contacts can be added to a list displayed on the screen. The user also has the option to save the entire contact list to a `contacts.csv` file. The project adheres to all mandatory requirements, including the use of custom modules, classes, functions, and a graphical interface.

## [span_6](start_span)Modulok és a modulokban használt függvények (Modules and Functions Used)[span_6](end_span)

* **Tanult modul (Learned module): `csv`**
    * `csv.writer()`: Creates a writer object to convert user data into delimited strings.
    * `writer.writerow()`: Writes a single row to the CSV file.
    * `writer.writerows()`: Can be used to write multiple rows.

* **Bemutatandó modul (Demonstrated module): `tkinter.messagebox`**
    * `messagebox.showwarning()`: Displays a warning message box.
    * `messagebox.showinfo()`: Displays an informational message box.
    * `messagebox.askyesno()`: Displays a message box with "Yes" and "No" buttons and returns a boolean.

* **Saját modul (Custom module): `contact_module_BA`**
    * `format_contact_for_display_BA()`: A custom function to format contact details for display.

## [span_7](start_span)Osztály(ok) (Class(es))[span_7](end_span)

* **`contact_module_BA.Contact_BA`**: A custom class representing a contact, containing attributes for name, phone, and email. The class name includes the student's monogram.

