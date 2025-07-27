import json
import os

BASE_DIR = "D:/BIA/New learning/BIA_GENAI_LEARNING/"

def read_users():
    with open(os.path.join(BASE_DIR, "data", "users.json")) as stream:
        users = json.load(stream)
        return users

def get_user_by_id(user_id: int):
    users = read_users()
    # Assuming users is a list of dictionaries with 'id' and 'name'
    for user in users:
        if user.get('id') == user_id:
            return user.get('name')
    return None

if __name__ == "__main__":
    users = read_users()
    print(users)
    user_name = get_user_by_id(1)
    print(user_name)