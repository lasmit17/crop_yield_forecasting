from osgeo import gdal
import os, csv

# Directory containing LAI cropped files
lai_files_dir = 'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_county_clipped'



# CSV file to store the results
output_csv = 'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_data_for_analysis/ndvi_2000_2022.csv'

# Prepare to write to the CSV
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['County', 'Year', 'NDVI_Avg_Value'])  

    # Iterate through each LAI file in the directory
    for filename in os.listdir(lai_files_dir):
        if filename.endswith('.tiff.tif'):
            # Extract county and year from the filename
            parts = filename.split('_')
            county = parts[1]
            year = parts[3]

            # Open the raster file
            filepath = os.path.join(lai_files_dir, filename)
            ds = gdal.Open(filepath)
            band = ds.GetRasterBand(1) 

            # Calculate the average value
            stats = band.GetStatistics(True, True)  
            avg_lai = stats[2]

            # Write the results to the CSV
            writer.writerow([county, year, avg_lai])

print("Process completed and output saved to:", output_csv)
