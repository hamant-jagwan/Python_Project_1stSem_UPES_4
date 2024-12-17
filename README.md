# Personal Diary Application

This project involves developing a personal diary application where users can write and save daily entries. The application uses the `tkinter` library for the graphical user interface (GUI).

## Screenshot

![alt text](<Screenshot 2024-12-17 203543.png>)

## Features

- Write daily diary entries in a multi-line text widget
- Save diary entries to a text file
- Clear the text widget for new entries

## Requirements

- Python 3.x
- `tkinter` library (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hamant-jagwan/Python_Project_1stSem_UPES_4/blob/main/Personal_Diary.py
    ```

2. Navigate to the project directory:
    ```sh
    cd personal-diary-app
    ```

## Usage

1. Run the Python script:
    ```sh
    python diary.py
    ```

2. The personal diary GUI will appear, allowing you to write and save daily entries.

## Project Structure

- `diary.py`: Main script containing the code for the diary application.

## Code Overview

1. **Importing Necessary Libraries:**
   The script starts by importing the `tkinter` library for creating the GUI.

2. **Setting Up the Main Window:**
   The main application window is initialized using `tkinter.Tk()`, and the title and size are set.

3. **Creating Text Widget:**
   A multi-line text widget is created using `tkinter.Text()` for diary entries.

4. **Creating Buttons:**
   Buttons for saving and clearing the text widget are created using `tkinter.Button()`.

5. **Defining Button Functions:**
   - `save_entry()`: Opens a file dialog to save the text from the text widget to a file and shows a success message.
   - `clear_text()`: Clears the text from the text widget.

6. **Running the Application:**
   The `mainloop()` method is used to start the application, displaying the diary GUI.

## Example Code
Here's a high-level overview of the steps involved in the script:

1. **Import Libraries**
2. **Set Up Main Window**
3. **Create Text Widget**
4. **Create Buttons**
5. **Define Button Functions**
6. **Run the Application**


