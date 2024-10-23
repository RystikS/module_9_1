def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        if func == max:
            results[func.__name__] = max(int_list)
        elif func == min:
            results[func.__name__] = min(int_list)
        elif func == len:
            results[func.__name__] = len(int_list)
        elif func == sum:
            results[func.__name__] = sum(int_list)
        if func == sorted:
            results[func.__name__] = sorted(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
