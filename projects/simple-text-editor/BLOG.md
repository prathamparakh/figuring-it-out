# Building a Simple Text Editor in Python

## Why I Built This

I wanted to understand how a text editor works internally rather than simply using an existing application.

The goal of this project is to build a minimal text editor using Python that can:

- Create a new document
- Open a text file
- Save a text file
- Save a document under a new name
- Export the document as a PDF
- Wrap long lines
- Create multiple PDF pages
- Protect unsaved work

The application will use:

- Python
- Tkinter
- ReportLab

## What I Want to Learn

This project is not just about building a text editor. It is an exercise in understanding:

- Python modules and imports
- Object-oriented programming
- Classes and objects
- GUI programming
- Event-driven programming
- File handling
- Paths and file systems
- External Python packages
- PDF generation
- Text measurement
- Line wrapping
- Pagination
- Error handling
- Git and GitHub

---

# 1. Project Setup

## 1.1 Virtual Environments

Python allows functionality to be separated into modules and reused through imports.

This project uses both Python's standard library and an external package.

The standard library provides functionality such as:

- Tkinter for the graphical interface
- `filedialog` for file-selection dialogs
- `messagebox` for displaying messages
- `pathlib` for working with filesystem paths

The project also uses ReportLab, which is an external package for generating PDF files.

This distinction is important. Not everything imported by a Python program needs to be installed using `pip`. Modules that are part of Python's standard library are already available with the Python installation, while third-party packages normally need to be installed separately.

### Import styles

There are different ways to import functionality.

For example:

```python
import tkinter as tk

## 1.2 Dependencies

## 1.3 `.gitignore`

# 2. Python Fundamentals

## 2.1 Imports

## 2.2 Classes and Objects

## 2.3 Methods

## 2.4 `self`

## 2.5 Static Methods

# 3. Building the GUI

## 3.1 Tkinter

## 3.2 The Root Window

## 3.3 Widgets

## 3.4 Menus

## 3.5 Event Handling

# 4. File Operations

## 4.1 Reading Files

## 4.2 Writing Files

## 4.3 File Paths

## 4.4 Encoding

# 5. PDF Generation

## 5.1 ReportLab

## 5.2 PDF Coordinates

## 5.3 Margins

## 5.4 Line Wrapping

## 5.5 Pagination

# 6. Error Handling

# 7. Testing

# 8. What I Learned

# 9. What I Would Improve