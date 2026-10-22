DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS classes;

CREATE TABLE classes (
    id INT PRIMARY KEY,
    class_name TEXT
);

CREATE TABLE students (
    id INT PRIMARY KEY,
    name TEXT,
    class_id INT,
    marks INT
);

INSERT INTO classes (id, class_name) VALUES
(1, 'Data Science'),
(2, 'Web Development'),
(3, 'Cyber Security');

INSERT INTO students (id, name, class_id, marks) VALUES
(1, 'Ali', 1, 85),
(2, 'Sara', 1, 92),
(3, 'Ahmad', 2, 70),
(4, 'Fatima', 2, 78),
(5, 'Usman', 1, 65),
(6, 'Hina', 2, 88);