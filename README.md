# newrelic-python-agent-graphql-issue

## Setup

1. Clone and `docker build`

```bash
git clone https://github.com/tdg5/newrelic-python-agent-graphql-issue.git
cd newrelic-python-agent-graphql-issue
docker build -t newrelic-python-agent-graphql-issue .
```

2. Test run without `NEW_RELIC_LICENSE_KEY`

```bash
docker run --rm newrelic-python-agent-graphql-issue
```

3. Test run with `NEW_RELIC_LICENSE_KEY`

```bash
read NEW_RELIC_LICENSE_KEY
# paste New Relic license key and press enter

docker run --rm --env "NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY" newrelic-python-agent-graphql-issue
```
