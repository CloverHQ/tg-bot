import time

from telethon import TelegramClient, events

from conf import config
import os

# Printing download progress


def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))


class tg_watchon_class:

    def __init__(self):
        cfg = config()
        self.cfg1 = cfg
        self.data_storage_path = cfg.getpath()
        self.api_id = cfg.get_API_ID()
        self.api_hash = cfg.get_API_HASH()

        self.client = TelegramClient(cfg.get_TG_AUTH_FILE_NAME(), self.api_id,
                                     self.api_hash).start()

        @self.client.on(events.NewMessage(chats=5520741783))
        async def handler(event):
            print("handler init success")
            '''
                print('sender: ' + str(event.input_sender) + 'to: ' + str(event.message.to_id))
            '''
            salt = self.cfg1.get_random_file_name()
            t_dir = time.strftime("%Y-%m-%d", time.localtime())
            filename_temp = self.data_storage_path + \
                '/' + str(t_dir) + '/' + str(salt)

            print("download - " + filename_temp)

            import re
            filename_ = re.findall(r"file_name='(.+?)'", str(event.media))  #
            # print(str(event.media))
            if len(filename_) > 0:
                filename = "{}_{}".format(filename_temp,
                                          str(filename_[0]).replace(" ", "_"))
            else:
                filename = filename_temp
            await event.message.download_media(filename)
            os.system('php coocc files:scan --path=tg_bot/files/video')
            await event.reply('Hey!')

    def get_client(self):
        return self.client

    def start(self):
        print('(Press Ctrl+C to stop this)')
        self.client.run_until_disconnected()
