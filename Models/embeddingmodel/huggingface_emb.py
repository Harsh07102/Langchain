from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"
                              
                              )
res = model.embed_query("Capital of india")
print(res)
