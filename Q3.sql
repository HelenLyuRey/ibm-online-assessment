SELECT owner_id
from owner
JOIN alticle using(owner_name)
JOIN category_article_mapping using(article_id)
JOIN category using (category_id)
group by owner_id