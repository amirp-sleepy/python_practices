# 🐍 Python Practice Projects

Welcome to my collection of small Python projects! 🚀

I’m building these projects as part of my journey to learn and improve my Python programming skills. Each project focuses on practicing specific concepts and applying what I’ve learned through hands-on coding.

---

## 🎲 Project #1: Generating Random Quiz Files(GRQF)

The first project in this collection is **Generating Random Quiz Files**.

This program generates any desired number of quiz files, each containing **50 questions** arranged in a different random order. The questions focus on identifying the **capital cities of the U.S. states** 🇺🇸.

### 🎯 Learning Goals

The main purpose of creating this project was to become familiar with:

* ✍️ Writing data to files
* 📂 Opening and closing files using `open()` and `close()`
* 🎲 Using several methods from Python's `random` module
* 🔀 Generating quizzes with different question orders

This project was a great opportunity to practice file handling and randomness while building a practical and reusable Python program.

> 💡 **One small project at a time, one step closer to mastering Python!** 🐍✨

---

## 📋 Project #2: Multiclipboard (MCB)

The second project in this collection is **Multiclipboard**.

This program is designed to make working with multiple frequently used pieces of text much easier. Instead of repeatedly copying and pasting the same text, the program allows users to save different clipboard contents under custom keywords and retrieve them whenever needed.

For example, a piece of text can be saved under a keyword such as `spam` and later copied back to the clipboard simply by using that keyword. The program also provides a `list` command that copies all saved keywords to the clipboard, making it easy to remember the available shortcuts.

### 🎯 Learning Goals

The main purpose of creating this project was to become familiar with:

* 🖥️ Reading command-line arguments using `sys.argv`
* 📋 Reading from and writing to the system clipboard
* 💾 Saving and loading data using shelf files
* 🔑 Using keywords to organize and retrieve saved text
* ⚙️ Building a practical command-line utility
* 🧩 Working with Python modules such as `sys`, `pyperclip`, and `shelve`

This project was a great opportunity to combine several Python concepts into a useful real-world tool while learning how programs can interact with the clipboard and store data for later use.

> 💡 **From simple scripts to practical tools — every project is another step toward becoming a better Python programmer!** 🐍✨

---

## 🗂️ Project #3: Renaming Files with American-Style Dates to European-Style Dates (RD)

The third project in this collection is **Renaming Files with American-Style Dates to European-Style Dates**.

This program is designed to automate a repetitive file-renaming task. It scans the filenames in the current working directory, looks for names that contain dates in the **American format** `MM-DD-YYYY`, and renames them so the date appears in the **European format** `DD-MM-YYYY`.

For example, a file named `report-03-15-2024.txt` would be renamed to `report-15-03-2024.txt`.

### 🎯 Learning Goals

The main purpose of creating this project was to become familiar with:

* 🔍 Using regular expressions to detect patterns in filenames
* 📂 Listing files in the current working directory with `os.listdir()`
* 🔁 Looping through files and checking whether they match a pattern
* ✍️ Renaming files with `shutil.move()`
* 🧠 Working with capture groups in regex to rearrange text
* ⚙️ Automating a boring but practical real-world task

This project was a great exercise in combining file handling, regular expressions, and automation to solve a problem that would be tedious to do manually.

> 💡 **A few lines of code can save hours of repetitive work.** 🐍✨

---

## 🗜️ Project #4: Backing Up a Folder into a ZIP File (BTZ)

The fourth project in this collection is **Backing Up a Folder into a ZIP File**.

This program creates compressed backup snapshots of an entire folder and all of its contents. Each time the program is run, it automatically creates a new ZIP file with an incrementing number.

For example:

```text
Project_1.zip
Project_2.zip
Project_3.zip
```

This makes it possible to keep multiple versions of a project without manually choosing backup filenames or accidentally overwriting an existing backup.

The program allows the user to enter the path of the folder they want to back up and optionally choose where the ZIP file should be saved. If no backup path is provided, the backup is created in the current working directory.

### 🎯 Learning Goals

The main purpose of creating this project was to become familiar with:

* 🗜️ Creating ZIP archives using Python's `zipfile` module
* 📁 Recursively traversing folders and subfolders with `os.walk()`
* 🔢 Automatically generating incrementing backup filenames
* 🧭 Working with absolute and relative paths
* 🛠️ Using `os.path.basename()`, `os.path.normpath()`, and `os.path.join()`
* 📦 Adding files and folders to a ZIP archive
* 🚫 Excluding previously created backup ZIP files from new backups
* 💾 Creating compressed archives using `ZIP_DEFLATED`
* ⌨️ Getting user input to make the program more flexible

This project was a great opportunity to combine file-system navigation, path manipulation, ZIP file creation, and automation into a practical backup utility.

> 💡 **Automating backups means protecting your work with just a few lines of code.** 🐍🗜️✨

---

## 🔍Project #5: Google Search (lucky)

This project is a simple Python program designed to search Google from the command line and open the first five search results in separate browser tabs.

**Note:**
This program does **not currently work with Google's current search page structure**. Google has changed the way search results are delivered, so the HTML received by `requests` no longer contains the search results in the format expected by this project.

The project was still completed for learning purposes. The goal was to practice and understand concepts such as:

* Using `sys.argv` to receive command-line arguments
* Sending HTTP requests with `requests`
* Working with HTTP headers
* Parsing HTML with `BeautifulSoup`
* Selecting HTML elements with CSS selectors
* Extracting links from HTML
* Using `webbrowser` to open URLs
* Combining multiple Python modules into a small practical program

Therefore, although the program is not functional with Google's current implementation, it successfully served its purpose as a learning exercise.
