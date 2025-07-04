def invest(amount, rate, years):
    for year in range(1, years+1):
        amount *= (1+rate)
        print(f"year {year}: ${amount:.2f}")
    return amount

invest(100, 0.05, 4)