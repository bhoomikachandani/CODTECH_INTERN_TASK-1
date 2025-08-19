import requests
import matplotlib.pyplot as plt
import seaborn as sns

city_name = input("Enter your city name : ")
API_key = "e34d108c2e2527e9a220b344fd1bcaf4"
base_url = "http://api.openweathermap.org/data/2.5/forecast"
complete_url = f"{base_url}?q={city_name}&appid={API_key}"

response = requests.get(complete_url)

if response.status_code == 200:
    weather_data = response.json()
    forecast_list = weather_data['list']

    dates = []
    temperatures = []
    last_date_points = {}

    for item in forecast_list:
        temp_kelvin = item['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        date_text = item['dt_txt']
        date_only = date_text.split()[0]
        dates.append(date_text)
        temperatures.append(temp_celsius)
        last_date_points[date_only] = (date_text, temp_celsius)

    scatter_dates = [v[0] for v in last_date_points.values()]
    scatter_temps = [v[1] for v in last_date_points.values()]

    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    sns.lineplot(x=dates, y=temperatures, color='blue', marker=None)
    sns.scatterplot(x=scatter_dates, y=scatter_temps, color='red', s=100, zorder=5, label='End of Day')

    plt.title(f"Temperature Forecast for {city_name}", fontsize=16)
    plt.xlabel("Date and Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(dates[::4], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print(f"Error: Could not retrieve data for '{city_name}'.")
    print("Please check the city name and your API key.")