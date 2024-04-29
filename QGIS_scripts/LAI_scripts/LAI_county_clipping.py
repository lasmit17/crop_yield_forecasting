import processing
from qgis.core import QgsProject, QgsRasterLayer
import os

# Path to your MODIS files
modis_files = ['D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2000.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2001.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2002.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2003.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2004.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2005.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2006.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2007.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2008.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2009.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2010.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2011.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2012.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2013.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2014.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2015.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2016.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2017.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2018.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2019.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2020.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2021.tiff',
'D:/thesis_data/lai_2000_2022/LAI_adjusted_Sclipped/LAI_adjusted_Sclippedclipped_lai_2022.tiff',
]

# Output directory for the clipped files
output_dir = 'D:/thesis_data/lai_2000_2022/LAI_county_clipped/'

for modis_file in modis_files:
    modis_layer = QgsRasterLayer(modis_file, 'MODIS LAI')
    if not modis_layer.isValid():
        print(f"Failed to load MODIS layer from {modis_file}")
        continue

    # Extract the unique identifier (year) from the MODIS file name
    basename = os.path.basename(modis_file)
    unique_identifier = basename.split('_')[4]  

    # Iterate through each county layer in the project
    for layer in QgsProject.instance().mapLayers().values():
        if layer.name().startswith("County_"):
            county_name = layer.name().split("_")[1]
            output_path = f'{output_dir}{county_name}_LAI_{unique_identifier}.tif'
            
            # Clip the MODIS layer to the county boundary
            processing.run("gdal:cliprasterbymasklayer", {
                'INPUT': modis_layer,
                'MASK': layer,  # Using the county layer directly as the mask
                'TARGET_CRS': modis_layer.crs(),
                'OUTPUT': output_path
            })
            
            print(f"Clipped {modis_layer.name()} to {county_name}, saved at {output_path}")
