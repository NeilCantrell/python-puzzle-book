def count_peaks_valleys(price_action):
    peaks = 0
    valleys = 0
    for i in range(1, len(price_action)-1):
        if price_action[i-1] < price_action[i] > price_action[i+1]:
            peaks += 1
        elif price_action[i-1] > price_action[i] < price_action[i+1]:
            valleys += 1
    return peaks, valleys


price_action = [1, 2, 3, 2, 1]
print(count_peaks_valleys(price_action))

price_action = [1, 2, 3, 2, 1, 2]
print(count_peaks_valleys(price_action))