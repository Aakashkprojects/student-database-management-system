def insert_sample_data(db):
    sample_students = [
        {
            'student_id': 'S001',
            'name': 'John Smith',
            'age': 20,
            'gender': 'Male',
            'mobile': '123-456-7890',
            'address': '123 College St, City',
            'major': 'Computer Science',
            'course': 'Bachelor of Science',
            'branch': 'Software Engineering',
            'gpa': 3.8,
            'attendance': 95
        },
        {
            'student_id': 'S002',
            'name': 'Emma Johnson',
            'age': 19,
            'gender': 'Female',
            'mobile': '234-567-8901',
            'address': '456 University Ave, Town',
            'major': 'Mathematics',
            'course': 'Bachelor of Science',
            'branch': 'Pure Mathematics',
            'gpa': 3.9,
            'attendance': 98
        },
        {
            'student_id': 'S003',
            'name': 'Michael Brown',
            'age': 21,
            'gender': 'Male',
            'mobile': '345-678-9012',
            'address': '789 Campus Dr, City',
            'major': 'Physics',
            'course': 'Bachelor of Science',
            'branch': 'Theoretical Physics',
            'gpa': 3.7,
            'attendance': 92
        },
        {
            'student_id': 'S004',
            'name': 'Sarah Davis',
            'age': 20,
            'gender': 'Female',
            'mobile': '456-789-0123',
            'address': '321 Student Lane, Town',
            'major': 'Chemistry',
            'course': 'Bachelor of Science',
            'branch': 'Organic Chemistry',
            'gpa': 3.6,
            'attendance': 94
        },
        {
            'student_id': 'S005',
            'name': 'James Wilson',
            'age': 22,
            'gender': 'Male',
            'mobile': '567-890-1234',
            'address': '654 Education St, City',
            'major': 'Biology',
            'course': 'Bachelor of Science',
            'branch': 'Molecular Biology',
            'gpa': 3.5,
            'attendance': 90
        },
        {
            'student_id': 'S006',
            'name': 'Emily Taylor',
            'age': 19,
            'gender': 'Female',
            'mobile': '678-901-2345',
            'address': '987 Learning Ave, Town',
            'major': 'Computer Science',
            'course': 'Bachelor of Science',
            'branch': 'Artificial Intelligence',
            'gpa': 4.0,
            'attendance': 97
        },
        {
            'student_id': 'S007',
            'name': 'Daniel Anderson',
            'age': 21,
            'gender': 'Male',
            'mobile': '789-012-3456',
            'address': '147 Knowledge Dr, City',
            'major': 'Mathematics',
            'course': 'Bachelor of Science',
            'branch': 'Applied Mathematics',
            'gpa': 3.8,
            'attendance': 93
        },
        {
            'student_id': 'S008',
            'name': 'Olivia Martinez',
            'age': 20,
            'gender': 'Female',
            'mobile': '890-123-4567',
            'address': '258 Wisdom Lane, Town',
            'major': 'Physics',
            'course': 'Bachelor of Science',
            'branch': 'Applied Physics',
            'gpa': 3.7,
            'attendance': 96
        },
        {
            'student_id': 'S009',
            'name': 'William Thompson',
            'age': 22,
            'gender': 'Male',
            'mobile': '901-234-5678',
            'address': '369 Scholar St, City',
            'major': 'Chemistry',
            'course': 'Bachelor of Science',
            'branch': 'Physical Chemistry',
            'gpa': 3.9,
            'attendance': 91
        },
        {
            'student_id': 'S010',
            'name': 'Sophia Garcia',
            'age': 19,
            'gender': 'Female',
            'mobile': '012-345-6789',
            'address': '741 Academic Ave, Town',
            'major': 'Biology',
            'course': 'Bachelor of Science',
            'branch': 'Marine Biology',
            'gpa': 3.6,
            'attendance': 95
        }
    ]
    
    for student in sample_students:
        db.add_student(student)