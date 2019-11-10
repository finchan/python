import os
import requests
import json

def do_load_media(url, path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
        pre_content_length = 0
        # 循环接收视频数据
        while True:
            # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
            if os.path.exists(path):
                headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
            res = requests.get(url, stream=True, headers=headers, verify=False)

            content_length = int(res.headers['content-length'])
            # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
            if content_length < pre_content_length or (
                    os.path.exists(path) and os.path.getsize(path) == content_length):
                break
            pre_content_length = content_length

            # 写入收到的视频数据
            with open(path, 'ab') as file:
                file.write(res.content)
                file.flush()
                print('receive data，file size : %d  total size:%d' % (os.path.getsize(path), content_length))
    except Exception as e:
        print(e)


def do_retrieve_all_files(file_name, save_location, prefix):
    with open(file_name) as file:
        str = file.read().strip()
    resource = json.loads(str)
    aweme_list = resource["aweme_list"]
    #Get all resources
    for tiktok in aweme_list:
        target_name = tiktok["aweme_id"]
        target = tiktok["video"]["play_addr"]["url_list"][0]
        media_type = tiktok["media_type"]
        if media_type == 4:
            do_load_media(target, save_location+prefix+"___"+target_name+".mp4")


def getVidsList (file_name):
    with open(file_name) as file:
        str = file.read().strip()
    resource = json.loads(str)
    aweme_list = resource["aweme_list"]
    return aweme_list