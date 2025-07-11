from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Prompt Template
polish_prompt = """
You are a senior content editor. Your task is to polish the following content to improve clarity, flow, and tone.
Make sure the tone is {tone} and suitable for the audience: {audience}.

Do not remove key ideas, but feel free to:
- Simplify complex sentences
- Improve logical transitions
- Fix grammar and punctuation
- Use a consistent tone and voice

Here is the draft content:
{draft}

Return only the polished article.
"""

def polish_draft(draft: str, tone: str = "Professional", audience: str = "Business Decision Makers", model_name="gpt-4o-mini"):
    prompt_template = PromptTemplate(
        input_variables=["draft", "tone", "audience"],
        template=polish_prompt
    )

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model=model_name,
        temperature=0.5  # Slightly lower for polish (less creative, more precise)
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)

    polished = chain.run(draft=draft, tone=tone, audience=audience)
    return polished
