SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary AS Salary
FROM Department d JOIN Employee e1 ON d.Id = e1.DepartmentId
WHERE e1.Salary = (
    SELECT MAX(e2.Salary)
    FROM Employee e2
    WHERE e2.DepartmentId = e1.DepartmentId
)
