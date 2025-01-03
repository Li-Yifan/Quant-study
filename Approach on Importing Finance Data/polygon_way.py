from polygon import RESTClient

client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "minute",
    "2022-01-01",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)


## python3.12 polygon_way.py   
