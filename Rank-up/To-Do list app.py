import json
import os

Task_File="tasks.json"
def Load_tasks():
    if os.path.exists(Task_File):
        with open(Task_File, "r") as file:
            return json.load(file)
    return []

}