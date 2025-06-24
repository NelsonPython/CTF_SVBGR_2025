import csv

filename = "silentsignal.csv"
with open(filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) # Skip the header row

    for row in reader:
        timestamps = []
        differences = []
        last_timestamp = None

        for row in reader:
            if not row:
                continue

            if len(row) > 1: # Ensure 'Time' column (index 1) exists
                time_str = row[1] # Access the second column (index 1) directly
                try:
                    current_timestamp = float(time_str)
                    timestamps.append(current_timestamp)

                    if last_timestamp is not None:
                        diff = current_timestamp - last_timestamp
                        differences.append(int(diff))
                    last_timestamp = current_timestamp
                except ValueError:
                    pass # Skip if timestamp is not a valid number
            else:
                pass # Skip incomplete rows

decoded_string = ''.join(chr(num) for num in differences)
print(decoded_string)

