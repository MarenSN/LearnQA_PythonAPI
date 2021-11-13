import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
total_redirects = len(response.history)
response_final = response

# finding the total amount of redirects
print(f"Total amount of redirects: {total_redirects}")

# output of the last URL
print(f"The last URL: {response_final.url}")
