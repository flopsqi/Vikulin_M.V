def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds_remaining = seconds % (24 * 3600)
    hours = seconds_remaining // 3600
    seconds_remaining %= 3600
    minutes = seconds_remaining // 60
    seconds_remaining %= 60

    return f"{days}:{hours:02d}:{minutes:02d}:{seconds_remaining:02d}"

seconds = 100000
result = convert_seconds(seconds)
print(result)