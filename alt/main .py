# import os
# import csv

# def process_weight_data(input_file='amazfit-body-history.csv', output_file='exportToGarming_weight.csv'):
#     # Open the input file and process it
#     with open(input_file, mode="r", encoding="utf8") as file:
#         reader = csv.reader(file, delimiter=",")
        
#         # Skip the first two header rows
#         next(reader)
#         next(reader)
        
#         # Create output data with headers
#         filtered_data = [
#             ['Body'],
#             ['Date', 'Weight', 'BMI', 'Fat']
#         ]
        
#         # Process each row
#         for row in reader:
#             # Skip empty rows or rows with value 162 in column 3
#             if not row or row[3] == '162':
#                 continue
                
#             # Only process rows that have data in the first column
#             if row[0]:
#                 date = row[0][:10]  # Extract just the date part
                
#                 # Process weight if available
#                 if row[1]:
#                     try:
#                         # Convert kg to lbs and round to 1 decimal place
#                         weight_lbs = float(row[1]) * 2.205
#                         weight_formatted = f"{weight_lbs:.1f}"
                        
#                         # Add processed row to filtered data
#                         filtered_data.append([date, float(weight_formatted), 0, 0])
#                     except ValueError:
#                         # Skip row if weight conversion fails
#                         continue
        
#         # Write processed data to output file
#         with open(output_file, mode="w", newline="", encoding="utf8") as output:
#             writer = csv.writer(output)
#             writer.writerows(filtered_data)

# if __name__ == "__main__":
#     file_path = os.path.join('amazfit-body-history.csv')
#     process_weight_data(file_path)


# v2
# import csv

# def convert_weight_amazfit_garmin(input_file, output_file='export.csv'):
#     """
#     Convert weight data from Amazfit format to Garmin format.
    
#     Args:
#         input_file (str): Path to the Amazfit CSV file
#         output_file (str): Path for the output Garmin-compatible CSV file
#     """
#     print(f"Converting data from {input_file} to {output_file}")
    
#     # Prepare output data structure with headers
#     garmin_data = [
#         ['Body'],
#         ['Date', 'Weight', 'BMI', 'Fat']
#     ]
    
#     # Process input file
#     with open(input_file, 'r', encoding='utf8') as csv_file:
#         reader = csv.reader(csv_file)
#         # Skip header rows
#         next(reader, None)
#         next(reader, None)
        
#         # Process data rows
#         processed_count = 0
#         skipped_count = 0
        
#         for row in reader:
#             # Skip records with specific value in third column
#             try:
#                 if abs(float(row[2]) - 162.0) < 0.01:  # Compare with small tolerance
#                     skipped_count += 1
#                     continue
#             except (ValueError, IndexError):
#                 # Handle possible conversion errors or missing data
#                 print(f"Warning: Could not process value in row: {row}")
#                 continue
                
#             # Extract and format date
#             date = row[0][:10]
            
#             # Convert weight from kg to lbs
#             try:
#                 weight_kg = float(row[1])
#                 weight_lbs = weight_kg * 2.205
#                 formatted_weight = f"{weight_lbs:.1f}"
                
#                 # Add processed row
#                 garmin_data.append([date, formatted_weight, 0, 0])
#                 processed_count += 1
                
#             except (ValueError, IndexError):
#                 print(f"Warning: Could not process weight in row: {row}")
    
#     # Write output file
#     with open(output_file, 'w', newline="", encoding='utf8') as output:
#         writer = csv.writer(output)
#         writer.writerows(garmin_data)
    
#     print(f"Conversion complete: {processed_count} records processed, {skipped_count} records skipped")
#     return processed_count

# if __name__ == "__main__":
#     convert_weight_amazfit_garmin('amazfit-body-history.csv')