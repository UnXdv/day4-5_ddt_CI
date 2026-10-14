from api.base_api import BaseApi

class CommentApi(BaseApi):
    def get_comments(self, post_id):
        return self.client.get(f"/posts/{post_id}/comments")

    def create_comment(self, payload):
        return self.client.post(f"/comments", json = payload)