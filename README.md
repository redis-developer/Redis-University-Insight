# Redis-University-Insight
The supplemental files to get the most out Redis University's course on Redis Insight.

### Files:
1. `commands.txt` - adds data for exploring in Redis Insight, removes pre-existing indexes on sample data to show tip when there are no indexes
2. `make_bikes.py` - generates a file called `add_bikes.txt` which, when uploaded to Redis Insight, will add 500,000 JSON documents for bikes
3. `search_slow.py` - uses the `keys` command to perform very slow search
4. `search_fast.py` - uses an index and `ft.search()...` to perform a much faster search

Due to how large the `add_bikes.txt` file ends up crossing GitHubs limit without using large file storage; so, if you want to add 500,000 bike JSONs to a database, you'll need to run the `make_bikes.py` file.
