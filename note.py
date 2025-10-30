# Note-Taking App
import os
from datetime import datetime

# Step 1: Define file name
FILE_NAME = "myNotes.txt"

# Helper to load notes (returns list of dicts)
def load_notes():
    notes = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if "|" in line:
                    timestamp, note = line.rstrip().split("|", 1)
                    notes.append({"timestamp": timestamp, "note": note})
    return notes

# Step 2: Display menu options
def show_menu():
    print("\n--- Note-Taking App Menu ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Modify a note")
    print("4. Delete all notes")
    print("5. Exit")

# Step 3: Add a new note
def add_note():
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}|{note}\n")
    print("Note added successfully!")

# Step 4: View all notes
def view_notes():
    notes = load_notes()
    if notes:
        print("\n--- Your Notes ---")
        for idx, entry in enumerate(notes, 1):
            print(f"{idx}. [{entry['timestamp']}] {entry['note']}")
    else:
        print("\nNo notes found.")

# Step 5: Modify notes
def modify_note():
    notes = load_notes()
    if not notes:
        print("\nNo notes to modify.")
        return
    view_notes()
    try:
        num = int(input("Enter the number of the note to modify: "))
        if 1 <= num <= len(notes):
            new_note = input("Enter the new note: ")
            notes[num - 1]["note"] = new_note
            # update the timestamp for modification
            notes[num - 1]["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                for entry in notes:
                    file.write(f"{entry['timestamp']}|{entry['note']}\n")
            print("Note modified successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

# Step 6: Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/n): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            pass
        print("All notes have been deleted.")
    else:
        print("Deletion cancelled.")

# Step 6: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        modify_note()
    elif choice == "4":
        delete_notes()
    elif choice == "5":
        print("Exiting Note-Taking App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
