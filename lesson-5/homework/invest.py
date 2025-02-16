def invest(amount, rate, years):
    for year in range(1,years+1):
        a = amount*(1+rate)**year
        print(f"year {year}: ${a:.2f}")
invest(100, .05, 4)