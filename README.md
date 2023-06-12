# newrelic-python-agent-graphene-issue

## Setup

1. Clone and `docker build`

```bash
git clone https://github.com/tdg5/newrelic-python-agent-graphene-issue.git
cd newrelic-python-agent-graphene-issue
docker build -t newrelic-python-agent-graphene-issue .
```

2. Test run without `NEW_RELIC_LICENSE_KEY`

```bash
docker run --rm newrelic-python-agent-graphene-issue
```

Example results from running 10 invocations * 100 queries:

```
Min.   :0.60
1st Qu.:0.60
Median :0.61
Mean   :0.63
3rd Qu.:0.61
Max.   :0.85
```

3. Test run with `NEW_RELIC_LICENSE_KEY`

```bash
read NEW_RELIC_LICENSE_KEY
# paste New Relic license key and press enter

docker run --rm --env "NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY" newrelic-python-agent-graphene-issue
```

Example results from running 10 invocations * 100 queries:
```
Min.   :1.580
1st Qu.:1.623
Median :1.640
Mean   :1.677
3rd Qu.:1.667
Max.   :2.060
```
