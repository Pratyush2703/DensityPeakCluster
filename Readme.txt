Original Codebase from : https://github.com/jasonwbw/DensityPeakCluster

Changes:
    1. Moved dependancies from V2.3 to V2.7
    2. Fixed divide by 0 bug in cluster.py
    3. Language syntax changes no longer reliably uses (arr = None). This wasmodified to the "is" keyword standard
    4. Implemented the distance builder python file with the enhancements from section 3.1
    5. The new distance file is stored at ./distance/Distance_builder_enhanced.py
    6. Added comments to map Steps 1-5 to Distance_builder_enhanced.py

Step 1: Run original algorithm. 
    Run ./Distance/Distance_builder_data_filename.py to create distance data file (eg. ./Distance/Distance_builder_data_aggregation.py)
    Run Step2_cluster.py to generate the results

Step 2: Create Advanced file. 
    Select the current input variables in "User variables" section
    Run ./Distance/Distance_builder_enhanced.py to create distance data file.
    Run Step2_cluster.py to generate the results
    Ensure the correct distancefile is selected in the main function