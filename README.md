# Домашнее задание № 2

## Веб сервер
- язык: Python
- архитектура: fork per request

## Построение образов и запуск контейнеров
```
docker build -t basic_server -f Dockerfile .
docker run -d --network=host basic_server

docker build -t nginx_server -f nginx.Dockerfile .
docker run -d --network=host nginx_server
```

## Функциональное тестирование
```
./httptest.py localhost 8080

```

## Нагрузочное тестирование
### Python: fork per request (basic_server)
```
(base) kllmagn@MacBook-Pro-Roman http-test-suite % ab -n 10000 -c 10 127.0.0.1:8080/httptest/wikipedia_russia.html

```

### Nginx (nginx_server)
```
(base) kllmagn@MacBook-Pro-Roman http-test-suite % ab -n 10000 -c 10 127.0.0.1:3030/httptest/wikipedia_russia.html


```