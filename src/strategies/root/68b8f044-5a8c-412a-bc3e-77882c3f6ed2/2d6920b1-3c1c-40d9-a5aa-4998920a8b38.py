#2d6920b1-3c1c-40d9-a5aa-4998920a8b38



def strategy(data, params):
    signals = []
    but_threshold = 30
    sell_threshold = 70
    for (index, rsi_metric) in enumerate(data):
        if rsi_metric < but_threshold:
            signals.append({'index': index, 'signal': 'buy'})
        elif rsi_metric > sell_threshold:
            signals.append({'index': index, 'signal': 'sell'})
    return signals





