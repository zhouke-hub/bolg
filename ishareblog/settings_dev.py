from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','ishareblog.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ishareblog_test',
        'USER': 'ishareblog',
        'PASSWORD': 'ishareblog@123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 1、取消外键约束，否则多对多模型迁移报django.db.utils.IntegrityError: (1215, 'Cannot add foreign key constraint')；
        # 2、解决字符串4个字节的utf8编码的字符报错的问题
        'OPTIONS': {
            'charset': 'utf8mb4',"init_command": "SET foreign_key_checks = 0;",
        }
    }
}