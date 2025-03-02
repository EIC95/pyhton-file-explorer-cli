# Command Line File Explorer

## Description

This project is an **interactive file explorer (TUI - Text User Interface)** that allows users to navigate, copy, move, rename, and delete files and directories directly from a terminal. It provides an intuitive interface for managing files without relying on a graphical file explorer.

## Features

- **Smooth navigation** between directories.
- **Displays essential file information** (name, type, size, modification date).
- **File operations** (copy, paste, delete, move, rename).
- **Sort files** by type, date, or size.
- **Interactive interface** with keyboard shortcuts.

## Technologies Used

This project is developed in **Python**, using the following modules:

- `os` and `shutil` → File and directory management.
- `pathlib` → Path handling.
- `ctypes` → Display system messages on Windows.
- `keyboard` → Real-time keyboard input handling.
- `datetime` → Formatting file modification dates.

## Installation

### Prerequisites
- Python 3.6+
- `pip` installed

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

Run the program with:
```sh
python main.py
```

The file explorer will open, displaying the current directory's files. You can navigate using keyboard shortcuts.

## Project Architecture

The project is structured into several modules:

- **`main.py`** → Entry point of the program.
- **`navigations.py`** → Manages directory navigation.
- **`affichage.py`** → Displays files and information.
- **`actions.py`** → Handles file operations (copy, delete, etc.).

## Compatibility

This program works on **Windows, macOS, and Linux**.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
