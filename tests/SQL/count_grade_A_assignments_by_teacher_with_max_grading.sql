-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT T.teacher_id, COUNT(A.id) AS count_grade_A_assignments
FROM Teacher AS T
JOIN Assignment AS A ON T.id = A.teacher_id
WHERE A.grade = 'A'
GROUP BY T.teacher_id
ORDER BY count_grade_A_assignments DESC
LIMIT 1;