import os
#from langchain.chains import LLMChain
from transformers import pipeline

HF_API_KEY = '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'
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HF_API_KEY

model_folder = "question-answering"
model_name = "distilbert-base-cased-distilled-squad"
model_revision = "main" #"626af31"

# Load the question answering pipeline with model name and revision
qa_pipeline = pipeline(model_folder, model=model_name, revision=model_revision)

# Provide context and question
context = "The game of cricket. Sachin scored 10000 runs while Kohli scored 9000. Some Abhi scores well over 5000 runs"
question = "Who is the best batsman?"
# Perform question answering
answer = qa_pipeline(question=question, context=context)

# Print the answer
print("Question:", question)
print("Answer:", answer['answer'])