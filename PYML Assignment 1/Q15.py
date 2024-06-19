import csv

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Example usage:
if __name__ == "__main__":
    csv_file = 'data.csv'  # Replace with your CSV file path
    read_csv_file(csv_file)
