#用户相关接口
from api.base_api import BaseApi

class UserApi(BaseApi):
    def get_user(self, user_id):
        return self.client.get(f"/users/{user_id}")

    def get_user_posts(self, user_id):
        return self.client.get("/posts",params = {"userId": user_id})