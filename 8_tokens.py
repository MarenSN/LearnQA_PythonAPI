import requests
import time
from json.decoder import JSONDecodeError

# variables
url_task = "https://playground.learnqa.ru/ajax/api/longtime_job"
status_ready = 'Job is ready'
status_not_ready = 'Job is NOT ready'


# 1. create task
try:
    task_response = requests.get(url_task)
    req_token = task_response.json()["token"]
    req_second = task_response.json()["seconds"]
except JSONDecodeError:
    print("not JSON format")

# 2. status "not ready"
not_ready_response = requests.get(url_task, params={"token": req_token})
status_not_ready_response = not_ready_response.json()
if status_not_ready_response["status"] == status_not_ready:
    print(f"You try to start new task until previous task end. Please wait {req_second} seconds")
    print(status_not_ready)

# 3. Waiting for task completion
time.sleep(req_second + 1)

# 4. status "ready"
ready_response = requests.get(url_task, params={"token": req_token})
status_ready_response = ready_response.json()
result_response = ready_response.json()["result"]
if status_ready_response["status"] == status_ready:
    print(f"\nPrevious task has finished. You can start a new task")
    print(f"The result: {result_response}")
    print(status_ready)
