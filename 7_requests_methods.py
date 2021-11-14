import requests

my_url = "https://playground.learnqa.ru/api/compare_query_type"
methods = ["GET", "PUT", "POST", "DELETE"]

# Task #1 Any request, no parameters
response_no_params = requests.get(my_url)
print(f"Ответ на запрос без параметров: '{response_no_params.text}'")

# Task #2 Request method out of the list
payload_out_list = {"method":"HEAD"}
response_out_list_method = requests.request(method="HEAD", url=my_url, data=payload_out_list)
print(f"Ответ на запрос методом {response_out_list_method.request.method} (вне списка): <{response_out_list_method.text}>")

# Task #3 Request method in the list
payload_in_list = {"method":"PUT"}
response_in_list_method = requests.request(method="PUT", url=my_url, data=payload_in_list)
success_response = response_in_list_method.text
print(f"Ответ на запрос методом {response_in_list_method.request.method} (из списка): {response_in_list_method.text}")

# Task #4 All possible variations
for request_method in methods:
    for params_method in methods:
        payload = {"method": params_method}

        if request_method == "GET":
            response = requests.request(method=request_method, url=my_url, params=payload)
            if (request_method != params_method and response.text == success_response) or \
               (request_method == params_method and response.text != success_response):
                print("\nBug detected:")
                print(f"Метод {request_method}, параметр {params_method}, Ответ: {response.text}")
        else:
            response = requests.request(method=request_method, url=my_url, data=payload)
            if (request_method != params_method and response.text == success_response) or \
               (request_method == params_method and response.text != success_response):
                print("\nBug detected:")
                print(f"Метод {request_method}, параметр {params_method}, Ответ: {response.text}")
