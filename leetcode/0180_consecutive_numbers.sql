SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l3.Num = l2.Num AND l2.Num = l1.Num AND
      l3.Id = l2.Id + 1 AND l2.Id = l1.Id + 1;
