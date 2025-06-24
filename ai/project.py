
def get_all(agent):
    models = agent.models.list()

    for model in models:
        print(model)