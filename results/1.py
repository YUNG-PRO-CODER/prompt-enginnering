import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, course TEXT)''')
    conn.commit()
    conn.close()

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    course = course_entry.get()
    if name and age and gender and course:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, gender, course) VALUES (?, ?, ?, ?)", (name, age, gender, course))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def update_student():
    student_id = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    course = course_entry.get()
    if student_id and name and age and gender and course:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name=?, age=?, gender=?, course=? WHERE id=?", (name, age, gender, course, student_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student updated successfully")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def delete_student():
    student_id = id_entry.get()
    if student_id:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student deleted successfully")
        clear_fields()
        display_students()
    else:
        messagebox.showwarning("Input Error", "Please enter student ID")

def display_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    student_list.delete(0, tk.END)
    for row in rows:
        student_list.insert(tk.END, row)
    conn.close()

def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    gender_var.set("")

create_db()

root = tk.Tk()
root.title("Student Management System")

id_label = tk.Label(root, text="Student ID")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

age_label = tk.Label(root, text="Age")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

gender_label = tk.Label(root, text="Gender")
gender_label.grid(row=3, column=0)
gender_var = tk.StringVar()
male_rb = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_rb.grid(row=3, column=1)
female_rb = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_rb.grid(row=3, column=2)

course_label = tk.Label(root, text="Course")
course_label.grid(row=4, column=0)
course_entry = tk.Entry(root)
course_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=5, column=0)

update_button = tk.Button(root, text="Update Student", command=update_student)
update_button.grid(row=5, column=1)

delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.grid(row=5, column=2)

clear_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_button.grid(row=5, column=3)

student_list = tk.Listbox(root, width=50, height=15)
student_list.grid(row=6, column=0, columnspan=4)

display_students()

root.mainloop()
