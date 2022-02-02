from . import utils
import requests

def test_ping():
    proc = utils.start_server()

    r = requests.get('http://localhost:8000/ping')
    print(r.text)
    print(r.status_code)
    assert r.status_code == 200
    assert r.text == "OK"

    utils.terminate_server(proc)


test_ping()