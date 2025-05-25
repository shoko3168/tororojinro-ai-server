from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

agents = {}

from typing import List, Dict

def summarize_village_day(logs: List[Dict]) -> str:
    summary_lines = []
    co_occupations = []
    divinations = []
    executions = []
    attacks = []
    village_trends = []

    for log in logs:
        text = log.get("text", "")
        name = log.get("name", "")
        type_ = log.get("type", "")

        if "占いCO" in text or "霊能CO" in text:
            co_occupations.append(f"{name}: {text.strip()}")

        if ("●" in text or "○" in text) and ("占" in text or "理由" in text or "CO" in text):
            divinations.append(f"{name}: {text.strip()}")

        if "処刑されました" in text:
            executions.append(text.strip())

        if "無残な姿で発見されました" in text:
            attacks.append(text.strip())

        if "吊り" in text and "いい" in text:
            village_trends.append(f"{name}: {text.strip()}")

    if co_occupations:
        summary_lines.append("■CO宣言:")
        summary_lines.extend(co_occupations)

    if divinations:
        summary_lines.append("■占い・霊能結果:")
        summary_lines.extend(divinations)

    if executions:
        summary_lines.append("■処刑結果:")
        summary_lines.extend(executions)

    if attacks:
        summary_lines.append("■襲撃結果:")
        summary_lines.extend(attacks)

    if village_trends:
        summary_lines.append("■村の流れ:")
        summary_lines.extend(village_trends)

    return "\n".join(summary_lines)

@app.route("/")
def health_check():
    return "TororoJinro AI Server is running!", 200


@app.route("/join", methods=["POST"])
def join():
    data = request.get_json()
    agent_id = data.get("id")
    role = data.get("role")

    if not agent_id or not role:
        return jsonify({"error": "id and role are required"}), 400

    agents[agent_id] = {
        "id": agent_id,
        "role": role,
        "history": []
    }

    return jsonify({"message": f"Agent {agent_id} ({role}) joined"}), 200


@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    agent_id = data.get("id")

    if agent_id not in agents:
        return jsonify({"error": "Agent not found"}), 404

    # DUMMY
    response = f"{agent_id}（{agents[agent_id]['role']}）は、うーん怪しいですねと言った。"

    # 発言履歴に記録
    agents[agent_id]["history"].append(response)

    # TODO: とろろ人狼の /api/speak にPOST

    return jsonify({"response": response}), 200


if __name__ == "__main__":
    app.run(debug=True)
