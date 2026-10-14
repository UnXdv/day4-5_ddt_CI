## base_url、超时、环境

class Settings:
    EVN = "test"

    EVN_MAP = {
        "test" : "https://jsonplaceholder.typicode.com",
        "dev" : "https://jsonplaceholder.typicode.com",
        "prod" : "https://jsonplaceholder.typicode.com",
    }
    
    BASE_URL = EVN_MAP[EVN]
    print(BASE_URL)
    TIMEOUT = 10
    LOG_DIR = "logs"
    ALLURE_DIR = "allure-results"

settings = Settings()