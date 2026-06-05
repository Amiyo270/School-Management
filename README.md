# School Management System (OOP Project)

A simple yet robust School Management System built in Python utilizing Object-Oriented Programming (OOP) concepts. The project simulates real-world academic functionalities such as student admissions, classroom mapping, teacher evaluation, automated examination grading, and GPA calculation.

## 🚀 Features

*   **School & Classroom Architecture:** Dynamic creation of schools and separate classrooms (e.g., Eight, Nine, Ten)[cite: 2, 4].
*   **Automatic ID Generation:** Automated unique Roll/ID generation for students upon joining a specific classroom (e.g., `Eight-1`, `Eight-2`)[cite: 1].
*   **Academic Subject Mapping:** Assigns dedicated teachers to specific subjects within individual classrooms[cite: 2, 5].
*   **Automated Examination System:** Simulates running semester final exams where teachers dynamically evaluate student performance with random marks allocation[cite: 1, 3, 5].
*   **Comprehensive Grading System:** 
    *   Converts numeric marks to letter grades ($A+$, $A$, $A-$, etc.).
    *   Calculates semester GPA and final letter grades according to standard academic credit scales.
*   **Detailed Analytics Report:** Overloaded representation methods to print structured information regarding classrooms, subjects, registered students, and detailed performance scripts.

## 📂 Project Structure

```text
├── ClassRoom.py       # Manages classroom objects, students, and subjects roster
├── school.py          # Core School configuration and static grading utility methods[cite: 2, 4]
├── persons.py         # Parent Person class with Student and Teacher subclasses[cite: 2, 3]
├── subjects.py        # Maps subject information with respective subject teachers[cite: 2, 5]
└── main.py            # Main runner file simulating the full ecosystem
