docker run -d -p 8080:80 -v /nextcloud/apps:/var/www/html/custom_apps -v /nextcloud/config:/var/www/html/config -v /nextcloud/data:/var/www/html/data  --privileged=true nextcloud    

docker run -d -v /nextcloud/data/tg_bot/files/tg_video:/data/down -v/root/tg-bot:/var/app --privileged=true tg-bot/v1
