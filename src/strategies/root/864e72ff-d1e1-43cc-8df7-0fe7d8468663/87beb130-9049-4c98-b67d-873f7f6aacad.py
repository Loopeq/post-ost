#87beb130-9049-4c98-b67d-873f7f6aacad



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





