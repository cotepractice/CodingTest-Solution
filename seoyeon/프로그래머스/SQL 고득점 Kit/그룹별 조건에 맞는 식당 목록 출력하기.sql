select m.member_name as MEMBER_NAME, r.review_text as REVIEW_TEXT, date_format(r.review_date,"%Y-%m-%d") as REVIEW_DATE
from rest_review r
join member_profile m on r.member_id = m.member_id
where r.member_id = (select member_id from rest_review group by member_id order by count(member_id) DESC limit 1)
order by r.review_date, r.review_text
