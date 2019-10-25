from datadog import initialize, statsd
import time

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

i = 0

while True:
    i += 1
    statsd.increment("bubble.tea.count", tags=["hello:fargate"])
    statsd.gauge("bubble.tea.gauge", i, tags=["hello:fargate"])
    time.sleep(10)
