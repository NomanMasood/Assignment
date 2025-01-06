import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.allure_results_dir = f'C:\\Users\\nomanm\\PycharmProjects\\pythonProject\\Assignment\\allure_results'  # Directory for storing results
