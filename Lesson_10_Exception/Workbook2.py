import requests
from requests.exceptions import HTTPError

def send_request(status_code=200):
    response = requests.get("https://httpstat.us/%d" % status_code)
    response.raise_for_status()
    return response.status_code

while True:
    try:
        code = int(input("Введите http код для проверки: "))
        response_code = None
        try:
            response_code = send_request(code)
        except HTTPError as ex:
            print('Произошла ошибка при отправке HTTP-запроса: %s' % str(ex))
            response_code = ex.response.status_code
        finally:
            print(f'Получен код: {response_code}')
        break
    except ValueError:
        print("Код должен быть представлен только числом! Попробуйте снова.")


