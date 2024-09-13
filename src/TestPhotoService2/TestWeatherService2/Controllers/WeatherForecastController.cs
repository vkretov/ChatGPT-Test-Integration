using Microsoft.AspNetCore.Mvc;

namespace TestPhotoService2.Controllers;

using DataAccess;
using Services;

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
    private readonly WeatherForecastGenerator _weatherForecastGenerator;

    public WeatherForecastController(ILogger<WeatherForecastController> logger, 
        WeatherRepository weatherRepository,
        WeatherForecastGenerator weatherForecastGenerator)
    {
        _logger = logger;
        _weatherRepository = weatherRepository;
        _weatherForecastGenerator = weatherForecastGenerator;
    }

    [HttpGet]
    public WeatherForecast GetByCity(string city)
    {
        var weatherDto = _weatherRepository.GetWeatherForecastByCity(city);
        if (weatherDto == null)
        {
            //generate a new weather forecast
            var newWeatherDto = _weatherForecastGenerator.GenerateWeatherForecast(city);
            _weatherRepository.AddWeatherForecast(newWeatherDto);
            return new WeatherForecast
            {
                City = newWeatherDto.City,
                Date = DateOnly.FromDateTime(DateTime.Now),
                TemperatureC = newWeatherDto.TemperatureC,
                Summary = Summaries[0]
            };
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