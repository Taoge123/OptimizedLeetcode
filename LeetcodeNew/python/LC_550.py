
"""

Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation:
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33


with temp as (
    select a.player_id, a.event_date, b.first_login
    from activity a
    left join
        (select player_id, min(event_date) as first_login
        from activity
        group by 1) b
    on a.player_id = b.player_id
)

select round(count(distinct player_id) / (select count(distinct player_id) from activity), 2) as fraction
from temp
where datediff(event_date, first_login) = 1



"""

