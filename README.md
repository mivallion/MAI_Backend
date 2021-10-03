# MAI_Backend

## Тестирование через ab:
```bash
$ ab -n 10 -c 2 -t 1 -v 2 http://193.108.113.188/
...
Finished 145 requests


Server Software:        nginx/1.21.3
Server Hostname:        193.108.113.188
Server Port:            80

Document Path:          /cat
Document Length:        0 bytes

Concurrency Level:      2
Time taken for tests:   1.001 seconds
Complete requests:      145
Failed requests:        0
Non-2xx responses:      145
Total transferred:      36395 bytes
HTML transferred:       0 bytes
Requests per second:    144.85 [#/sec] (mean)
Time per request:       13.807 [ms] (mean)
Time per request:       6.904 [ms] (mean, across all concurrent requests)
Transfer rate:          35.51 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        4    5   1.5      5      16
Processing:     5    8   5.3      7      54
Waiting:        5    8   5.3      7      53
Total:          9   13   5.8     12      62

Percentage of the requests served within a certain time (ms)
  50%     12
  66%     13
  75%     14
  80%     14
  90%     17
  95%     19
  98%     25
  99%     54
 100%     62 (longest request)
```
Вывод по тестированию - по какой-то причине ab не поддерживает auto redirects.
