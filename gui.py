import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from sample_data import insert_sample_data

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1200x700")
        self.db = Database()
        
        # Insert sample data if database is empty
        if not self.db.get_all_students():
            insert_sample_data(self.db)
        
        self.create_main_page()
        
    def create_main_page(self):
        # Search Frame
        search_frame = ttk.LabelFrame(self.root, text="Search", padding="10")
        search_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(search_frame, text="Search:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_students).pack(side="left")
        ttk.Button(search_frame, text="Show All", command=self.refresh_table).pack(side="left", padx=5)
        
        # Student List
        list_frame = ttk.LabelFrame(self.root, text="Student List", padding="10")
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create Treeview
        columns = ("ID", "Name", "Age", "Gender", "Mobile", "Major", "GPA", "Attendance")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        
        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons Frame
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(btn_frame, text="Add Student", command=self.show_add_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Edit Student", command=self.show_edit_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete Student", command=self.delete_student).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="View Details", command=self.show_details_window).pack(side="left", padx=5)
        
        # Load initial data
        self.refresh_table()
        
    def refresh_table(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Load all students
        students = self.db.get_all_students()
        for student in students:
            self.tree.insert("", "end", values=(
                student['student_id'],
                student['name'],
                student['age'],
                student['gender'],
                student['mobile'],
                student['major'],
                student['gpa'],
                f"{student['attendance']}%"
            ))
    
    def search_students(self):
        query = self.search_var.get()
        if not query:
            self.refresh_table()
            return
            
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Load searched students
        students = self.db.search_students(query)
        for student in students:
            self.tree.insert("", "end", values=(
                student['student_id'],
                student['name'],
                student['age'],
                student['gender'],
                student['mobile'],
                student['major'],
                student['gpa'],
                f"{student['attendance']}%"
            ))
    
    def show_add_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Student")
        add_window.geometry("400x600")
        
        # Create form fields
        fields = {}
        for field in ['student_id', 'name', 'age', 'gender', 'mobile', 'address', 
                     'major', 'course', 'branch', 'gpa', 'attendance']:
            frame = ttk.Frame(add_window)
            frame.pack(fill="x", padx=10, pady=5)
            ttk.Label(frame, text=field.title() + ":").pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="right", expand=True)
            fields[field] = entry
        
        def save():
            data = {field: entry.get() for field, entry in fields.items()}
            if self.db.add_student(data):
                messagebox.showinfo("Success", "Student added successfully!")
                add_window.destroy()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Failed to add student!")
        
        ttk.Button(add_window, text="Save", command=save).pack(pady=10)
    
    def show_edit_window(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to edit!")
            return
            
        student_id = self.tree.item(selected[0])['values'][0]
        student = self.db.get_student(student_id)
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Student")
        edit_window.geometry("400x600")
        
        # Create form fields
        fields = {}
        for field in ['name', 'age', 'gender', 'mobile', 'address', 
                     'major', 'course', 'branch', 'gpa', 'attendance']:
            frame = ttk.Frame(edit_window)
            frame.pack(fill="x", padx=10, pady=5)
            ttk.Label(frame, text=field.title() + ":").pack(side="left")
            entry = ttk.Entry(frame)
            entry.insert(0, str(student[field]))
            entry.pack(side="right", expand=True)
            fields[field] = entry
        
        def save():
            data = {field: entry.get() for field, entry in fields.items()}
            if self.db.update_student(student_id, data):
                messagebox.showinfo("Success", "Student updated successfully!")
                edit_window.destroy()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Failed to update student!")
        
        ttk.Button(edit_window, text="Save", command=save).pack(pady=10)
    
    def delete_student(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to delete!")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            student_id = self.tree.item(selected[0])['values'][0]
            if self.db.delete_student(student_id):
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Failed to delete student!")
    
    def show_details_window(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a student to view!")
            return
            
        student_id = self.tree.item(selected[0])['values'][0]
        student = self.db.get_student(student_id)
        
        details_window = tk.Toplevel(self.root)
        details_window.title("Student Details")
        details_window.geometry("400x600")
        
        # Create labels for all fields
        for field, value in student.items():
            frame = ttk.Frame(details_window)
            frame.pack(fill="x", padx=10, pady=5)
            ttk.Label(frame, text=field.title() + ":", width=15).pack(side="left")
            ttk.Label(frame, text=str(value)).pack(side="left")