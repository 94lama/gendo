import sys, openai, os
from .agent import *

client = openai.OpenAI()
client.project=os.getenv("OPENAI_PROJECT")
client.api_key=os.getenv("OPENAI_API_KEY")

def get_all_models(agent):
    models = agent.models.list()

    for model in models:
        print(model)
