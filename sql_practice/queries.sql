SELECT name, marks FROM students
WHERE marks > 80;


SELECT 
    COUNT(*) AS total_students,
    AVG(marks) AS avg_marks,
    MAX(marks) AS highest,
    MIN(marks) AS lowest
FROM students;


SELECT class_id, AVG(marks) AS avg_marks FROM students
GROUP BY class_id HAVING AVG(marks) > 75;


SELECT 
    students.name,
    classes.class_name,
    students.marks
FROM students
INNER JOIN classes
    ON students.class_id = classes.id;


SELECT
    classes.class_name,
    students.name
FROM classes
LEFT JOIN students
    ON students.class_id = classes.id;


SELECT name, marks FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
);