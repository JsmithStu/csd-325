import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

FILENAME = "sitka_weather_2018_simple.csv"


def load_weather_data(filename):
    """Load dates, high temps, and low temps from the CSV file."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header row

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                # skip rows with missing/bad data
                continue

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_temps(dates, temps, title, color):
    """Plot a list of temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(title, fontsize=20)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis="both", which="major", labelsize=12)

    plt.show()


def print_menu():
    print("\n=== Sitka Weather Menu ===")
    print("H - Show high temperatures")
    print("L - Show low temperatures")
    print("E - Exit")


def main():
    # Load the data once
    dates, highs, lows = load_weather_data(FILENAME)

    # Loop until user exits
    while True:
        print_menu()
        choice = input("Enter your choice (H/L/E): ").strip().lower()

        if choice in ("h", "high", "highs"):
            print("Showing high temperatures...")
            plot_temps(dates, highs, "Daily HIGH temperatures - 2018", "red")

        elif choice in ("l", "low", "lows"):
            print("Showing low temperatures...")
            plot_temps(dates, lows, "Daily LOW temperatures - 2018", "blue")

        elif choice in ("e", "exit"):
            print("Thanks for using the Sitka Weather Viewer. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please type H, L, or E.")


if __name__ == "__main__":
    main()
