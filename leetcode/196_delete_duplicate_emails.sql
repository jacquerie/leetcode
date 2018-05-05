DELETE p1
FROM Person AS p1
JOIN Person AS p2
WHERE p1.Id > p2.Id AND p1.Email = p2.Email
