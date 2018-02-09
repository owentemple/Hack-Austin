import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
import settings
import pandas as pd
import numpy as np

def concatenate():
    # Create Super Dataset
    # From files downloaded from https://github.com/cityofaustin/hack-austin/tree/master/Austin%20Fire%20Department%20Data

    # 2012
    fire_2012 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY12 - SOC Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2012.dropna(inplace=True)
    fire_2012.index = pd.to_datetime(fire_2012.index)

    # 2013
    fire_2013 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY13 - SOC Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2013.dropna(inplace=True)
    fire_2013.index = pd.to_datetime(fire_2013.index)

    # 2014
    fire_2014 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY14 - SOC Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2014.dropna(inplace=True)
    fire_2014.index = pd.to_datetime(fire_2014.index)

    # 2015
    fire_2015 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY15 - SOC Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2015.dropna(inplace=True)
    fire_2015.index = pd.to_datetime(fire_2015.index)

    # 2016
    fire_2016 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY16 - SOC Fire Data Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2016.dropna(inplace=True)
    fire_2016.index = pd.to_datetime(fire_2016.index)

    # 2017
    fire_2017 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_CY17 - SOC Filtered Data_Generalized.csv'), index_col='AFD Time Phone Pickup')
    fire_2017.dropna(inplace=True)
    fire_2017.index = pd.to_datetime(fire_2017.index)

    # Combine all years into single dataframe
    final_df = pd.concat([fire_2012, fire_2013, fire_2014, fire_2015, fire_2016, fire_2017])

    # Calculate time between AFD phone pickup and first unit arrival in seconds and in minutes
    final_df['First Unit Arrived'] = pd.to_datetime(final_df['First Unit Arrived'])
    final_df['Response Time (s)'] = (final_df['First Unit Arrived'] - final_df.index).astype('timedelta64[s]')
    final_df['Response Time (m)'] = ((final_df['First Unit Arrived'] - final_df.index).astype('timedelta64[s]')) / 60
    final_df.reset_index(inplace=True)

    # Read in incident detail reports for all years available
    # Downloaded from https://data.austintexas.gov/browse?q=AFD&sortBy=relevance&anonymous=true
    AFD_13 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_Fire_Incidents_2013_January_Thru_December.csv'))
    AFD_14 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_Fire_Incidents_2014_January_Thru_December.csv'))
    AFD_15 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_Fire_Incidents_2015_January_Thru_December.csv'))
    AFD_16 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_Fire_Incidents_2016_January_Thru_December.csv'))
    AFD_17 = pd.read_csv(os.path.join('..', settings.DATA_DIR, 'AFD_Fire_Incidents_2017_January_Thru_December.csv'))

    # Concatenate all years incident detail reports into one dataframe
    frames = [AFD_13, AFD_14, AFD_15, AFD_16, AFD_17]
    result = pd.concat(frames)
    result = result.rename(index=str, columns={"MasterIncidentNumber": "Master Incident Number"})

    # Join dataframe with response time information with problem detail dataframe
    detail_final_df = pd.merge(final_df, result, how='inner', on='Master Incident Number')
    detail_final_df['day_of_week'] = detail_final_df['First Unit Arrived'].dt.dayofweek
    detail_final_df['hour'] = detail_final_df['First Unit Arrived'].dt.hour
    detail_final_df['late_response'] = np.where(detail_final_df['Response Time (s)'] > (60 * 8), 1, 0)

    del detail_final_df['CalendarYear_y']
    del detail_final_df['PriorityDescription_y']
    del detail_final_df['Response Status_y']
    detail_final_df.rename(columns={'CalendarYear_x': 'CalendarYear', 'Response Status_x': 'Response Status',
                                    'PriorityDescription_x': 'PriorityDescription'}, inplace=True)

    detail_final_df.to_csv(os.path.join('..', settings.PROCESSED_DIR, 'All Years with Response Times and Problem Types.csv'))
    df = detail_final_df
    return df

def create_dummies(df):
    df = pd.get_dummies(df, columns=['Problem', 'ResponseArea', 'day_of_week', 'hour'])
    return df

def write_data():
    df.to_csv(os.path.join('..', settings.PROCESSED_DIR, "all_years_with_RT-and-PT-dummies.csv"), index_label='index')
    pass


if __name__ == "__main__":
    df = concatenate()
    df = create_dummies(df)
    write_data()