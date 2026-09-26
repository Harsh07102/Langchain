from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

n = input("Write Your Prompt : ")
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("gemini_api")
)

result = llm.invoke(n)
print(result.content[0]['text'])