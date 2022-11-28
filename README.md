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

2022-11-28T12:54:29.1385187Z test_directory_index (__main__.HttpServer)
2022-11-28T12:54:29.1461065Z directory index file exists ... ok
2022-11-28T12:54:29.1461377Z test_document_root_escaping (__main__.HttpServer)
2022-11-28T12:54:29.1468041Z document root escaping forbidden ... ok
2022-11-28T12:54:29.1468364Z test_empty_request (__main__.HttpServer)
2022-11-28T12:54:29.1474377Z Send empty line ... ok
2022-11-28T12:54:29.1476261Z test_file_in_nested_folders (__main__.HttpServer)
2022-11-28T12:54:29.1523717Z file located in nested folders ... ok
2022-11-28T12:54:29.1528753Z test_file_not_found (__main__.HttpServer)
2022-11-28T12:54:29.1530668Z absent file returns 404 ... ok
2022-11-28T12:54:29.1531108Z test_file_type_css (__main__.HttpServer)
2022-11-28T12:54:29.1538204Z Content-Type for .css ... ok
2022-11-28T12:54:29.1538464Z test_file_type_gif (__main__.HttpServer)
2022-11-28T12:54:29.1551218Z Content-Type for .gif ... ok
2022-11-28T12:54:29.1551481Z test_file_type_html (__main__.HttpServer)
2022-11-28T12:54:29.1558993Z Content-Type for .html ... ok
2022-11-28T12:54:29.1559258Z test_file_type_jpeg (__main__.HttpServer)
2022-11-28T12:54:29.1564522Z Content-Type for .jpeg ... ok
2022-11-28T12:54:29.1564820Z test_file_type_jpg (__main__.HttpServer)
2022-11-28T12:54:29.1575582Z Content-Type for .jpg ... ok
2022-11-28T12:54:29.1581589Z test_file_type_js (__main__.HttpServer)
2022-11-28T12:54:29.1583241Z Content-Type for .js ... ok
2022-11-28T12:54:29.1583698Z test_file_type_png (__main__.HttpServer)
2022-11-28T12:54:29.1589655Z Content-Type for .png ... ok
2022-11-28T12:54:29.1590089Z test_file_type_swf (__main__.HttpServer)
2022-11-28T12:54:29.1595759Z Content-Type for .swf ... ok
2022-11-28T12:54:29.1596046Z test_file_urlencoded (__main__.HttpServer)
2022-11-28T12:54:29.1605678Z urlencoded filename ... ok
2022-11-28T12:54:29.1606160Z test_file_with_dot_in_name (__main__.HttpServer)
2022-11-28T12:54:29.1611476Z file with two dots in name ... ok
2022-11-28T12:54:29.1611781Z test_file_with_query_string (__main__.HttpServer)
2022-11-28T12:54:29.1617670Z query string with get params ... ok
2022-11-28T12:54:29.1617989Z test_file_with_slash_after_filename (__main__.HttpServer)
2022-11-28T12:54:29.1623687Z slash after filename ... ok
2022-11-28T12:54:29.1624233Z test_file_with_spaces (__main__.HttpServer)
2022-11-28T12:54:29.1629519Z filename with spaces ... ok
2022-11-28T12:54:29.1629796Z test_head_method (__main__.HttpServer)
2022-11-28T12:54:29.1635917Z head method support ... ok
2022-11-28T12:54:29.1636339Z test_index_not_found (__main__.HttpServer)
2022-11-28T12:54:29.1641545Z directory index file absent ... ok
2022-11-28T12:54:29.1641830Z test_large_file (__main__.HttpServer)
2022-11-28T12:54:29.1658768Z large file downloaded correctly ... ok
2022-11-28T12:54:29.1659219Z test_post_method (__main__.HttpServer)
2022-11-28T12:54:29.1664767Z post method forbidden ... ok
2022-11-28T12:54:29.1665077Z test_request_without_two_newlines (__main__.HttpServer)
2022-11-28T12:54:29.1668980Z Send GET without to newlines ... ok
2022-11-28T12:54:29.1669318Z test_server_header (__main__.HttpServer)
2022-11-28T12:54:29.1674457Z Server header exists ... ok
2022-11-28T12:54:29.1674777Z 
2022-11-28T12:54:29.1675197Z ----------------------------------------------------------------------
2022-11-28T12:54:29.1675899Z Ran 24 tests in 0.029s
2022-11-28T12:54:29.1676209Z 
2022-11-28T12:54:29.1762160Z OK
```

## Нагрузочное тестирование
### Python: fork per request (basic_server)
```
(base) kllmagn@MacBook-Pro-Roman http-test-suite % ab -n 10000 -c 10 127.0.0.1:8080/httptest/wikipedia_russia.html

2022-11-28T12:54:29.2616852Z This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
2022-11-28T12:54:29.2618706Z Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
2022-11-28T12:54:29.2619948Z Licensed to The Apache Software Foundation, http://www.apache.org/
2022-11-28T12:54:29.2620516Z 
2022-11-28T12:54:29.2620626Z Benchmarking 127.0.0.1 (be patient)
2022-11-28T12:54:29.8378555Z Completed 1000 requests
2022-11-28T12:54:30.4008566Z Completed 2000 requests
2022-11-28T12:54:30.9140235Z Completed 3000 requests
2022-11-28T12:54:31.4131166Z Completed 4000 requests
2022-11-28T12:54:31.9234608Z Completed 5000 requests
2022-11-28T12:54:32.3650920Z Completed 6000 requests
2022-11-28T12:54:32.7768098Z Completed 7000 requests
2022-11-28T12:54:33.1805448Z Completed 8000 requests
2022-11-28T12:54:33.5830817Z Completed 9000 requests
2022-11-28T12:54:33.9632542Z Completed 10000 requests
2022-11-28T12:54:33.9633315Z Finished 10000 requests
2022-11-28T12:54:33.9707669Z 
2022-11-28T12:54:33.9707890Z 
2022-11-28T12:54:33.9708346Z Server Software:        Python
2022-11-28T12:54:33.9708638Z Server Hostname:        127.0.0.1
2022-11-28T12:54:33.9708852Z Server Port:            8080
2022-11-28T12:54:33.9708984Z 
2022-11-28T12:54:33.9709123Z Document Path:          /httptest/wikipedia_russia.html
2022-11-28T12:54:33.9709387Z Document Length:        954824 bytes
2022-11-28T12:54:33.9709525Z 
2022-11-28T12:54:33.9709606Z Concurrency Level:      100
2022-11-28T12:54:33.9709829Z Time taken for tests:   4.702 seconds
2022-11-28T12:54:33.9710054Z Complete requests:      10000
2022-11-28T12:54:33.9710258Z Failed requests:        0
2022-11-28T12:54:33.9710494Z Total transferred:      9549800000 bytes
2022-11-28T12:54:33.9710733Z HTML transferred:       9548240000 bytes
2022-11-28T12:54:33.9710971Z Requests per second:    2126.66 [#/sec] (mean)
2022-11-28T12:54:33.9711222Z Time per request:       47.022 [ms] (mean)
2022-11-28T12:54:33.9711512Z Time per request:       0.470 [ms] (mean, across all concurrent requests)
2022-11-28T12:54:33.9711815Z Transfer rate:          1983317.33 [Kbytes/sec] received
2022-11-28T12:54:33.9711964Z 
2022-11-28T12:54:33.9712048Z Connection Times (ms)
2022-11-28T12:54:33.9712483Z               min  mean[+/-sd] median   max
2022-11-28T12:54:33.9712713Z Connect:        0    1   0.5      1       7
2022-11-28T12:54:33.9712924Z Processing:     2   46   8.2     44      76
2022-11-28T12:54:33.9713144Z Waiting:        0    1   2.6      1      34
2022-11-28T12:54:33.9713348Z Total:          4   47   8.3     45      79
2022-11-28T12:54:33.9713464Z 
2022-11-28T12:54:33.9713606Z Percentage of the requests served within a certain time (ms)
2022-11-28T12:54:33.9713850Z   50%     45
2022-11-28T12:54:33.9714024Z   66%     50
2022-11-28T12:54:33.9714174Z   75%     52
2022-11-28T12:54:33.9714328Z   80%     54
2022-11-28T12:54:33.9714486Z   90%     58
2022-11-28T12:54:33.9714632Z   95%     62
2022-11-28T12:54:33.9714789Z   98%     67
2022-11-28T12:54:33.9714946Z   99%     73
2022-11-28T12:54:33.9715117Z  100%     79 (longest request)
```

### Nginx (nginx_server)
```
(base) kllmagn@MacBook-Pro-Roman http-test-suite % ab -n 10000 -c 10 127.0.0.1:3030/httptest/wikipedia_russia.html

2022-11-28T12:54:24.3287989Z This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
2022-11-28T12:54:24.3288854Z Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
2022-11-28T12:54:24.3289263Z Licensed to The Apache Software Foundation, http://www.apache.org/
2022-11-28T12:54:24.3289467Z 
2022-11-28T12:54:24.3289574Z Benchmarking 127.0.0.1 (be patient)
2022-11-28T12:54:24.7437224Z Completed 1000 requests
2022-11-28T12:54:25.1518554Z Completed 2000 requests
2022-11-28T12:54:25.5366437Z Completed 3000 requests
2022-11-28T12:54:25.9196569Z Completed 4000 requests
2022-11-28T12:54:26.3122672Z Completed 5000 requests
2022-11-28T12:54:26.7430559Z Completed 6000 requests
2022-11-28T12:54:27.1256201Z Completed 7000 requests
2022-11-28T12:54:27.5092000Z Completed 8000 requests
2022-11-28T12:54:27.9611304Z Completed 9000 requests
2022-11-28T12:54:28.3936073Z Completed 10000 requests
2022-11-28T12:54:28.3936639Z Finished 10000 requests
2022-11-28T12:54:28.4009655Z 
2022-11-28T12:54:28.4009662Z 
2022-11-28T12:54:28.4009828Z Server Software:        nginx/1.23.2
2022-11-28T12:54:28.4010190Z Server Hostname:        127.0.0.1
2022-11-28T12:54:28.4010591Z Server Port:            3030
2022-11-28T12:54:28.4010814Z 
2022-11-28T12:54:28.4011032Z Document Path:          /httptest/wikipedia_russia.html
2022-11-28T12:54:28.4011401Z Document Length:        954824 bytes
2022-11-28T12:54:28.4011615Z 
2022-11-28T12:54:28.4011777Z Concurrency Level:      100
2022-11-28T12:54:28.4012094Z Time taken for tests:   4.064 seconds
2022-11-28T12:54:28.4012394Z Complete requests:      10000
2022-11-28T12:54:28.4012677Z Failed requests:        0
2022-11-28T12:54:28.4012979Z Total transferred:      9550620000 bytes
2022-11-28T12:54:28.4013297Z HTML transferred:       9548240000 bytes
2022-11-28T12:54:28.4013619Z Requests per second:    2460.40 [#/sec] (mean)
2022-11-28T12:54:28.4013929Z Time per request:       40.644 [ms] (mean)
2022-11-28T12:54:28.4014282Z Time per request:       0.406 [ms] (mean, across all concurrent requests)
2022-11-28T12:54:28.4014663Z Transfer rate:          2294758.48 [Kbytes/sec] received
2022-11-28T12:54:28.4015292Z 
2022-11-28T12:54:28.4015452Z Connection Times (ms)
2022-11-28T12:54:28.4016160Z               min  mean[+/-sd] median   max
2022-11-28T12:54:28.4016465Z Connect:        0    1   0.2      1       4
2022-11-28T12:54:28.4016766Z Processing:    13   40   4.3     38      71
2022-11-28T12:54:28.4017069Z Waiting:        0    1   1.0      1      16
2022-11-28T12:54:28.4017369Z Total:         14   41   4.4     38      72
2022-11-28T12:54:28.4017559Z 
2022-11-28T12:54:28.4017769Z Percentage of the requests served within a certain time (ms)
2022-11-28T12:54:28.4018082Z   50%     38
2022-11-28T12:54:28.4018341Z   66%     39
2022-11-28T12:54:28.4018613Z   75%     42
2022-11-28T12:54:28.4018835Z   80%     45
2022-11-28T12:54:28.4019065Z   90%     47
2022-11-28T12:54:28.4019299Z   95%     48
2022-11-28T12:54:28.4019525Z   98%     52
2022-11-28T12:54:28.4019751Z   99%     58
2022-11-28T12:54:28.4020009Z  100%     72 (longest request)
```