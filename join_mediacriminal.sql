SELECT c.first_name as 'first Name',last_name,m.title, CONVERT (m.description using UTF8)
from 	(criminal as c 
		join media2criminal as m2c on c.id = m2c.criminal_id)
        join media as m on m.id = m2c.media_id
where c.last_name like '%undy%'