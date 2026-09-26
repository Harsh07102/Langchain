from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    api_key = os.getenv("GOOGLE_API_KEY")
    )
result = model.invoke("Write a poem on cricket")
print(result.content)

