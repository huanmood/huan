import pymysql
import redis
import yaml
import os
import config
# 读取配置文件


config_path = os.path.join(config.DIR_PATH, 'DB.yaml')
with open(config_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# MySQL连接
def get_mysql_conn():
    return pymysql.connect(
        host=config['mysql']['host'],
        port=config['mysql']['port'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database'],
        cursorclass=pymysql.cursors.DictCursor  # 返回字典形式
    )

# Redis连接
def get_redis_conn():
    pool = redis.ConnectionPool(
        host=config['redis']['host'],
        port=config['redis']['port'],
        db=config['redis']['db']
    )
    return redis.Redis(connection_pool=pool)
