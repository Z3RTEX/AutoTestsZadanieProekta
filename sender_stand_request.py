import requests
import configuration
import data


def post_new_user():
    body = data.user_body
    return requests.post(configuration.BASE_URL + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(auth_token, body):
    url = configuration.BASE_URL + configuration.CREATE_KIT
    data.kit_body = body
    new_headers = data.headers.copy()
    new_headers['Authorization'] = f'Bearer {auth_token}'
    return requests.post(url, json=body, headers=new_headers)
