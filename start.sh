docker run -d -p 8080:80 -v /nextcloud/apps:/var/www/html/custom_apps -v /nextcloud/config:/var/www/html/config -v /nextcloud/data:/var/www/html/data  --privileged=true nextcloud    
