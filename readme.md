# Python Projekt: Egyszerű Névjegykatalógus

## Hallgató
Bernscherer Antal

## Feladat leírása
Ez egy egyszerű, grafikus felületű névjegykatalógus alkalmazás, amely a "Szkript nyelvek Python" kurzusra készült. A program lehetővé teszi a felhasználó számára, hogy nevet, telefonszámot és e-mail címet rögzítsen. Ezek a névjegyek egy listában jelennek meg a képernyőn. A felhasználónak lehetősége van a teljes névjegylistát egy `contacts.csv` nevű fájlba menteni. A projekt megfelel minden kötelező követelménynek, beleértve a saját modul, osztály, függvény és a grafikus felület használatát.

## Modulok és a modulokban használt függvények

* **Tanult modul: `csv`**
    * `csv.writer()`: Egy író objektumot hoz létre, amely a felhasználói adatokat elválasztójelekkel tagolt szöveggé alakítja.
    * `writer.writerow()`: Egyetlen sort ír a CSV fájlba.

* **Bemutatandó modul: `tkinter.messagebox`**
    * `messagebox.showwarning()`: Egy figyelmeztető üzenetablakot jelenít meg.
    * `messagebox.showinfo()`: Egy tájékoztató üzenetablakot jelenít meg.
    * `messagebox.askyesno()`: Egy "Igen" és "Nem" gombokat tartalmazó üzenetablakot jelenít meg, és logikai (boolean) értéket ad vissza.

* **Saját modul: `contact_module_BA`**
    * `format_contact_for_display_BA()`: Egy saját függvény, amely a névjegy adatait formázza a listában való megjelenítéshez.

## Osztály(ok)

* **`contact_module_BA.Contact_BA`**: Egy saját osztály, amely egy névjegyet reprezentál. Attribútumai a név, telefonszám és e-mail cím. Az osztály neve tartalmazza a hallgató monogramját.