from polygon import RESTClient

client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")  # POLYGON_API_KEY environment variable is used

aggs = []
for a in client.list_aggs(
    "NIO",
    1,
    "day",
    "2024-01-03",
    "2025-01-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)
