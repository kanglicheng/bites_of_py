def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    if not sequence:
        return []
    running_avg = [0]*len(sequence)
    running_avg[0] = sequence[0]
    for i, n in enumerate(sequence):
        if i == 0:
            continue
        running_avg[i] = sequence[i] + running_avg[i-1]
    for i, n in enumerate(running_avg):
        if i == 0:
            continue
        running_avg[i] = round(running_avg[i]/(i+1), 2)
    return running_avg

print(running_mean([2, 6, 10, 8, 11, 10]))


# official solution
def running_mean_old(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    if not sequence:
        return []

    total = 0
    running_mean = []

    for i, num in enumerate(sequence, 1):
        total += num
        mean = round(total/i, 2)
        running_mean.append(mean)

    return running_mean


def running_mean(sequence):
    """Same functionality as above but using itertools.accumulate
       and turning it into a generator"""
    for i, num in enumerate(accumulate(sequence), 1):
        yield round(num/i, 2)
