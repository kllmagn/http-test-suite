FROM python:3.9-bullseye

# исправление для swf 
# меняем vnd.adobe.flash.movie на application/x-shockwave-flash в mime.types
RUN sed -i 's/vnd.adobe.flash.movie/x-shockwave-flash/g' /etc/mime.types

COPY httptest /var/www/html/httptest
COPY . .

EXPOSE 8080

CMD python3 main.py