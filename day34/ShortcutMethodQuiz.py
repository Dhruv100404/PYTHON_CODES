import html

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters, verify=False)
response.raise_for_status()
data = response.json()["results"]
count = 0

for i in range(0, 9):
    question = html.unescape((data[i]["question"]))
    answer = data[i]["correct_answer"]

    user_answer = input(f"Q{i + 1}  {question} (True/False)")

    if answer == user_answer:
        count = count + 1
        print(f"You Got the Right Answer! \n Your Score is {count}/10")
    else:
        print(f"You Got the Wrong Answer! \n Your Score is {count}/10")
