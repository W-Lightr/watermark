# -*- coding: utf8 -*-
import json
import re
import requests


class Douyin:
    def __init__(self, url):
        self.__url = url
        self.__aweme = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="
        self.__title = ""
        self.__author = ""
        self.__mp3_title = ""
        self.__mp3_url = ""
        self.__mp4_url = ""
        self.__void_url = ""

    # 获取正则后的void_id
    def __request(self):
        share = requests.get(self.__url)
        void_id = re.search(r'video/.*?/', share.url)
        str_id = void_id.group()
        str_id = str_id.replace("video/", "").replace("/", "")
        self.__str_id = str_id

    # 获取视频地址和相关信息
    def request_vide(self):
        self.__request()
        dow_url = self.__aweme + self.__str_id
        # date 响应的所有数据
        date = requests.get(dow_url).json()
        # print(date)
        self.__title = date['item_list'][0]['desc']
        self.__author = date['item_list'][0]['author']['nickname']
        self.__mp3_title = date['item_list'][0]['music']['title']
        self.__mp3_url = date['item_list'][0]['music']['play_url']['uri']
        video_url = str(date['item_list'][0]['video']['play_addr']['url_list'][0])
        video_url = video_url.replace("playwm", "play")
        self.__void_url = video_url

    def response(self):
        self.__mp4_url = requests.get(self.__void_url).url
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({'mp3_title': self.__mp3_title, 'mp3_url': self.__mp3_url, 'video_url': self.__mp4_url,
                                'title': self.__title,
                                'author': self.__author})
        }


def main_handler(event, context):
    # 获取视频地址参数
    url = event['queryString']['v']
    print("参数1: " + json.dumps(event, indent=2))
    print("参数2: " + str(context))
    douyin = Douyin(url)
    douyin.request_vide()
    return douyin.response()
