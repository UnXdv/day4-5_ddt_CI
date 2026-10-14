import pytest
import yaml
from api.post_api import PostApi
from api.comment_api import CommentApi
from api.user_api import UserApi

@pytest.fixture(scope = "session")
def post_api():
    return PostApi()

@pytest.fixture(scope = "session")
def comment_api():
    return CommentApi()

@pytest.fixture(scope = "session")
def user_api():
    return UserApi()

def pytest_generate_tests(metafunc):
    if "post_data" in metafunc.fixturenames:
        with open("data/post_data.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            cases = data["create_post"]
            ids = [case["case_name"] for case in cases]
            metafunc.parametrize("post_data", cases, ids=ids)
