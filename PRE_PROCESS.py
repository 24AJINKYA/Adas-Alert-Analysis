# PREPROCESSING
import pandas as pd

# Load the Excel file
file_path = "data.csv" # Replace with your file path
data = pd.read_csv(file_path)

# Display the first few rows to verify the data
print(data.head())

            
                     Alert        Date      Time        Lat       Long  Vehicle  Speed  Unnamed: 7  Unnamed: 8  Unnamed: 9
            0  cas_fcw  01-06-2022  06:26:32  12.724588  79.982251      805     33         NaN         NaN         NaN
            1  cas_fcw  01-06-2022  06:41:35  12.630791  79.931575      805     58         NaN         NaN         NaN
            2  cas_fcw  01-06-2022  17:01:28  12.747127  79.995694      805     58         NaN         NaN         NaN
            3  cas_fcw  01-06-2022  17:46:32  12.528537  79.898806      805     59         NaN         NaN         NaN
            4  cas_hmw  01-06-2022  06:14:53  12.815835  80.033858      805     45         NaN         NaN         NaN




### CHECKING FOR NULL VALUES 

missing_values = data.isnull().sum()
print(missing_values)


                                    Alert            0
                                    Date             0
                                    Time             0
                                    Lat              0
                                    Long             0
                                    Vehicle          0
                                    Speed            0


                        
