def convert_minutes(minutes):
    days = minutes // (24 * 60)
    minutes_remaining = minutes % (24 * 60)
    hours = minutes_remaining // 60
    minutes %= 60

    return f"{days:02d}:{hours:02d}:{minutes:02d}"

minutes = int(input('Введите количество минту: '))
result = convert_minutes(minutes)
print(result)