import csv
import os

source_filename = os.path.join(os.getcwd(), "test_files/names.csv")

dirname, filename = os.path.split(source_filename)

new_filename = os.path.join(dirname, "new_names.csv")


with open(source_filename, "r") as csv_file:

    csv_reader = csv.reader(csv_file)

    with open(new_filename, "w") as new_csv_file:

        csv_writer = csv.writer(new_csv_file, delimiter="\t")

        # next(csv_reader)  # skip the header

        for line in csv_reader:

            csv_writer.writerow(line)

with open(source_filename, "r") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    with open(new_filename, "w") as new_csv_file:

        csv_writer = csv.DictWriter(new_csv_file, csv_reader.fieldnames, delimiter="\t")

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

with open(source_filename, "r") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    with open(new_filename, "w") as new_csv_file:

        # remove email column

        csv_writer = csv.DictWriter(
            new_csv_file, ["first_name", "last_name"], delimiter="\t"
        )

        csv_writer.writeheader()

        for line in csv_reader:
            del line["email"]
            csv_writer.writerow(line)
