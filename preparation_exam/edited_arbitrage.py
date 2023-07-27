from math import log

def bellman_ford(graph, start, target_currency):
    distances = {currency: float('inf') for currency in graph}
    distances[start] = 0
    parents = {currency: None for currency in graph}

    for _ in range(len(graph) - 1):
        for source in graph:
            for destination, price in graph[source].items():
                if distances[source] + log(price) < distances[destination]:
                    distances[destination] = distances[source] + log(price)
                    parents[destination] = source

    # Check for negative-weight cycles (arbitrage opportunity)
    arbitrage_currencies = [target_currency]
    for source in graph:
        for destination, price in graph[source].items():
            if distances[source] + log(price) < distances[destination]:
                currency = destination
                while currency not in arbitrage_currencies:
                    arbitrage_currencies.append(currency)
                    currency = parents[currency]
                # Check if the cycle starts and ends with the target currency
                if currency == target_currency:
                    cycle_start = currency
                    break
                else:
                    arbitrage_currencies = [target_currency]

    if len(arbitrage_currencies) > 1:
        cycles = []
        for currency in set(arbitrage_currencies):
            cycle_currencies = []
            while True:
                cycle_currencies.append(currency)
                currency = parents[currency]
                if currency == cycle_start:
                    cycle_currencies.append(cycle_start)
                    break
            cycles.append(cycle_currencies[::-1])

        # Filter out paths that don't start and end with the target currency
        best_arbitrage_paths = [path for path in cycles if path[0] == target_currency and path[-1] == target_currency]

        return True, distances, best_arbitrage_paths
    else:
        return False, distances, None

def format_price(price):
    return "{:.3f}".format(price)

def solve_arbitrage_task(trading_pairs, target_currency):
    graph = {}
    currencies = set()
    for pair in trading_pairs:
        from_currency, to_currency, price = pair
        price = float(price)
        currencies.add(from_currency)
        currencies.add(to_currency)
        if from_currency not in graph:
            graph[from_currency] = {}
        graph[from_currency][to_currency] = price

    arbitrage_exists, distances, arbitrage_paths = bellman_ford(graph, target_currency, target_currency)

    if arbitrage_exists:
        print("True")
        print("Currency exchange rates to achieve the opportunity:")
        for source in graph:
            for destination, price in graph[source].items():
                if distances[source] + log(price) < distances[destination]:
                    print(f"{source} -> {destination}: {price:.2f}")

        print("Best arbitrage paths:")
        for path in arbitrage_paths:
            print(" -> ".join(path))
    else:
        print("False")
        for currency in currencies:
            if currency == target_currency:
                continue
            print(f"{currency}: {format_price(distances[currency])}")

# Example usage in the main function:
if __name__ == "__main__":
    n = 5
    trading_pairs = [
        ['GBP', 'USD', '1.27'],
        ['USD', 'AUD', '1.43'],
        ['USD', 'NZD', '1.51'],
        ['NZD', 'AUD', '0.95'],
        ['AUD', 'GBP', '0.55']
    ]
    target_currency = 'GBP'

    solve_arbitrage_task(trading_pairs, target_currency)
