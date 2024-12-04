import sqlite3
from typing import List, Dict, Optional

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('student_db.sqlite')
        self.create_tables()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Create Students table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            mobile TEXT,
            address TEXT
        )
        ''')
        
        # Create Academic Info table with foreign key
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS academic_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            major TEXT,
            course TEXT,
            branch TEXT,
            gpa REAL,
            attendance REAL,
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
        ''')
        
        self.conn.commit()
    
    def add_student(self, data: Dict) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # Insert into students table
            cursor.execute('''
            INSERT INTO students (student_id, name, age, gender, mobile, address)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (data['student_id'], data['name'], data['age'], 
                 data['gender'], data['mobile'], data['address']))
            
            # Insert into academic_info table
            cursor.execute('''
            INSERT INTO academic_info (student_id, major, course, branch, gpa, attendance)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (data['student_id'], data['major'], data['course'],
                 data['branch'], data['gpa'], data['attendance']))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False
    
    def get_student(self, student_id: str) -> Optional[Dict]:
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT s.*, a.major, a.course, a.branch, a.gpa, a.attendance
        FROM students s
        LEFT JOIN academic_info a ON s.student_id = a.student_id
        WHERE s.student_id = ?
        ''', (student_id,))
        
        result = cursor.fetchone()
        if result:
            return {
                'student_id': result[0],
                'name': result[1],
                'age': result[2],
                'gender': result[3],
                'mobile': result[4],
                'address': result[5],
                'major': result[6],
                'course': result[7],
                'branch': result[8],
                'gpa': result[9],
                'attendance': result[10]
            }
        return None
    
    def get_all_students(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT s.*, a.major, a.course, a.branch, a.gpa, a.attendance
        FROM students s
        LEFT JOIN academic_info a ON s.student_id = a.student_id
        ''')
        
        students = []
        for row in cursor.fetchall():
            students.append({
                'student_id': row[0],
                'name': row[1],
                'age': row[2],
                'gender': row[3],
                'mobile': row[4],
                'address': row[5],
                'major': row[6],
                'course': row[7],
                'branch': row[8],
                'gpa': row[9],
                'attendance': row[10]
            })
        return students
    
    def update_student(self, student_id: str, data: Dict) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # Update students table
            cursor.execute('''
            UPDATE students 
            SET name=?, age=?, gender=?, mobile=?, address=?
            WHERE student_id=?
            ''', (data['name'], data['age'], data['gender'],
                 data['mobile'], data['address'], student_id))
            
            # Update academic_info table
            cursor.execute('''
            UPDATE academic_info 
            SET major=?, course=?, branch=?, gpa=?, attendance=?
            WHERE student_id=?
            ''', (data['major'], data['course'], data['branch'],
                 data['gpa'], data['attendance'], student_id))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating student: {e}")
            return False
    
    def delete_student(self, student_id: str) -> bool:
        try:
            cursor = self.conn.cursor()
            
            # Delete from academic_info first due to foreign key constraint
            cursor.execute('DELETE FROM academic_info WHERE student_id=?', (student_id,))
            cursor.execute('DELETE FROM students WHERE student_id=?', (student_id,))
            
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False
    
    def search_students(self, query: str) -> List[Dict]:
        cursor = self.conn.cursor()
        search = f"%{query}%"
        cursor.execute('''
        SELECT s.*, a.major, a.course, a.branch, a.gpa, a.attendance
        FROM students s
        LEFT JOIN academic_info a ON s.student_id = a.student_id
        WHERE s.name LIKE ? OR s.student_id LIKE ?
        ''', (search, search))
        
        students = []
        for row in cursor.fetchall():
            students.append({
                'student_id': row[0],
                'name': row[1],
                'age': row[2],
                'gender': row[3],
                'mobile': row[4],
                'address': row[5],
                'major': row[6],
                'course': row[7],
                'branch': row[8],
                'gpa': row[9],
                'attendance': row[10]
            })
        return students