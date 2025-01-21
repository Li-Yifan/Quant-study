# list_aggs return a list of info for option O:NIO250131C00005000

from polygon import RESTClient
from datetime import datetime


client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")

aggs = []
for a in client.list_aggs(
    "O:NIO250131C00005000",
    1,
    "minute",
    "2025-01-03",
    "2025-01-03",
    limit=5000,
):
    aggs.append(a)

print(aggs[2].open)


# [Agg(open=0.48, high=0.49, low=0.48, close=0.49, volume=34, vwap=0.4865, timestamp=1733979600000, transactions=12, otc=None),
# Agg(open=0.36, high=0.39, low=0.35, close=0.35, volume=12, vwap=0.3717, timestamp=1734066000000, transactions=8, otc=None),
# Agg(open=0.38, high=0.38, low=0.31, close=0.33, volume=98, vwap=0.351, timestamp=1734325200000, transactions=30, otc=None),
# Agg(open=0.32, high=0.39, low=0.32, close=0.35, volume=222, vwap=0.3514, timestamp=1734411600000, transactions=46, otc=None),
# Agg(open=0.34, high=0.35, low=0.22, close=0.28, volume=98, vwap=0.3127, timestamp=1734498000000, transactions=36, otc=None),
# Agg(open=0.29, high=0.33, low=0.29, close=0.3, volume=1550, vwap=0.3269, timestamp=1734584400000, transactions=52, otc=None),
# Agg(open=0.33, high=0.35, low=0.3, close=0.33, volume=502, vwap=0.3116, timestamp=1734670800000, transactions=84, otc=None),
# Agg(open=0.3, high=0.31, low=0.26, close=0.26, volume=2640, vwap=0.2674, timestamp=1734930000000, transactions=144, otc=None),
# Agg(open=0.26, high=0.3, low=0.19, close=0.26, volume=3966, vwap=0.2379, timestamp=1735016400000, transactions=126, otc=None),
# Agg(open=0.27, high=0.37, low=0.25, close=0.29, volume=634, vwap=0.3128, timestamp=1735189200000, transactions=132, otc=None),
# Agg(open=0.19, high=0.25, low=0.19, close=0.22, volume=884, vwap=0.2183, timestamp=1735275600000, transactions=92, otc=None),
# Agg(open=0.17, high=0.2, low=0.16, close=0.17, volume=1570, vwap=0.1819, timestamp=1735534800000, transactions=218, otc=None),
# Agg(open=0.18, high=0.21, low=0.14, close=0.15, volume=5088, vwap=0.17, timestamp=1735621200000, transactions=210, otc=None),
# Agg(open=0.17, high=0.26, low=0.15, close=0.18, volume=3982, vwap=0.1858, timestamp=1735794000000, transactions=332, otc=None),
# Agg(open=0.19, high=0.21, low=0.15, close=0.2, volume=2584, vwap=0.1799, timestamp=1735880400000, transactions=264, otc=None)]

# timestamp is unix timestamp, Unix time is a system for representing timestamps as the number of seconds that have elapsed since January 1, 1970
# use function below to do transfermation
# from datetime import datetime
# timestamp=int('1735880400000')/1000
# print(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
