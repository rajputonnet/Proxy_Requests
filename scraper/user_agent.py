import random


class UserAgent:
    user_agents = []

    def __init__(self):
        self.user_agents = open('config/user_agents.txt').read().splitlines()

    def get_random_user_agent(self):
        return random.choice(self.user_agents)
