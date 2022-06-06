import sys
import csv


def get_filename():
  argv = sys.argv
  # One argument: the csv file
  if len(argv) != 2:
    sys.exit("Invalid number of arguments. Program takes csv file as single argument.")
  return argv[1]


def validate_col_filter(csv_filter):
  return csv_filter == "first_name" or csv_filter == "last_name" or csv_filter == "dob"


def get_col_filter():
  while True:
    col_filter = input("Enter column filter (first_name/last_name/dob): ")
    col_filter = col_filter.lower().strip()
    if validate_col_filter(col_filter):
      break
    print("Invalid column filter. Valid options: first_name, last_name, dob")
  return col_filter


def get_name_filter(col_filter):
  return input("Enter filter for " + col_filter + " (case-sensitive): ")


def validate_dob_filter(dob_filter):
  return len(dob_filter) == 8 and dob_filter.isdecimal()


def get_dob_filter(col_filter):
  while True:
    dob_filter = input("Enter filter for " + col_filter + " (YYYYMMDD): ")
    dob_filter = dob_filter.lower()
    if validate_dob_filter(dob_filter):
      break
    print("Invalid filter for " + col_filter + ". Filter must contain only digits and format YYYYMMDD.")
  return dob_filter


def get_csv_filter(col_filter):
  if col_filter == "first_name" or col_filter == "last_name":
    csv_filter = get_name_filter(col_filter)
  elif col_filter == "dob":
    csv_filter = get_dob_filter(col_filter)
  return csv_filter


if __name__ == "__main__":
  filename = get_filename()

  try:
    csv_file = open(filename, mode="r")
    csv_reader = csv.reader(csv_file, delimiter=",")
  except FileNotFoundError:
    sys.exit("File not found: " + filename)

  col_filter = get_col_filter()
  if col_filter == "first_name":
    col_index = 0
  elif col_filter == "last_name":
    col_index = 1
  elif col_filter == "dob":
    col_index = 2
  
  csv_filter = get_csv_filter(col_filter)

  matching = []

  index = 0
  for row in csv_reader:
    # skip first row
    if index != 0:
      if row[col_index] == csv_filter:
        matching.append(row)
    index += 1
  

  if len(matching) == 0:
    print("No matching records.")
  else:
    # print out all matching lines
    for line in matching:
      print(",".join(line))

  csv_file.close()


