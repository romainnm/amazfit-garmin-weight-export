import os
import csv

def convert_weight_amazfit_garmin(file):
    print("Starting file processing")

    # file_path = os.path.join(file)

    filtered_data = [
        ['Body'],
        ['Date', 'Weight', 'BMI', 'Fat']
    ]


    with open(file, 'r', encoding='utf8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        next(reader)


        for row in reader:
            if row[2].strip() == '162' or row[2].strip() == '162.0':
                continue

            date = row[0][:10]
            weight = float(row[1])*2.205
            formatted_weight = f"{weight:.1f}"
            filtered_data.append([date, formatted_weight, 0, 0])
            print(f"Adding row with date: {date}, weight: {formatted_weight}, BMI: 0, Fat: 0")

    with open('export.csv', 'w', newline="", encoding='utf8') as output:
        writer = csv.writer(output)
        writer.writerows(filtered_data)


if __name__ == "__main__":
    convert_weight_amazfit_garmin('amazfit-body-history.csv')