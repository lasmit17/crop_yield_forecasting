from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer
import processing

# Path to your North Carolina state boundary layer 
nc_state_boundary_path = 'D:/thesis_data/nc_state_boundary_counties/North_Carolina_State_and_County_Boundary_Polygons.shp'

# Load the NC state boundary layer
nc_state_boundary_layer = QgsVectorLayer(nc_state_boundary_path, 'NC State Boundary', 'ogr')

# Ensure the layer is correctly loaded
if not nc_state_boundary_layer.isValid():
    print("State boundary layer failed to load!")
else:
    QgsProject.instance().addMapLayer(nc_state_boundary_layer)

# List of MODIS LAI file paths
modis_files = ['D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2000.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2001.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2002.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2003.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2004.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2005.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2006.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2007.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2008.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2009.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2010.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2011.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2012.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2013.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2014.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2015.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2016.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2017.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2018.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2019.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2020.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2021.tiff',
'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted/ndvi_adjusted_2022.tiff',
]


# Output directory for clipped files
output_dir = 'D:/thesis_data/ndvi_evi_2000_2022/NDVI/NDVI_adjusted_Sclipped/'

# Iterate over each MODIS file
for modis_file in modis_files:
    modis_layer = QgsRasterLayer(modis_file, 'MODIS LAI')
    
    # Make sure the MODIS layer is valid
    if not modis_layer.isValid():
        print(f"MODIS layer {modis_file} failed to load!")
        continue
    
    # Define the output file path
    output_path = output_dir + 'clipped_' + os.path.basename(modis_file)
    
    # Clip the MODIS layer to the NC state boundary
    processing.run("gdal:cliprasterbymasklayer", 
                   {'INPUT': modis_layer,
                    'MASK': nc_state_boundary_layer,
                    'NODATA': -9999,  
                    'TARGET_CRS': modis_layer.crs(),  
                    'OUTPUT': output_path})
    
    print(f"Clipped MODIS layer saved to: {output_path}")

