SELECT s.name, AVG(g.grade) AS avg_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.name = 'Назва_предмета'
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
