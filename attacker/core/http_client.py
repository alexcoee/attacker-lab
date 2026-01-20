import requests

def send_request(method, url, timeout=3):
    try:
        response = requests.request(
            method=method,
            url=url,
            timeout=timeout
        )
        return response
    except requests.exceptions.RequestException:
        return None
