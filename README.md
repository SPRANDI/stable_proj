🚀 QuickEdit – Simple Console File Manager

QuickEdit is a lightweight, menu‑driven console utility written in pure Python. It lets you create, edit (overwrite or append), view, and delete text files directly from your terminal. The tool features a colorful animated banner that adds a touch of style to your command‑line experience.

⚠️ Note: This script was created for learning purposes. It intentionally lacks some safety checks – use it with care (see Notes).

✨ Features
📄 Create a new text file (⚠️ overwrites existing files without warning)

✏️ Edit a file – choose to overwrite completely or append new content

👀 View the contents of any text file

🗑️ Delete a file

🎨 Colorful banner with a smooth “scanning” animation (ANSI escape codes)

⌨️ Simple numeric menu for easy navigation

📦 Requirements
Python 3.6 or higher

No external dependencies – only standard library modules (os, sys, time)

🔧 Installation
Clone the repository (or download the script directly):

bash
git clone https://github.com/yourusername/quickedit.git
cd quickedit
Make the script executable (optional on Linux/macOS):

bash
chmod +x quickedit.py
Run it:

bash
python quickedit.py
🖥️ Usage
When you start the script, you’ll see the animated banner and the main menu:

text
 1. Create file
 2. Edit file
 3. View the file
 4. Delete file
 5. Exit
 >>> 
Just type the number of your choice and follow the prompts.

Create file – you will be asked for a file name and its content.

Edit file – you can either overwrite the whole file or append new lines to the end.

View file – displays the file’s content in the terminal.

Delete file – permanently removes the file after confirmation.

📸 Example
text
$ python quickedit.py
<img width="514" height="133" alt="image" src="https://github.com/user-attachments/assets/fda58053-4bb1-4a4d-b647-fc4d5a4ad80b" />


 1. Create file
 2. Edit file
 3. View the file
 4. Delete file
 5. Exit
 >>> 
📝 Notes / Known Limitations
No existence checks – If you try to read or delete a non‑existent file, the script will crash with an error.

Silent overwrite – Creating a new file with a name that already exists will overwrite it without any warning.

Minimal error handling – Unexpected input or filesystem issues (permissions, invalid paths) may cause abrupt termination.

Path handling – Relative paths are resolved from the current working directory; if the parent directory does not exist, file operations will fail.

ANSI colors – The banner animation uses ANSI escape codes. It works best in Linux, macOS, and Windows 10+ terminals with VT100 emulation enabled.

Educational purpose – This code is intentionally kept simple and is not intended for production use.

Feel free to fork and improve it!
