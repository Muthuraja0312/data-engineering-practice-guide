
💡𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧:- 
/*
Write an SQL query to calculate the percentage of successful payments 
for each driver in the table. A payment is considered successful
if its status is 'Completed'
*/

-- 𝐑𝐢𝐝𝐞𝐬 𝐓𝐚𝐛𝐥𝐞
CREATE TABLE Rides ( 
ride_id INT PRIMARY KEY,
driver_id INT,
fare_amount DECIMAL(10, 2),
driver_rating DECIMAL(3, 2),
start_time DATETIME
);

-- 𝐈𝐧𝐬𝐞𝐫𝐭 𝐭𝐡𝐞 𝐝𝐚𝐭𝐚 𝐈𝐧𝐭𝐨 𝐑𝐢𝐝𝐞𝐬 𝐓𝐚𝐛𝐥𝐞
INSERT INTO Rides (ride_id, driver_id, fare_amount, driver_rating, start_time) VALUES(1, 101, 25.50, 4.8, '2024-01-10 09:00:00'),(2, 102, 15.00, 4.5, '2024-01-10 10:30:00'),(3, 101, 30.00, 4.9, '2024-01-11 11:00:00'),(4, 103, 12.75, 4.2, '2024-01-11 13:15:00'),(5, 102, 20.00, 4.7, '2024-01-12 14:00:00');

-- 𝐏𝐚𝐲𝐦𝐞𝐧𝐭𝐬 𝐓𝐚𝐛𝐥𝐞
CREATE TABLE Payments (
 payment_id INT PRIMARY KEY,
 ride_id INT,
 payment_status VARCHAR(255)
);

-- 𝐈𝐧𝐬𝐞𝐫𝐭 𝐭𝐡𝐞 𝐝𝐚𝐭𝐚 𝐈𝐧𝐭𝐨 𝐏𝐚𝐲𝐦𝐞𝐧𝐭𝐬 𝐓𝐚𝐛𝐥𝐞
INSERT INTO Payments (payment_id, ride_id, payment_status) VALUES
(1001, 1, 'Completed'),(1002, 2, 'Completed'),(1003, 3, 'Completed'),
(1004, 4, 'Pending'),(1005, 5, 'Completed'),(1006, 1, 'Refunded');


with cte as(select driver_id,sum(case when payment_status ='Completed' then 1 else 0 end) as completed_payments,count(*) as total_payments from rides a left join payments b on a.ride_id=b.ride_id group by driver_id) 
select *,cast(completed_payments *100/total_payments as decimal(5,2)) as percentage from cte 
