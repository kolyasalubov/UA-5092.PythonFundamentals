def count_symbols(text: str) -> dict[str, int]:
    """
    Count occurrences of each distinct symbol.
    input parameters: text - str
    output: dict[str, int] sorted by value DESC
    """
    if not isinstance(text, str):
        raise TypeError("'Text' argument should be str data type.")

    if not text:
        return {}

    symbols = set(text)
    result = {symbol: text.count(symbol) for symbol in symbols}

    if len(symbols) == 1:
        return result

    sorted_result = dict(sorted(result.items(),
                                key=lambda x: x[1],
                                reverse=True))

    return sorted_result


count_symbols("Aaaa!..") #{{'a': 3, '.': 2, 'A': 1, '!': 1}
count_symbols("") #{}
count_symbols(" ") #{' ': 1}
