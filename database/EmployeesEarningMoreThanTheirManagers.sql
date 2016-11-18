select E1.Name as "Employee" 
    from Employee as E1
    left join Employee as E2 on E2.id = E1.ManagerId
    where E1.Salary > E2.Salary