
from core.agent import Agent
from firebase.firestore import FirestoreClient
from core.vil import Vil

class GameManager:
    def __init__(self):
        self.db = FirestoreClient()
        self.agents = {}
        self.vils = {}
        self.players = {}
        self.load_from_firestore()

