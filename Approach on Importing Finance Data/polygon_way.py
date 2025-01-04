
from polygon import RESTClient

client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")
ticker = "NIO"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_="2023-01-01", to="2023-06-13", limit=50):
    aggs.append(a)

print(aggs)
## python3.12 polygon_way.py
