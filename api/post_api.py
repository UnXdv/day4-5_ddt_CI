#帖子相关接口
from api.base_api import BaseApi

class PostApi(BaseApi):
    def get_posts(self):
        return self.client.get("/posts")

    def get_post(self, post_id):
        return self.client.get(f"/posts/{post_id}")

    def create_post(self, payload):
        return self.client.post("/posts", json= payload)

    def update_post(self, post_id, payload):
        return self.client.post(f"/posts/{post_id}", json = payload)

    def patch_post(self, post_id, payload):
        return self.client.patch(f"/posts/{post_id}", json = payload)

    def delete_post(self, post_id):
        return self.client.delete(f"/posts/{post_id}")