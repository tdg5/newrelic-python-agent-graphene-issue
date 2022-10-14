import json


# A very solid reference config can be found here:
# https://github.com/bynect/hypercorn-fastapi-docker/blob/main/images/hypercorn_conf.py

bind = "0.0.0.0:8000"

# This object is just for output. Hypercorn will get it's conf from the
# primitives defined above.
conf_data = {
    "bind": bind,
}

# Print out the conf for debugging visibility
print(json.dumps(conf_data, indent=4), flush=True)
