weather = {
    'sunny': {'sunny':0.7, 'rainy':0.1, 'cloudy':0.2},
    'rainy': {'sunny':0.1, 'rainy':0.6, 'cloudy':0.3},
    'cloudy': {'sunny':0.2, 'rainy':0.5, 'cloudy':0.3}
    }

def get_next_day(model, today):
    ans = ''
    for e in model:
        if e == today:
            probable = model[e]
            tomorrow = max(list(probable.values()))
            for a in probable:
                if probable[a] == tomorrow:
                    ans = a
    return a

print(get_next_day(weather, 'sunny'))

def get_forecast(model, days, start):
    ans = []
    i = 0
    while i <= days:
        ans.append(get_next_day(model, start))
        i += 1
        start = get_next_day(model, start)
    return ans

print(get_forecast(weather, 10, 'sunny'))


