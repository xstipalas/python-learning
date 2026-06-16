def convert_time(time: str | int, reverse=False):
    if reverse:
        oth, s = divmod(time, 60)
        h, m = divmod(oth, 60)
        
        return f'{int(h):02}|{int(m):02}|{int(s):02}'
    else:
        h, m, s = map(int, time.split('|'))
    
        return (h * 60 + m) * 60 + s

def stat(strg):
    if not strg:
        return ''
    
    runners = list(sorted(convert_time(runner) for runner in strg.split(',')))
    runners_count = len(runners)
    
    range = runners[-1] - runners[0]
    average = sum(runners) / runners_count
    median = (runners[(runners_count - 1) // 2] + runners[runners_count // 2]) / 2
    
    return f'Range: {convert_time(range, reverse=True)} Average: {convert_time(average, reverse=True)} Median: {convert_time(median, reverse=True)}'