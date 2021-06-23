# Install Redis Ubuntu
# https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-quickstart-ru


import redis

USERS_FUNDS = {}

result = redis.Redis()

# get
result.get("foo")

# set
result.set("qwe", 123)

# set on time
result.setex("qwerty", 1, "foobar")

# many set
result.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
