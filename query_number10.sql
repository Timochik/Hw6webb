SELECT sub.name
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
JOIN teachers AS t ON sub.teacher_id = t.id
WHERE s.name = 'Ім'я_студента' AND t.name = 'Ім'я_викладача';
