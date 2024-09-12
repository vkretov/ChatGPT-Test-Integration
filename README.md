# ChatGPT-Test-Integration
ChatGPT-Test-Integration

This repo contins a test api.
it also has github actions for chatgpt to do a code review and to generate changelogs automatically.

api doc: tbd

```markdown
# Project Update

### Implement Basic Endpoints; Simulate a Database

This update introduces basic API endpoints to simulate a weather data repository. The following changes have been made to the project:

### Changes

#### WeatherForecastController.cs

- Introduced a dependency on `WeatherRepository` to retrieve and manage weather data.
- Updated the `Get` method to `GetByCity`, allowing retrieval of weather forecasts based on the city name.
- Added error handling for cases when a forecast for a specified city does not exist.
- Implemented an `AddWeatherForecast` endpoint to allow adding new weather forecasts to the in-memory database.

#### WeatherDto.cs

- Created a new class `WeatherDto` to represent weather data, including properties for `City` and `TemperatureC`.

#### WeatherRepository.cs

- Implemented a simple in-memory repository to manage weather data.
- Added methods to get a weather forecast by city and to add new weather forecasts.

#### Program.cs

- Registered `WeatherRepository` as a singleton service in the application.

### Summary of Endpoints
- **GET** `/WeatherForecast?city={city}` - Retrieves the weather forecast for a specified city.
- **POST** `/WeatherForecast` - Adds a new weather forecast.

This update enhances the API's capabilities, allowing it to simulate a basic weather data storage and retrieval system.
```