from langchain_openai import ChatOpenAI # Wrapper for OpenAI's chat models
from langchain.prompts import PromptTemplate # Reusable template for prompt formatting
from langchain.chains import LLMChain # Combines LLMs with prompts to create a chain of operations
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = """You are a content strategist. 
Based on the following keywords: {keywords}
Suggest 5 article topics that are fesh, relevant, and engaging."""


def generate_topics(keywords: list, model_name = "gpt-4o-mini"):

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
    response = chain.run(keywords=keywords_str)

    return response.strip()


    