def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False




time = int(input("What year?: "))
print(f"The year {time}\nIs leap year: {is_leap(time)}")