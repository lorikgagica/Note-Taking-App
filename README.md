# 📝 Note-Taking App

A simple Python console app to let you create, view, and modify notes with timestamps. All your notes are automatically saved and reloaded when you restart the app!

---

## ✨ Features

- **Add notes** with automatic timestamps
- **View all notes** with their creation or last modification time
- **Modify any note** (timestamp updates to show when it was changed)
- **Delete all notes** in one command (with confirmation)
- **Persistent storage:**  
  All notes are saved automatically to `myNotes.txt` and loaded whenever the app starts

---

## 🚀 How to Use

1. Make sure Python is installed.
2. Save your script as `note.py`.
3. Open your terminal or command prompt and navigate to the script location.
4. Launch the app:`python note.py`
5. Use the on-screen menu to manage your notes.

---

## 💡 Sample Interaction

--- Note-Taking App Menu ---

1. Add a new note
2. View all notes
3. Modify a note
4. Delete all notes
5. Exit
Enter your choice (1-5): 1
Enter your note: Buy groceries
Note added successfully!

--- Note-Taking App Menu ---
2
--- Your Notes ---

[2025-10-30 15:10:45] Buy groceries
...

---

## 🔒 Data Storage

- All notes are saved in a plain text file called `myNotes.txt`, with each note’s timestamp.
- The file is read on startup, so you’ll always see your saved notes.

---

## 📄 License

MIT License — free to use, extend, and share!

---

Get organized and happy noting!
