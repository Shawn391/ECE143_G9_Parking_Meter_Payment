import pandas as pd
import numpy as np
#%%
def merge_time_overlapping_row(df,time_diff_by_sec=120):
    # Convert 'date_trans_start' and 'date_meter_expire' to datetime
    df['date_trans_start'] = pd.to_datetime(df['date_trans_start'])
    df['date_meter_expire'] = pd.to_datetime(df['date_meter_expire'])

    # Sort by 'date_trans_start' for sequential processing
    #df = df.sort_values('date_trans_start')
    df = df.sort_values(by=['pole_id', 'date_trans_start'], ascending=[True, True])

    # Initialize a new column 'group' to identify rows that can be grouped together
    df['group'] = (df['date_trans_start'] - df['date_trans_start'].shift()).dt.total_seconds() > time_diff_by_sec
    '''
    Converting Flags to Group Identifiers: By using cumsum() on this boolean series, 
    you convert these flags into a series of identifiers. 
    Since True is treated as 1 and False as 0, each True increments the cumulative sum by 1,
    effectively starting a new group.
                  group  group_before cumsum
    0             0      False
    1             1      True
    2             2      True
    3             2      False    ##### within 'time_diff_by_sec' compared with previous one
    4             3      True

    Note line 2 and 3 are put in the same group using flag, which are two timestap within certain period.
    '''
    df['group'] = df['group'].cumsum()
    # Group by 'ID' and the new 'group' column, and then aggregate
    grouped_df = df.groupby(['pole_id', 'group'], as_index=False).agg({
        'date_trans_start': 'min',
        'date_meter_expire': 'max',
        'trans_amt': 'sum'
    })  
    grouped_df=grouped_df.drop(columns=['group'])
    return grouped_df 

def get_total_hours(df):
    df['date_trans_start'] = pd.to_datetime(df['date_trans_start'])
    df['date_meter_expire'] = pd.to_datetime(df['date_meter_expire'])
    df['time_period_min'] = df['date_meter_expire'] - df['date_trans_start']
    df['time_period_min']=round(df['time_period_min'].dt.total_seconds()/60)
    df['counter']=1
    #print(df.loc[df['pole_id'] == '1-1004'])

    df = df.groupby(['pole_id','is_weekday'], as_index=False).agg({
        'time_period_min': 'sum',
        'trans_amt': 'sum',
        'counter': 'sum'
    })    

    df['ave_time_period_min']=df['time_period_min']/df['counter']
    df=df.drop(columns=['counter'])
    return df



# %%
def get_occupied_time_by_time_range(df,start_time,end_time,hour_interval=1):
    #start_time = pd.Timestamp("08:00:00")
    #end_time = pd.Timestamp("18:00:00")
    interval = pd.Timedelta(hours=hour_interval)
    time_slots = pd.date_range(start=start_time, end=end_time, freq=interval)
    # Create list of hour slots in the specified format
    hour_slots = [f'{start.strftime("%H:%M")}-{(start + interval).strftime("%H:%M")}' for start in time_slots]

    # Prepare output DataFrame with additional columns for hour slots
    output_df = df.copy()
    for slot in hour_slots:
        output_df[slot] = 0
    # Function to calculate minutes in each hour slot
    def calculate_minutes_in_slot(row, start_hour, end_hour):
        start_of_hour = row['date_trans_start'].replace(hour=0,minute=0, second=0, microsecond=0) + pd.Timedelta(hours=start_hour)
        #start_of_hour = pd.Timedelta(hours=start_hour)

        end_of_hour = start_of_hour + pd.Timedelta(hours=1)
        #end_of_hour=end_hour
        # If the parking period is entirely within the hour slot
        if row['date_trans_start'] >= end_of_hour:
            return_tmp = 0
        elif row['date_meter_expire'] <= start_of_hour:
            return_tmp = 0
        elif row['date_trans_start'] >= start_of_hour and row['date_meter_expire'] <= end_of_hour:
            return_tmp = (row['date_meter_expire'] - row['date_trans_start']).seconds / 60
        
        # If the parking starts before the hour slot and ends within the hour slot
        elif row['date_trans_start'] < start_of_hour and row['date_meter_expire'] <= end_of_hour:
            return_tmp = (row['date_meter_expire'] - start_of_hour).seconds / 60
        
        # If the parking starts within the hour slot and ends after the hour slot
        elif row['date_trans_start'] >= start_of_hour and row['date_meter_expire'] > end_of_hour:
            return_tmp = (end_of_hour - row['date_trans_start']).seconds / 60
        
        # If the parking covers the whole hour slot
        elif row['date_trans_start'] < start_of_hour and row['date_meter_expire'] > end_of_hour:
            return_tmp = 60
        
        # If the parking does not overlap with the hour slot at all
        else:
            return_tmp = 0
        return return_tmp
    # Iterate over each row and hour slot to calculate the minutes
    total_rows = len(output_df)
    for i, (index, row) in enumerate(output_df.iterrows(), 1):
        # Calculate rough percentage
        percentage_complete = (i / total_rows) * 100        
        # Print the percentage
        print(f"Processing row {i}/{total_rows} - {percentage_complete:.2f}% complete")
        for hour in range(int(start_time.strftime('%H')), int(end_time.strftime('%H'))):
            output_df.at[index, f'{str(hour).zfill(2)}:00-{str(hour+1).zfill(2)}:00'] = calculate_minutes_in_slot(row, hour, hour + 1)

    # Display the resulting DataFrame
    return output_df

# %%
