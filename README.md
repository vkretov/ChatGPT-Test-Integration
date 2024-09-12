# ChatGPT-Test-Integration
ChatGPT-Test-Integration repository that hosts an http service as well as github actions for integrating ChatGPT in the codereview and code documentation process.

# TestWeatherService2

TestWeatherService2 is a .NET Core web API service designed to handle weather forecast data. This service provides endpoints to retrieve and add weather forecasts based on city names.

## Features

- **Get Weather Forecast**: Retrieve weather forecast information for a specific city.
- **Add Weather Forecast**: Add new weather forecast data to the repository.

## API Endpoints

### Get Weather Forecast

- **Endpoint**: `GET /weatherforecast`
- **Description**: Retrieves the current weather forecast for a specified city.
- **Query Parameters**:
    - `city` (string): The name of the city for which the weather forecast is requested.
- **Response**: Returns a `WeatherForecast` object containing the city, date, temperature in Celsius, and a summary of the weather.

**Example Request:**
GET /weatherforecast?city=Seattle

**Example Response:**
```json
{
  "city": "Seattle",
  "date": "2024-09-12",
  "temperatureC": 15,
  "summary": "Freezing"
}
```

### Add Weather Forecast
- **Endpoint**: POST /weatherforecast
- **Description**: Adds a new weather forecast entry to the repository.
- **Request Body**: A WeatherDto object containing the weather forecast data to be added.

**Request Body Schema**:
- **City (string)**: The name of the city.
- **TemperatureC (int)**: Temperature in Celsius.
- **Date (string)**: The date of the weather forecast in yyyy-MM-dd format.

**Example Request**:

```json
{
  "city": "string",
  "temperatureC": 0,
  "date": "string"
}
```

**Example Response:**

Status Code: 200 OK