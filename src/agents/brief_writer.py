# src/ agents/ brief_writer.py
from langchain_openai import ChatOpenAI  # Wrapper for OpenAI's chat models
from langchain.prompts import PromptTemplate  # Reusable template for prompt formatting
from langchain.chains import LLMChain  # Combines LLMs with prompts to
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt for generating a brief with multiple fields
brief_prompt = """
You are a senior content strategist. Based on the topic title and description below, write a structured content brief including:

1. A clear and compelling article title
2. A blog post outline with 4-6 sections
3. Tone of the article (e.g. professional, witty, conversational)
4. Intended audience (e.g. marketers, tech founders)
5. A suggested call to action (CTA)

Topic Title: {title}

Topic Description: {description}

Respond in this format:

Title:
Outline:
Tone:
Audience:
CTA:
"""

def generate_brief(title: str, description: str, model_name="gpt-4o-mini"):

    # Langhchain PromptTemplate needs to know the name # of the variables it will use in the template, not the values.
    # In this case, we have a single variable called "keywords".
    # The template will be filled in with the actual keywords when the prompt is run.
    # This allows for dynamic generation of prompts based on user input or other variables.
    prompt_template = PromptTemplate(
        input_variables=["title", "description"],  # Variables to be filled in the prompt
        template = brief_prompt
    )

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY,
                     model=model_name,
                     temperature=0.7)  # Controls randomness. 0 = deterministic, 1 = creative. 0.7 gives moderately creative results.
    
    chain = LLMChain(llm=llm, prompt=prompt_template)

    response = chain.run(title =title, description=description)

    return response.strip()
