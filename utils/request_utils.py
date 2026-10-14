import time
from config.setting import settings
from utils.logger import logger
import requests

class RequestsUtil:
    def __init__(self, base_url = None, timeout = None, headers = None):
        self.base_url = (base_url or settings.BASE_URL).rstrip("/")
        self.timeout = timeout or settings.TIMEOUT
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def _url(self, path):
        if path.startswith("http"):
            return path
        return f"{self.base_url}{path}"

    def request(self, method, path, **kwargs):
        url = self._url(path)
        kwargs.setdefault("timeout", self.timeout)
        start_time = time.perf_counter()
        logger.info(f"请求{method}{url} | params= {kwargs.get('params')} | json = {kwargs.get('json')}")
        resp = self.session.request(method, url, **kwargs)
        cost_time = round((time.perf_counter() - start_time) * 1000, 2)
        logger.info(f"响应{resp.status_code} | 耗时：{cost_time}ms | body = {resp.text[:500]}")
        return resp

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)
    
    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)
    
    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)
    
    def patch(self, path, **kwargs):
        return self.request("PATCH", path, ** kwargs)
    
    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)
    
    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})
    
    def close(self):
        self.session.close()

    