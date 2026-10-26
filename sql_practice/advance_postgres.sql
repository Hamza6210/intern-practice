-- Window Functions

SELECT
    name,
    class_id,
    marks,
    RANK() OVER (PARTITION BY class_id ORDER BY marks DESC) AS class_rank,
    ROW_NUMBER() OVER (PARTITION BY class_id ORDER BY marks DESC) AS row_num,
    ROUND(AVG(marks) OVER (PARTITION BY class_id), 2) AS class_avg_marks

FROM students;


-- CTE (Common Table Expression)

WITH class_avg AS(
    SELECT class_id, AVG(marks) AS avg_marks
    FROM students
    GROUP BY class_id
)
SELECT
    s.name,
    c.class_name,
    s.marks,
    ROUND(ca.avg_marks, 2) AS class_average

FROM students s
JOIN classes c ON s.class_id = c.id
JOIN class_avg ca ON s.class_id = ca.class_id
WHERE s.marks > ca.avg_marks;



--INDEXES

DROP INDEX IF EXISTS idx_students_class;

EXPLAIN
SELECT * FROM students WHERE class_id = 1;

CREATE INDEX  idx_students_class ON students(class_id);

SET enable_seqscan = off;
EXPLAIN
SELECT * FROM students WHERE class_id = 1;