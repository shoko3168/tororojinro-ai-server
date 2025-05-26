import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.jinro_api import JinroAPI
from dotenv import load_dotenv

def test_get_vil():
    result = JinroAPI.get_vil(vid = "13")
    print(result)

if __name__ == "__main__":
    load_dotenv()
    test_get_vil()
    print("JinroAPI.get_village_list test passed.")
