from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()
model = ChatAnthropic(
    model = 'claude-3-5-sonnet-20241022',
    api_key=os.getenv("antropic_api")
    )
result = model.invoke("Write a poem on cricket")
print(result.content)


