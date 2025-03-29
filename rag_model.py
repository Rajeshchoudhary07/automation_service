import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from automation_functions import FUNCTIONS

class RAGModel:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.function_names = list(FUNCTIONS.keys())
        self.embeddings = self.model.encode(self.function_names)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve_function(self, query):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k=1)
        return self.function_names[indices[0][0]]

rag_model = RAGModel()