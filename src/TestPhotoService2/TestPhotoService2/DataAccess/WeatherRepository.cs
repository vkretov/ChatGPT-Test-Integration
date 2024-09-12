namespace TestPhotoService2.DataAccess;

public class WeatherRepository
{
    //for now, maintain the data in memory
    public Dictionary<string, WeatherDto> WeatherData = new();
    
    public WeatherDto GetWeatherForecastByCity(string city)
    {
        if (WeatherData.ContainsKey(city))
        {
            return WeatherData[city];
        }
        else
        {
            return null;
        }
    }
    
    public void AddWeatherForecast(WeatherDto weatherDto)
    {
        WeatherData.Add(weatherDto.City, weatherDto);
    }
}