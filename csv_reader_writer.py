import csv

input_file_name = ""
write_file_location = ""

csv_file_handle = open(input_file_name, 'rbU')
file_reader = csv.DictReader(csv_file_handle)

headers = ['first_name', 'last_name']
write_file_handle = open(input_file_name, 'rbU')
writer = csv.DictWriter(write_file_handle, fieldnames=headers)

for row in file_reader:
    print row['phone_number']
    writer.writerow({'first_name': "fsa", 'last_name': "sadfsdaf"})
