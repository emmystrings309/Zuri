# Django Endpoint Project

This project creates and hosts a Django endpoint that accepts GET requests with query parameters and returns specific information in JSON format.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Development Server](#running-the-development-server)
- [Usage](#usage)
  - [Testing the Endpoint](#testing-the-endpoint)
- [API Endpoint](#api-endpoint)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of this project is to create a publicly accessible endpoint using Django that takes two GET request query parameters: `slack_name` and `track`. It then returns specific information in JSON format, including the Slack name, current day of the week, current UTC time (within a +/-2 minute window), track information, GitHub file URL, GitHub repository URL, and a status code of 200.

## Requirements

- Python (3.6+)
- Django
- pytz (for handling time zones)

## Getting Started

To run this project locally, follow these steps:

### Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

## Usage

You can test the project's endpoint locally or on a public server.

### Testing the Endpoint

To test the endpoint locally, you can use a tool like `curl` or Postman. Here's an example `curl` request:

```bash
curl -X GET "http://localhost:8000/api/?slack_name=example_name&track=backend"
```

This will send a GET request to the locally hosted endpoint with the `slack_name` and `track` parameters.

## API Endpoint

The API endpoint is accessible at `/api/` and accepts the following query parameters:

- `slack_name`: The Slack name provided as a GET request query parameter.
- `track`: The track information provided as a GET request query parameter.

The response will be in JSON format and includes the following information:

- `slack_name`: The provided Slack name.
- `current_day`: The current day of the week.
- `utc_time`: The current UTC time (within a +/-2 minute window).
- `track`: The track information.
- `github_file_url`: The GitHub URL of the file being run.
- `github_repo_url`: The GitHub URL of the full source code.
- `status_code`: 200 (indicating success).

## Configuration

There is no specific configuration required for this project beyond the standard Django settings.

## Contributing

Contributions to this project are welcome. If you find issues or have suggestions for improvements, please open an issue or create a pull request following our contribution guidelines.

## License

This project is licensed under the [MIT License](LICENSE).
