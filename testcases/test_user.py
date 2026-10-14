import allure

@allure.feature("用户模块")
class TestUser:


    @allure.story("接口关联")
    @allure.title("先查用户再查该用户帖子")
    def test_user_posts(self, user_api):
        r1 = user_api.get_user(1)
        assert r1.status_code == 200
        user_id = r1.json()["id"]

        r2 = user_api.get_user_posts(user_id)
        assert r2.status_code == 200
        posts = r2.json()
        assert len(posts) > 0
        assert all(p["userId"] == user_id for p in posts)