SELECT first_half.flavor
FROM first_half
JOIN icecream_info
ON first_half.flavor = icecream_info.flavor
WHERE first_half.total_order>3000 and icecream_info.ingredient_type LIKE "fruit_based"
ORDER BY first_half.total_order DESC ;