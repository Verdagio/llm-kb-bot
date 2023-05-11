import os
import chromadb
from chromadb.utils import embedding_functions as emb
from dotenv import load_dotenv


class ChromaClient:
    
    def __init__(self) -> None:
        load_dotenv()
        self.client = chromadb.Client()
        self.ef = emb.OpenAIEmbeddingFunction(api_key=os.getenv('OPENAI_API_KEY'), model_name='text-embedding-ada-002')
        
    
    def use_collection(self, name: str):
        return self.client.get_or_create_collection(name=name, embedding_function=self.ef)
    