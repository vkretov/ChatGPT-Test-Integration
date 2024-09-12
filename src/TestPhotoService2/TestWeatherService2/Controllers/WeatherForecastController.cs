using Microsoft.AspNetCore.Mvc;

namespace TestPhotoService2.Controllers;

using DataAccess;

[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private static readonly string[] Summaries = new[]
    {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };
    

    private readonly ILogger<WeatherForecastController> _logger;
    private readonly WeatherRepository _weatherRepository;

    public WeatherForecastController(ILogger<WeatherForecastController> logger, WeatherRepository weatherRepository)
    {
        _logger = logger;
        _weatherRepository = weatherRepository;
    }

    [HttpGet]
    public WeatherForecast GetByCity(string city)
    {
        var weatherDto = _weatherRepository.GetWeatherForecastByCity(city);
        if (weatherDto == null)
        {
            return null;
        }
        else
        {
            return new WeatherForecast
            {
                City = weatherDto.City,
                Date = DateOnly.FromDateTime(DateTime.Now),
                TemperatureC = weatherDto.TemperatureC,
                Summary = Summaries[0]
            };
        }
    }
    
    [HttpPost]
    public void AddWeatherForecast(WeatherDto weatherDto)
    {
        _weatherRepository.AddWeatherForecast(weatherDto);
    }
    
    
}