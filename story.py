from langchain import PromptTemplate, OpenAI, LLMChain


def story(text):
    template = """
    You are story teller.
    You can narrate a story from the given context. The story shouldn't be more than 30 words
    
    CONTEXT: {text}
    STORY:
"""
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm_model = LLMChain(llm=OpenAI(model_name="gpt-3.5-turbo",
                         temperature=1, openai_api_key="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"), prompt=prompt, verbose=True)
    scene = llm_model.predict(text=text)
    return scene


k = input()

print(story(k))
