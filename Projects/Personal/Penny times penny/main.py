def pennytimespenny(days):
    amount = .01
    for day in range(1, days):
        amount = amount * 2

    return amount


result = pennytimespenny(30)
print(f"Total: ${result:,.2f}")




