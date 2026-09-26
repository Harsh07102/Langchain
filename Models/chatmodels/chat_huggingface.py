from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    temperature=0.7,
    max_new_tokens=512
)

chat = ChatHuggingFace(llm=llm)
n = input("Enter your prompt: ")

response = chat.invoke(n)

print(response.content)