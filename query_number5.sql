SELECT sub.name
FROM subjects AS sub
JOIN teachers AS t ON sub.teacher_id = t.id
WHERE t.name = 'Ім'я_викладача';
