#%%
import pandas as pd
import numpy as np
from preprocess_func import *
# %%
# read files
df = pd.read_csv('treas_parking_payments_2023_datasd.csv')
parking_meter_location_raw = pd.read_csv('treas_parking_meters_loc_datasd.csv')
### preprocess location data set, drop unused columns and rows.
parking_meter_location_raw.rename(columns={'pole': 'pole_id'}, inplace=True)
parking_meter_location_raw=parking_meter_location_raw.drop(columns=['config_id','config_name','date_inventory','sapid'])
parking_meter_location=parking_meter_location_raw.drop_duplicates(subset=['pole_id'])
#%%
### Merge the rows that same person keep adding money.
merged_df = merge_time_overlapping_row(df)
merged_df
#%%
# add day name to seprate weekday and weekend
merged_df['day_of_week']=merged_df['date_trans_start'].dt.day_name()
merged_df['is_weekday']= ~((merged_df['day_of_week']=='Saturday') | (merged_df['day_of_week']== 'Sunday'))
#%%
print(merged_df)


#%%
#########################################################
### sum total parking time and transaction for each pole.
#########################################################
parking_payment_2023=get_total_hours(merged_df)
### merge two dataset based on pole_id and drop unmatch rows. (Some poles have no transaction through the year.)
merged_ori = pd.merge(parking_meter_location, parking_payment_2023, on='pole_id', how='inner')
print(merged_ori)
#%%
### Get 
merged = merged_ori.groupby(['area','is_weekday'], as_index=False).agg({
    'time_period_min': 'sum',
    'pole_id': 'count',
    'ave_time_period_min':'sum',
    'trans_amt': 'sum'
})   
merged.sort_values(by='time_period_min', ascending=False)

# %%
merged['time_period_min_per_pole']=merged.eval("time_period_min/pole_id")
merged['ave_time_period_min_per_pole']=merged.eval("ave_time_period_min/pole_id")

# %%
output_csv_weekday=merged.loc[merged['is_weekday'] == True].sort_values(by='time_period_min_per_pole', ascending=False)
output_csv_weekend=merged.loc[merged['is_weekday'] == False].sort_values(by='time_period_min_per_pole', ascending=False)
output_csv_weekday.to_csv('parking_time_by_area_weekday.csv', index=False)
output_csv_weekend.to_csv('parking_time_by_area_weekend.csv', index=False)



# %%
############################################################
# Get occupied time by hours
############################################################
# Create a list of two-hour intervals
start_time = pd.Timestamp("08:00:00")
end_time = pd.Timestamp("18:00:00")
interval = pd.Timedelta(hours=1)
time_slots = pd.date_range(start=start_time, end=end_time, freq=interval)
hour_slots = [f'{start.strftime("%H:%M")}-{(start + interval).strftime("%H:%M")}' for start in time_slots]
# Get parking time by hours, take few minutes.
df_parking_time_by_hours_ori=get_occupied_time_by_time_range(merged_df,start_time,end_time)
# %%
df_parking_time_by_hours_ori = pd.read_csv('parking_time_by_hours_ori.csv')
tmp_df1=pd.merge(parking_meter_location, df_parking_time_by_hours_ori, on='pole_id', how='inner')
tmp_df1
# %%
tmp_df1=tmp_df1.drop(columns=['zone','sub_area','lat','lng','date_trans_start','date_meter_expire','trans_amt'])

#%%
area_parking_time_by_hours = tmp_df1.groupby(['area','pole_id']).sum()
#%%
area_parking_time_by_hours['pole_id']=1
area_parking_time_by_hours = area_parking_time_by_hours.groupby(['area']).sum()
# %%
#df_parking_time_by_hours_ori.to_csv('parking_time_by_hours_ori.csv', index=False)
# %%
area_parking_time_by_hours
area_parking_time_by_hours.reset_index().to_csv('parking_time_by_hours_per_area.csv', index=False)
