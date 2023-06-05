import datetime

# Unix timestamp string
unix_timestamp_string = "1622874915"

# Convert Unix timestamp string to datetime object
unix_timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp_string))

# Convert datetime object to readable date string
readable_date = unix_timestamp.strftime("%Y-%m-%d %H:%M:%S")

# Print the readable date
print("Readable date:", readable_date)
