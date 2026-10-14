import logging
import os

os.makedirs("log", exist_ok=True)  #创建logs目录，目录存在则跳过不报错

logging.basicConfig(
    level = logging.INFO,  #最低等级为INFO，低于不输出
    format = "%(asctime)s [%(levelname)s] %(message)s",  #定义格式：时间、级别、内容
    handlers = [
        logging.FileHandler("log/api.log", encoding = "utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)