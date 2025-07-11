# src/agents/brief_writer.py

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt Template
brief_prompt = """
You are a senior content strategist. Based on the topic: "{title}" and the description: "{description}", write a structured content brief as a JSON object with the following keys:

{{
  "title": "<Catchy Article Title>",
  "outline": ["Section 1", "Section 2", "Section 3", "Section 4"],
  "tone": "<Specify tone, e.g., Professional, Conversational, Witty>",
  "audience": "<Intended Audience>",
  "cta": "<Call to Action>"
}}

Only return the JSON. No additional commentary.
"""

def generate_brief(title: str, description: str, model_name="gpt-4o-mini"):
    #print("generate_brief called")
    #print(f"DEBUG: Title and Description passed are:\nTitle: {title}\nDescription: {description}")

    prompt_template = PromptTemplate(
        input_variables=["title", "description"],
        template=brief_prompt
    )

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=model_name,
        temperature=0.7
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)
    #print("DEBUG: Calling chain.run...")

    raw_response = chain.run(title=title, description=description)
    #raw_response = chain.invoke({"title": title, "description": description})

    #print("DEBUG: Raw response received:", raw_response)

    #brief = json.loads(raw_response.strip().strip("```").strip("json").strip())

    try:
        #print("DEBUG: Raw response:", raw_response)
        brief = json.loads(raw_response.replace("```json", "").replace("```", "").strip())

    except json.JSONDecodeError:
        print("Warning: Failed to parse JSON response. Returning raw response.")
        return raw_response.strip()

    return brief
