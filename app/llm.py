from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text