class Agent:
    def __init__(self, userid: str, name: str, pid, personality: str):
        self.userid = userid
        self.name = name
        self.pid = pid
        self.personality = personality  # 例: "疑い深い", "楽天家"
        self.first_message = f"こんにちは、{name}です。よろしくお願いします！"

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

    @staticmethod
    def from_dict(data: dict):
        return Agent(
            userid=data.get("userid", ""),
            name=data.get("name", ""),
            pid=data.get("pid", ""),
            personality=data.get("personality", ""),
        )