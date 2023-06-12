#!/bin/bash

set -eo pipefail

REPETITIONS="$1"
if [ -z "$REPETITIONS" ]; then
  REPETITIONS=10
fi

for index in $(seq 1 "$REPETITIONS"); do
  \time -f %e python -m main
done 2>results.txt

# Use R to print out stats on the collected results
R -q -e "x <- read.csv('results.txt', header = F); summary(x); sd(x[ , 1])"
