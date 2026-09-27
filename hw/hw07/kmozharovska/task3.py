import re


def count_symbols(text: str) -> dict[str, int]:
    """
    Count occurrences of each distinct symbol.
    Args: text - str
    Returns: dict[str, int] sorted by value DESC
    """
    if not text:
        return {}

    symbols = list(set(text))
    result = {symbol: text.count(symbol) for symbol in symbols}

    if len(symbols) == 1:
        return result

    sorted_result = dict(sorted(result.items(),
                                key=lambda x: x[1],
                                reverse=True))

    return sorted_result


if __name__ == "__main__":
    text = input("Enter your text: ")
    symbols_frequency = count_symbols(text)

    if symbols_frequency:
        print("In your text:")
        for symbol, frequency in symbols_frequency.items():
            pattern = r"^\s$"
            if bool(re.match(pattern, symbol)):
                print(f"there are {frequency} whitespaces")
            else:
                print(f"{symbol} is mentioned {frequency} time(s)")
    else:
        print("Text wasn't provided.")
