#End-to_end ML Project example
#Build a simple recommendation system

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample User-Item Ratings Matrix
data = {'Item1':[5,0,3], 'Item2':[4,0,0], 'Item3':[1,1,0]}
ratings = pd.DataFrame(data, index=['User1', 'User2', 'User3'])
print(ratings)
#Compute consine similarity
item_similarity = cosine_similarity(ratings.T) #Transpose for item-based similarity
print(item_similarity)
item_similarity_df = pd.DataFrame(item_similarity, index=ratings.columns, columns=ratings.columns)


print("Item-Item Similarity Matrix:\n", item_similarity_df)

#Recommend a similar items for Item1
recommended_items = item_similarity_df['Item1'].sort_values(ascending=False)[1:3]
print("Top Recommendations for Item1:\n", recommended_items)