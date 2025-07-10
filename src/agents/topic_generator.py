import json
from langchain_openai import ChatOpenAI # Wrapper for OpenAI's chat models
from langchain.prompts import PromptTemplate # Reusable template for prompt formatting
from langchain.chains import LLMChain # Combines LLMs with prompts to create a chain of operations
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Return a JSON array instead of a text response so that it is easier to parse one topic at a time.
    # Note the double curly braces {{ and }} around the JSON object literals inside the prompt. 
    # This tells the PromptTemplate to keep them as literal braces rather than interpreting them as variables.
prompt = """
You are a content strategist. Based on the following keywords: {keywords},
please suggest 5 article topics as a JSON array, where each topic has:
- "title": a short, catchy article title,
- "description": a brief explanation of the topic.

Example output:

[
  {{
    "title": "Harnessing AI in Marketing",
    "description": "How AI is transforming personalized customer experiences."
  }},
  {{
    "title": "SEO Automation Tools",
    "description": "Latest AI-powered tools for streamlining SEO workflows."
  }}
]

Return ONLY the JSON array, no extra text.
"""


def generate_topics(keywords: list, model_name = "gpt-4o-mini"):
    
    #print("generate_topics called")
    #print("DEBUG: Keywords passed in:", keywords[:5])  # preview first 5 keywords

    # Langhchain PromptTemplate needs to know the name # of the variables it will use in the template, not the values.
    # In this case, we have a single variable called "keywords".
    # The template will be filled in with the actual keywords when the prompt is run.
    # This allows for dynamic generation of prompts based on user input or other variables.
    prompt_template = PromptTemplate(
        input_variables=["keywords"], # Variables to be filled in the prompt 
        template=prompt
    )

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, 
                     model=model_name, 
                     temperature=0.7) # Controls randomness. 0 = deterministic, 1 = creative. 0.7 gives moderately creative results.
    
    chain = LLMChain(llm=llm, prompt=prompt_template)

    keywords_str = ", ".join(keywords)

    #print("DEBUG: Calling chain.run with keywords:", keywords_str)
    raw_response = chain.run(keywords=keywords_str)
    #print("DEBUG: Raw response:", raw_response)

    # Parse the JSON response
    try:
        topics = json.loads(raw_response)
    except json.JSONDecodeError:
        print("Warning: Failed to parse JSON response. Returning raw response.")
        return raw_response.strip()
    
    return topics


    