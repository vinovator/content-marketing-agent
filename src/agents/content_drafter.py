import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define the structured prompt
draft_prompt = """
You are an expert content writer.

Using the following brief, write a complete blog post draft.

Title: {title}
Outline: {outline}
Tone: {tone}
Audience: {audience}
Call to Action: {cta}

Instructions:
- Use the outline to structure the blog.
- Ensure the tone matches the target audience.
- Keep the content informative, engaging, and SEO-friendly.
- Conclude with the given Call to Action.

Begin writing the blog post now:
"""

def generate_draft(brief: dict, model_name="gpt-4o-mini"):
    prompt_template = PromptTemplate(
        input_variables=["title", "outline", "tone", "audience", "cta"],
        template=draft_prompt,
    )

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=model_name,
        temperature=0.7
    )

    chain = prompt_template | llm | StrOutputParser()

    return chain.invoke(brief).strip()
