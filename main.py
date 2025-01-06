import os
import subprocess

if __name__ == '__main__':
    # Run pytest with allure results
    subprocess.run(['pytest', '--alluredir=allure_results', '--disable-warnings'])

    # Generate Allure report
    subprocess.run(['allure', 'generate', 'allure_results', '-o', 'allure_report', '--clean'])
