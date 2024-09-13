namespace TestPhotoService2.Services;

using DataAccess;

public class WeatherForecastGenerator
{
    public WeatherDto GenerateWeatherForecast(string city)
    {
        var random = new Random();
        var temperatureC = random.Next(-20, 55);
        return new WeatherDto
        {
            City = city,
            TemperatureC = temperatureC
        };
    }
}