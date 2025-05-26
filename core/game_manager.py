
from core.agent import Agent
from firebase.firestore import FirestoreClient
from core.vil import Vil
from core.jinro_api import JinroAPI

class GameManager:
    def __init__(self):
        self.db = FirestoreClient()
        self.agents = {}
        self.joined_villages = []
        self.players = {}
        self.load_from_firestore()
        self.load_jinro_api()

    def load_jinro_api(self):
        new_joined_vilages = []
        # joined_villagesにある分だけ村情報を取得
        for village_id in self.joined_villages:
            vil = JinroAPI.get_vil(vid=village_id)
            # print(vil['vid'])
            # print(vil['state'])
            # print(vil['players'])
            has_bot = self.load_agent_players(vil)
            if has_bot:
                new_joined_vilages.append(village_id)
        self.db.set_document("game_manager_settings", "joined_villages", {"joined_villages": new_joined_vilages})

    def load_agent_players(self, vil):
        has_bot = False
        for player in vil['players']:
            agent = Agent.from_dict(player)
            if agent.userid.startswith("bot") and agent.userid[3:].isdigit():
                self.players[str(vil['vid']) + '_' + agent.userid] = agent
                has_bot = True
        return has_bot

    def load_from_firestore(self):
        settings = self.db.get_document("game_manager_settings", "joined_villages")
        if settings and "joined_villages" in settings:
            self.joined_villages = settings["joined_villages"]
        else:
            self.joined_villages = []

    def load_agents(self):
        agent_data = self.db.get_all_documents("agents")
        for item in agent_data:
            agent = Agent.from_dict(item)
            self.agents[agent.name] = agent

    def update_agent(self, agent: Agent):
        self.agents[agent.name] = agent
        self.db.set_document("agents", agent.name, agent.to_dict())

    def update_village(self, village_id, village):
        self.villages[village_id] = village
        self.db.collection("villages").document(village_id).set(village.to_dict())

    def log_action(self, village_id, log_dict):
        self.db.collection("villages").document(village_id).collection("logs").add(log_dict)
        self.agents[agent_id] = {
            "id": agent_id,
            "role": role,
            "status": "active"
        }

    def entry_player(self, agent_id: str, role: str):
        if agent_id not in self.agents:
            self.agents[agent_id] = Agent(name=agent_id, role=role)
        else:
            self.agents[agent_id].role = role
        self.db.collection("agents").document(agent_id).set(self.agents[agent_id].to_dict())
