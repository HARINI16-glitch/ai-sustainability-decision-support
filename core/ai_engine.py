from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class AIEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def get_best_response(self, user_query, knowledge_list):
        query_vec = self.model.encode([user_query])
        knowledge_vecs = self.model.encode(knowledge_list)

        similarities = cosine_similarity(query_vec, knowledge_vecs)[0]
        best_index = np.argmax(similarities)

        return knowledge_list[best_index]
