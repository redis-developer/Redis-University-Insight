import redis
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query
import time

# Connect to Redis
client = redis.Redis(
  host='localhost',
  port=6379)


def find_bikes_with_keys():
    start = time.time()
    bike_keys = client.keys("bike:*")
    new_affordable_bikes = []
    for key in bike_keys:
        bike_data = client.json().get(key)
        if bike_data.get('condition') == 'new' and bike_data.get('price') < 1000:
            new_affordable_bikes.append(key)
    end = time.time()
    runtime = end - start
    return new_affordable_bikes, runtime

# Fetch the bikes with "new" condition using KEYS
new_affordable_bikes, runtime = find_bikes_with_keys()
print(f"Affordable bikes with 'new' condition using KEYS:{len(new_affordable_bikes)}")
print(f"Time taken: {runtime}")