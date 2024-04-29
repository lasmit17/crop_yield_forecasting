from osgeo import gdal
import os, csv

# Directory containing LAI cropped files
lai_files_dir = 'D:/thesis_data/lai_2000_2022/LAI_county_clipped'

# CSV file to store the results
output_csv = 'D:/thesis_data/lai_2000_2022/lai_data_for_analysis/lai_2000_2022.csv'


# Prepare to write to the CSV
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['County', 'Year', 'LAI_Avg_Value']) 

    # Iterate through each LAI file in the directory
    for filename in os.listdir(lai_files_dir):
        if filename.endswith('.tiff.tif'):
            # Extract county and year from the filename
            parts = filename.split('_')
            county = parts[0]
            year = parts[2]

            # Open the raster file
            filepath = os.path.join(lai_files_dir, filename)
            ds = gdal.Open(filepath)
            band = ds.GetRasterBand(1)

            # Calculate the average value
            stats = band.GetStatistics(True, True)  # This grabs the min, max, mean, and std dev
            avg_lai = stats[2]  

            # Put the results in the CSV
            writer.writerow([county, year, avg_lai])

print("Process completed and output saved to:", output_csv)
