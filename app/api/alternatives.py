import json
import os

BASE_DIR= "D:/BIA/New learning/BIA_GENAI_LEARNING/"

def read_alternatives():
    with open (os.path .join (BASE_DIR, "data", "alternatives.json")) as stream:
        alternatives = json.load(stream)
        return alternatives

if __name__ == "__main__":
    print(read_alternatives())