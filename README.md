# Crop_Yield_Forecasting
Hertie 2024 Master of Data Science for Public Policy - Thesis

## Description

analysis_script:
This folder contains all scripts used for the primary data analysis of the thesis. Inside, you will find the Python script responsible for creating, tuning, and evaluating various machine learning models such as Random Forest, XGBoost, and Deep Neural Networks. Additionally, this folder includes scripts for generating visualizations that illustrate the results of the models, compare their performance, and display the feature importance used in the models. These scripts are essential for understanding the predictive capabilities of the models and for interpreting how different variables influence soybean yield predictions.

QGIS_scripts:
This folder houses Python scripts designed as plugins for QGIS, specifically used for processing MODIS satellite images. The scripts automate tasks such as clipping the MODIS images to the North Carolina state and county boundaries, and calculating average values of environmental indices like NDVI, EVI, and LAI for each county. These processed data are crucial for the analysis as they provide the satellite-derived variables used in the machine learning models to predict soybean yields. These plugins represent a significant part of the data preprocessing and integration efforts detailed in the thesis.

data:
This folder contains the final data used within the analysis_script. It consists of MODIS variables, weather data, and the soybean yield data utilized in all of the machine learning models.


## License
This project includes software developed at QGIS, which is licensed under the GNU General Public License (GPL), version 2. The use of the QGIS software is in compliance with its license, and any derivative scripts retain this license.

All analysis and visualization scripts created for Google Colab are available under the MIT License to promote the free use, modification, and distribution of this academic work.
