-- Write query to get number of graded assignments for each student:
SELECT S.id AS student_id, COUNT(A.id) AS graded_assignments_count
FROM Student AS S
JOIN Assignment AS A ON S.id = A.student_id
WHERE A.state = 'GRADED'
GROUP BY S.id
ORDER BY graded_assignments_count DESC;