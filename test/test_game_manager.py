import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.game_manager import GameManager

from dotenv import load_dotenv
import os

def test_gamemanager_init():
    gm = GameManager()

if __name__ == "__main__":
    load_dotenv()
    test_gamemanager_init()
    print("GameManager init test passed.")
    # key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    # print (key_path)
