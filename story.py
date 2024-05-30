from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai


def story(text, api):
    template = """
    You are story teller.
    You can narrate a story from the given context. The story shouldn't be more than 60 words. 
    The story should be interesting and heart warming or emotional or joyful. Only Return the story as a string.
    CONTEXT: {text}
    STORY:
"""
    model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key=api)
    scene = model.invoke(template+text)
    return scene.content
