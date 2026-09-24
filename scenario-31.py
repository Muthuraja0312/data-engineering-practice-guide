with cte as (
  select explode(sequence(TIMESTAMP '2024-06-01 00:00:00', TIMESTAMP '2024-06-01 04:00:00', INTERVAL '1' HOUR)) as expected_time
),

cte1 as (
  select date_trunc('hour', event_time) as event_hour from event_logs)

select a.expected_time
from cte a
left join cte1 b on a.expected_time = b.event_hour where event_hour is null ;
