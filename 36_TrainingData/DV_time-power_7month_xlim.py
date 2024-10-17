import pandas as pd
import matplotlib.pyplot as plt

for i in range(1, 18):
    # Load the dataset
    file_path = 'L' + str(i) + '_Train.csv'  # Ensure the file is in the correct directory
    df = pd.read_csv(file_path)

    # Convert DateTime to datetime format
    df['DateTime'] = pd.to_datetime(df['DateTime'])

    # Calculate the daily average of Power(mW)
    df['Date'] = df['DateTime'].dt.date  # Extract the date part
    df_daily_avg = df.groupby('Date')['Power(mW)'].mean().reset_index()

    # Set up the plot for all months (January to July)
    plt.figure(figsize=(12, 8))

    # Define month names for the title and labels
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July']

    # Loop over each month to plot its data
    for month in range(1, 8):  # Months 1 to 7
        # Filter data for the current month
        df_month = df_daily_avg[df_daily_avg['Date'].apply(lambda x: x.month) == month]
        
        # Plot the scatter points for the current month with a unique color
        plt.scatter(df_month['Date'], df_month['Power(mW)'], label=month_names[month-1])

    # Set labels and title
    plt.xlabel('Date')
    plt.ylabel('Average Power (mW)')
    plt.title(f'Average Solar Power Generation (January to July) L{i}')

    # Set the X-axis to show months from January to July, even if there's no data
    plt.xticks(pd.date_range('2024-01-01', '2024-07-01', freq='MS').date, 
               labels=['January', 'February', 'March', 'April', 'May', 'June', 'July'])
    
    # Set X and Y axis limits
    plt.xlim(pd.Timestamp('2024-01-01'), pd.Timestamp('2024-07-31'))  # Ensure the plot covers January to July
    # plt.ylim(0, df_daily_avg['Power(mW)'].max() * 1.1)  # Adjust Y axis limit based on the data
    plt.ylim(0, 1500)  # Set the Y-axis limit to a fixed range (0 to 1500)

    # Rotate the X-axis labels for readability
    plt.xticks(rotation=45, ha='right')

    # Adjust layout to prevent clipping and save the plot
    plt.tight_layout()
    plt.savefig(f'./fig/month scatter 1~17 lim/power_merged_scatter_L{i}.png')  # Saves to the specified directory
    plt.close()  # Close the plot to prevent it from displaying
