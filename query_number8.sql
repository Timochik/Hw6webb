SELECT AVG(g.grade) AS avg_grade
FROM teachers AS t
JOIN subjects AS sub ON t.id = sub.teacher_id
JOIN grades AS g ON sub.id = g.subject_id
WHERE t.name = 'Ім'я_викладача';
