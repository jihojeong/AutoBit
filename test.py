import pyupbit as pu
access = "gFpmgg7Bq6x3dtZdVx3ZseNGx3hSw9TDt4rCkZ0x"
secret = "ELEf0e8omG7x0d9GpIYPwXg1c84EWV7lybSK2jET"
upbit = pu.Upbit(access,secret)
print(upbit.get_balance("KRW-BTC"))  
print(upbit.get_balance("KRW"))         # 보유 현금 조회