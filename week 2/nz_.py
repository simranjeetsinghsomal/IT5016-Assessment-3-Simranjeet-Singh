
amount_to_convert = 500 

nz_to_aus_rate = 0.95
nz_dollars = amount_to_convert

aus_dollars = nz_dollars*nz_to_aus_rate
nz_dollars = aus_dollars / nz_to_aus_rate
print(nz_dollars)