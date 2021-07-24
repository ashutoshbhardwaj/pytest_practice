import json

from pytest import fixture
from config import Config
from selenium import webdriver

data_path = '/home/ashutosh/pyworkspace/pytest_practice/tests/test_data.json'
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="dev or qa"
    )


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@fixture(scope="session")
def app_config(env):
    return Config(env)

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

@fixture(params=load_test_data(data_path))
def tv_model(request):
    data = request.param
    return data

@fixture(params=[webdriver.Chrome])
def browser(request):
    driver = request.param
    drvr = driver()
    yield  drvr
    drvr.quit()

