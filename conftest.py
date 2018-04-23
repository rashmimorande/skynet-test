
def pytest_addoption(parser):
    parser.addoption("--type",default='firefox')
    parser.addoption("--env",default='local')

