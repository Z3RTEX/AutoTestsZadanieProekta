import data
import sender_stand_request


def get_new_user_token():
    res = sender_stand_request.post_new_user()
    if res.ok:
        return res.json()['authToken']
    else:
        return ''


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    body = get_kit_body(name)
    token = get_new_user_token()
    res = sender_stand_request.post_new_client_kit(token, body)
    assert res.status_code == 201
    assert res.json()['name'] == name


def negative_assert_code_400(name):
    body = get_kit_body(name)
    token = get_new_user_token()
    res = sender_stand_request.post_new_client_kit(token, body)
    assert res.status_code == 400
    assert res.json()['name'] == name


def negative_assert_no_first_name(body):
    token = get_new_user_token()
    res = sender_stand_request.post_new_client_kit(token, body)
    assert res.status_code == 400
    assert res.json()["code"] == 400
    assert res.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1.

def test_valid_kit_body_name_1():
    positive_assert('a')


# Тест 2.

def test_valid_kit_body_name_511():
    positive_assert('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')


# Тест 3.
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400('')


# Тест 4.

def test_invalid_kit_body_name_512():
    negative_assert_code_400('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCD')


# Тест 5.
def test_valid_kit_body_name_eng_word():
    positive_assert('QWErty')


# Тест 6.
def test_valid_kit_body_name_rus_word():
    positive_assert('Мария')


# Тест 7.
def test_valid_kit_body_name_symbols():
    positive_assert('"№%@",')


# Тест 8.
def test_valid_kit_body_name_space():
    positive_assert('Человек и КО')


# Тест 9.
def test_valid_kit_body_name_numbers():
    positive_assert('123')


# Тест 10.
def test_create_kit_no_name_get_error_response():
    body = data.kit_body.copy()
    body.pop('name')
    negative_assert_no_first_name(body)


# Тест 11.
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(123)
