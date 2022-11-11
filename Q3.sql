SELECT owner_id, owner_name, COUNT(DISTINCT category_name) as different_category_count
from owner
JOIN alticle using(owner_name)
JOIN category_article_mapping using(article_id)
JOIN category using (category_id)
group by owner_id