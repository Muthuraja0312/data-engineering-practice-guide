CREATE TABLE Trips (CREATE TABLE Trips (
    Id INT PRIMARY KEY,
    Client_Id INT,
    Driver_Id INT,
    City_Id INT,
    Status STRING,
    Request_at DATE
);
CREATE TABLE Users (
    Users_Id INT PRIMARY KEY,
    Banned STRING,
    Role STRING
);
INSERT INTO Users (Users_Id, Banned, Role)
VALUES
(1, 'No', 'client'),
(2, 'Yes', 'client'),
(3, 'No', 'client'),
(4, 'No', 'client'),
(10, 'No', 'driver'),
(11, 'No', 'driver'),
(12, 'No', 'driver'),
(13, 'No', 'driver');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at)
VALUES
(1, 1, 10, 1, 'completed', '2013-10-01'),
(2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
(3, 3, 12, 6, 'completed', '2013-10-01'),
(4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
(5, 1, 10, 1, 'completed', '2013-10-02'),
(6, 2, 11, 6, 'completed', '2013-10-02'),
(7, 3, 12, 6, 'completed', '2013-10-02'),
(8, 2, 12, 12, 'completed', '2013-10-03'),
(9, 3, 10, 12, 'completed', '2013-10-03'),
(10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03');

select * from users;

select round((sum(case when status !="completed" then 1 else 0 end)/count(*))* 100,2) as rate, request_at from users a join trips b on a.Users_Id=b.Client_Id where Banned ='No' and request_at between '2013-10-01' and '2013-10-03' group by Request_at order by Request_at;
    Id INT PRIMARY KEY,
    Client_Id INT,
    Driver_Id INT,
    City_Id INT,
    Status STRING,
    Request_at DATE
);
CREATE TABLE Users (
    Users_Id INT PRIMARY KEY,
    Banned STRING,
    Role STRING
);
INSERT INTO Users (Users_Id, Banned, Role)
VALUES
(1, 'No', 'client'),
(2, 'Yes', 'client'),
(3, 'No', 'client'),
(4, 'No', 'client'),
(10, 'No', 'driver'),
(11, 'No', 'driver'),
(12, 'No', 'driver'),
(13, 'No', 'driver');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at)
VALUES
(1, 1, 10, 1, 'completed', '2013-10-01'),
(2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
(3, 3, 12, 6, 'completed', '2013-10-01'),
(4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
(5, 1, 10, 1, 'completed', '2013-10-02'),
(6, 2, 11, 6, 'completed', '2013-10-02'),
(7, 3, 12, 6, 'completed', '2013-10-02'),
(8, 2, 12, 12, 'completed', '2013-10-03'),
(9, 3, 10, 12, 'completed', '2013-10-03'),
(10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03');

select * from users;

select round((sum(case when status !="completed" then 1 else 0 end)/count(*))* 100,2) as rate, request_at from users a join trips b on a.Users_Id=b.Client_Id where Banned ='No' and request_at between '2013-10-01' and '2013-10-03' group by Request_at order by Request_at;
