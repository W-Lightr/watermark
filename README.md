#  抖音无水印解析

使用腾讯云函数（SCF）部署代码

#### 示例

##### 接口返回数据

###### 请求：

```
https://service-ljayspu6-1300659921.gz.apigw.tencentcs.com/release/douyin?v=https://v.douyin.com/JwVv8T6/
```

| 方法 | 参数 | 值                                            |
| ---- | ---- | --------------------------------------------- |
| GET  | v    | 抖音分享地址，如https://v.douyin.com/JwVv8T6/ |

###### 返回:

```
{
    "mp3_title": "@仓鼠历险记创作的原声",
    "mp3_url": "https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/6925007243020733197.mp3",
    "video_url": "http://v26.douyinvod.com/87416fbf1772af0cd64421d45bc89a22/602cbceb/video/tos/cn/tos-cn-ve-15/89561744665f4f87b30b5a281443cbf3/?a=1128&br=3632&bt=908&cd=0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202102151451230102121440393095A8D5&lr=&mime_type=video_mp4&pl=0&qs=0&rc=M3lwbXIzZ3I8MzMzZ2kzM0ApZDRlZGk2ZGQzNzkzZzk4OGcpaGRqbGRoaGRmNDA2bXNnbS5hYC0tMi0vc3NiXmEtMzVfXmMuMl9jMy0xOmNwb2wrbStqdDo%3D&vl=&vr=",
    "title": "#仓鼠 #手工#蜈蚣 @DOU+小助手",
    "author": "仓鼠历险记"
}
```

| mp3_title    | mp3_url  | video_url  | title    | author |
| ------------ | -------- | ---------- | -------- | ------ |
| 背景音频标题 | 背景音频 | 无水印地址 | 视频标题 | 作者   |



#### 使用方法

代码部署到腾讯云函数 (环境 python3.6)

```
腾讯云函数-->新建--> 自定义创建-->完成
```

```
代码粘贴
```

```
触发管理-->创建触发器--->触发方法：API网关触发-->请求方法：GET-->提交
```

```
点击API服务名 SCF_API_SERVICE 开通或者进入API网关--->选择API-->编辑-->添加参数 v
```





