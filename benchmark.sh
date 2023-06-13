#!/bin/bash

set -eo pipefail

\time -f %e python -m main 2>&1
