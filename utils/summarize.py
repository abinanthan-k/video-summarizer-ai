from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os


def summarize_text(text):
    llm = ChatGroq(temperature=0.5, model_name="llama3-8b-8192")

    prompt = PromptTemplate.from_template(
        "You are an AI summarizer. Summarize the following transcript:\n\n{text}\n\nSummary:"
    )
    print("Summarizing text...")
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(text=text)
    return result
