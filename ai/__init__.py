import sys, openai
from .agent import *
from config import config

client = openai.OpenAI()
client.project = config.OPENAI_PROJECT
client.api_key = config.OPENAI_API_KEY

def get_all_models(agent):
    models = agent.models.list()

    for model in models:
        print(model)
