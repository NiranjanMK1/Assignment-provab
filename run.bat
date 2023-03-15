behave -f allure_behave.formatter:AllureFormatter -o reports/jsonreports features/
allure generate reports/jsonreports --clean -o reports/htmlreports
