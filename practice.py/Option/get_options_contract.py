
from polygon import RESTClient
## get_options_contract returns option info 


client = RESTClient("zC4gTZtCcPheJAj2_YYFEeQhYBj0fGRQ")
ticker = "NIO"

contract_name = "O:NIO250131C00005000"

contract = client.get_options_contract(contract_name)

# print raw values
print(contract)

# OptionsContract(additional_underlyings=None, cfi='OCASPS', contract_type='call', correction=None, exercise_style='american',
#  expiration_date='2025-01-31', primary_exchange='BATO', shares_per_contract=100, strike_price=5, ticker='O:NIO250131C00005000',
#  underlying_ticker='NIO')
