FROM nginx:1.23.2

WORKDIR /etc/nginx

#COPY mime.types mime.types
COPY nginx.conf /etc/nginx/nginx.conf
COPY httptest /etc/nginx/static/httptest