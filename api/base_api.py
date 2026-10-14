#继承RequestsUtils
from utils.request_utils import RequestsUtil

class BaseApi:
    def __init__(self):
        self.client = RequestsUtil()