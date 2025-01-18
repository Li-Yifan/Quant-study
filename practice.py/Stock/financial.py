from polygon import RESTClient

client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")

financials = client.get_ticker_details("NFLX")
print(financials)

for i, n in enumerate(client.list_ticker_news("INTC", limit=5)):
    print(i, n)
    if i == 5:
        break
