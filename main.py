from multiprocessing import Process
import os
import time

from rt import tg_watchon_class
from conf import config

# 下载 history 不是实时监听 实时监听在 `rt`


def get_media(channel_username, client):
    # myself = client.get_me()
    # print(channel_username)
    # limit = 1000 history 1000 records
    for msgs in client.get_messages(channel_username, limit=1000):
        conf = config()
        if msgs.media is not None:
            salt = conf.get_random_file_name()
            t_dir = time.strftime("%Y-%m-%d", time.localtime())
            filename = conf.get_pic_path() + str(t_dir) + '/' + str(salt)
            client.download_media(msgs.media, filename)


if __name__ == '__main__':

    t = tg_watchon_class()
    p_list = []
    # for xx in ['hao123']:
    #     p_list.append(Process(target=get_media, args=('%s' % xx,t.get_client(),)))

    # 独立启动监听
    p_list.append(Process(target=t.start, args=()))
    for xx in p_list:
        xx.start()
    for xx in p_list:
        xx.join()
    print('(Press Ctrl+C to main thread)')
