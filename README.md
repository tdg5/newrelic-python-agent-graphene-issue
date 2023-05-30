# Sample project

1. Setup

Create `.env` file:

```bash
cp env-template .env
```

2. Update `.env` to add value for `NEW_RELIC_LICENSE_KEY`

3. Run the demo app:

```bash
docker-compose build && docker-compose up
```

4. Send a single request to warm up the app:

```bash
curl -H 'Content-Type: application/json' -d '@query.json' http://localhost:9000/graphql
```

4. Send lots of requests to app using `apache-bench`:

```bash
ab -n 1000 -c 1 -T 'application/json' -p query.json http://localhost:9000/graphql
```

## RESULTS WITHOUT NEW_RELIC_LICENSE_KEY

```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            9000

Document Path:          /graphql
Document Length:        48520 bytes

Concurrency Level:      1
Time taken for tests:   6.674 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      48667000 bytes
Total body sent:        405000
HTML transferred:       48520000 bytes
Requests per second:    149.84 [#/sec] (mean)
Time per request:       6.674 [ms] (mean)
Time per request:       6.674 [ms] (mean, across all concurrent requests)
Transfer rate:          7121.28 [Kbytes/sec] received
                        59.26 kb/s sent
                        7180.54 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     6    7   0.7      7      23
Waiting:        6    7   0.7      6      22
Total:          6    7   0.7      7      23
WARNING: The median and mean for the waiting time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%      7
  66%      7
  75%      7
  80%      7
  90%      7
  95%      7
  98%      7
  99%      8
 100%     23 (longest request)
```

## RESULTS WITH NEW_RELIC_LICENSE_KEY (OUCH)

```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            9000

Document Path:          /graphql
Document Length:        48520 bytes

Concurrency Level:      1
Time taken for tests:   96.852 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      48667000 bytes
Total body sent:        405000
HTML transferred:       48520000 bytes
Requests per second:    10.33 [#/sec] (mean)
Time per request:       96.852 [ms] (mean)
Time per request:       96.852 [ms] (mean, across all concurrent requests)
Transfer rate:          490.71 [Kbytes/sec] received
                        4.08 kb/s sent
                        494.80 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:    89   97  10.0     91     143
Waiting:       78   85   9.4     80     122
Total:         89   97  10.0     91     143

Percentage of the requests served within a certain time (ms)
  50%     91
  66%     93
  75%    105
  80%    110
  90%    113
  95%    115
  98%    121
  99%    127
 100%    143 (longest request)
```
