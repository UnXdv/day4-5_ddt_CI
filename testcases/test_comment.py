import allure

@allure.feature("评论模块")
class TestComment:


    @allure.story("查询评论")
    @allure.title("获取帖子1的评论")
    def test_get_comments(self, comment_api):
        r = comment_api.get_comments(1)
        assert r.status_code == 200
        comments = r.json()
        assert len(r.json()) > 0
        assert all(c["postId"] == 1 for c in comments)

    @allure.story("创建评论")
    @allure.title("创建评论成功")
    def test_create_comment(self, comment_api):
        payload = {"title":"foo", "body" : "bar", "userId": 1, "postId": 1}
        r = comment_api.create_comment(payload)
        assert r.status_code == 201
        assert r.json()["postId"] == 1