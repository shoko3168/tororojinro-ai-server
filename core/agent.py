class Agent:
    def __init__(self, user_id: str, name: str, personality: str, role=None):
        self.user_id = user_id
        self.name = name
        self.personality = personality  # 例: "疑い深い", "楽天家"

    def act(self, context_summary: str, timing: str):
        # f"{self.name}（{self.personality}）は「{context_summary}」について考え中です。"
        return {
            "speak": True,
            "message": "もし話すならこの内容"
        }

    def decide_vote(self, context: dict) -> str:
        return "学者 カーク"

    def decide_night_action(self, context: dict) -> dict:
        """
        return {
            "action": "attack" / "divine" / "guard" / "none",
            "target": "道化師 マリオン"
        }
        """
        # 非能力者
        return {
            "action": "none",
            "target": None
        }
