import redis
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query
from redis.commands.search.aggregation import AggregateRequest, Reducer
import time

# Connect to Redis
client = redis.Redis(
  host='localhost',
  port=6379)

# If no index is created yet, create the index
def create_bike_index():
    # Define the schema for the index
    schema = (
        TextField("$.brand", as_name="brand"),
        TextField("$.model", as_name="model"),
        NumericField("$.price", as_name="price"),
        TagField("$.condition", as_name="condition")
    )

    # Create the index
    index = client.ft("idx:bikes")
    index.create_index(
        schema,
        definition=IndexDefinition(prefix=["bike:"], index_type=IndexType.JSON)
    )

def search_bikes_with_condition():
    start = time.time()
    query = "@condition:{new} @price:[-inf (1000]"
    new_affordable_bikes = client.ft('idx:bikes').search(query)
    end = time.time()
    runtime = end - start
    return new_affordable_bikes, runtime

# Create the index (only needs to be done once)
create_bike_index()
time.sleep(12)
# Search for bikes with "new" condition using RediSearch
new_affordable_bikes, runtime = search_bikes_with_condition()
print("Affordable bikes with 'new' condition using RediSearch:", new_affordable_bikes.total)
print(f"Time taken: {runtime}")