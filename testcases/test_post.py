import allure

@allure.feature("帖子模块")
class TestPost:


    @allure.story("查询帖子")
    @allure.title("获取帖子列表")
    def test_get_posts(self, post_api):
        r = post_api.get_posts()
        assert r.status_code == 200
        assert len(r.json()) == 100

    @allure.story("创建帖子")
    @allure.title("创建帖子-数据驱动")
    def test_create_post_ddt(self, post_api, post_data):
        case_name = post_data["case_name"]
        print(case_name)
        payload = post_data["payload"]
        r = post_api.create_post(payload)
        assert r.status_code == post_data["expected_code"]
        assert r.json()["title"] == post_data["expected_title"]

    @allure.story("删除帖子")
    @allure.title("删除帖子成功")
    def test_delete_post(self, post_api):
        r = post_api.delete_post(1)
        assert r.status_code == 200    
