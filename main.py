import sqlite3
from faker import Faker
import random

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних SQLite3
conn = sqlite3.connect('university.db')
cur = conn.cursor()

# Створюємо таблиці
cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id)
                )''')

# Функція для додавання студентів
def add_students(num_students):
    for _ in range(num_students):
        name = fake.name()
        group_id = random.randint(1, 3)  # Випадково вибираємо групу
        cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

# Функція для додавання груп
def add_groups():
    groups = ['Group A', 'Group B', 'Group C']
    for name in groups:
        cur.execute("INSERT INTO groups (name) VALUES (?)", (name,))

# Функція для додавання викладачів
def add_teachers(num_teachers):
    for _ in range(num_teachers):
        name = fake.name()
        cur.execute("INSERT INTO teachers (name) VALUES (?)", (name,))

# Функція для додавання предметів
def add_subjects(num_subjects):
    for _ in range(num_subjects):
        name = fake.word() + " " + fake.word()
        teacher_id = random.randint(1, 5)  # Випадково вибираємо викладача
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (name, teacher_id))

# Функція для додавання оцінок
def add_grades(num_grades):
    for _ in range(num_grades):
        student_id = random.randint(1, 50)  # Ідентифікатори студентів від 1 до 50
        subject_id = random.randint(1, 8)   # Ідентифікатори предметів від 1 до 8
        grade = random.randint(1, 100)      # Випадкова оцінка від 1 до 100
        date = fake.date_this_year()         # Випадкова дата у поточному році
        cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, grade, date))

# Додаємо дані
add_groups()
add_students(50)
add_teachers(5)
add_subjects(8)
add_grades(100)

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
conn.close()

print("База даних створена та заповнена випадковими даними.")
