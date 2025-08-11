# Currency Converter with Enhancements

# Fixed exchange rates (hard-coded)
exchange_rates = {
    'USD': {'EUR': 0.85, 'CAD': 1.25, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'CAD': 1.47, 'GBP': 0.88},
    'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.60},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'CAD': 1.67}
}

# List to store conversion history
conversion_history = []

# Convert a specific amount from source to target currency
def convert_currency(amount, source, target):
    if source in exchange_rates and target in exchange_rates[source]:
        return amount * exchange_rates[source][target]
    return None

# Show conversion to all available target currencies
def show_all_conversions(amount, source):
    if source in exchange_rates:
        print(f"\nEquivalent values for {amount:.2f} {source}:")
        for target in exchange_rates[source]:
            converted = convert_currency(amount, source, target)
            print(f"{converted:.2f} {target}")
    else:
        print("Source currency not supported.")

# Main program loop
def main():
    while True:
        try:
            amount = float(input("\nEnter the amount (or type 0 to quit): "))
            if amount == 0:
                break  # Exit the loop

            source_currency = input("Source currency (USD/EUR/CAD/GBP): ").upper()
            target_currency = input("Target currency (USD/EUR/CAD/GBP or 'ALL'): ").upper()

            # If user wants all conversions
            if target_currency == "ALL":
                show_all_conversions(amount, source_currency)
                for target in exchange_rates.get(source_currency, {}):
                    converted = convert_currency(amount, source_currency, target)
                    conversion_history.append((amount, source_currency, converted, target))
            else:
                # Single conversion
                converted = convert_currency(amount, source_currency, target_currency)
                if converted is not None:
                    print(f"{amount:.2f} {source_currency} is equal to {converted:.2f} {target_currency}")
                    conversion_history.append((amount, source_currency, converted, target_currency))
                else:
                    print("Invalid currency combination.")

        except ValueError:
            print("Invalid input. Please enter numeric values for amount.")

    # Show conversion history
    print("\nConversion History:")
    for record in conversion_history:
        a, src, conv, tgt = record
        print(f"{a:.2f} {src} => {conv:.2f} {tgt}")

# Run the program
main()