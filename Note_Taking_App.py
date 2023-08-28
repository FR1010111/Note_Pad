import os
import datetime

class NoteTakingApp:
    def __init__(self):
        self.notes = []
        self.notes_directory = "notes"

        if not os.path.exists(self.notes_directory):
            os.makedirs(self.notes_directory)

    def create_note(self):
        note_text = input("Enter your note: ")
        timestamp = datetime.datetime.now()
        note_filename = f"{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

        note_path = os.path.join(self.notes_directory, note_filename)

        with open(note_path, "w") as f:
            f.write(note_text)
        
        print("Note created!")

    def list_notes(self):
        print("Available notes:")
        for idx, note_filename in enumerate(os.listdir(self.notes_directory)):
            print(f"{idx + 1}. {note_filename}")

    def read_note(self, note_number):
        try:
            note_filename = os.listdir(self.notes_directory)[note_number - 1]
            note_path = os.path.join(self.notes_directory, note_filename)
            with open(note_path, "r") as f:
                note_content = f.read()
                print(f"Note content:\n{note_content}")
        except IndexError:
            print("Note not found.")

if __name__ == "__main__":
    app = NoteTakingApp()

    while True:
        print("\nMenu:")
        print("1. Create a new note")
        print("2. List available notes")
        print("3. Read a note")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            app.create_note()
        elif choice == "2":
            app.list_notes()
        elif choice == "3":
            app.list_notes()
            note_number = int(input("Enter the number of the note you want to read: "))
            app.read_note(note_number)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")


#FN1010111