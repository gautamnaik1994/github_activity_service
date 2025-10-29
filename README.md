# GitHub Activity Service

This project implements a service that fetches and summarizes a GitHub user's recent activity across public repositories using GitHub's public API. It identifies the most common event types for each repository the user has contributed to and flags repositories owned by the user.

## Features

- Fetches public events for a specified GitHub user.
- Summarizes the three most common event types per repository.
- Flags repositories owned by the user.
- Caches API responses to handle network issues gracefully.

## Project Structure

The project is structured as follows:

- `main.py`: The entry point of the application that handles command-line arguments and initiates the activity summary process.
- `services/github_client.py`: Contains the `GitHubClient` class responsible for interacting with the GitHub API and caching responses.
- `services/activity_summarizer.py`: Contains `ActivitySummarizer` class that processes the fetched events and generates the summary.
- `models/`: Directory containing data models used in the application.

## Technologies Used

- Python 3.12
- Requests
- GitHub API
- Docker

## Setup

1. Clone the repository:

```bash
git clone https://github.com/gautamnaik1994/github_activity_service.git
cd github_activity_service
git checkout feature/jira-123
```

2. Create and activate a virtual environment optionally:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the program, use the following command,

```bash
python main.py <github_username>
```

## Docker Usage

To run the program using Docker, follow these steps:

1. Build the Docker image:

```bash
docker build -t github_activity_service .
```

2. Run the Docker container with the GitHub username as an argument:

```bash
docker run -p 8000:8000 github_activity_service ge0ffrey
```

## Scope for Improvement

1. Implementing unit tests and integration tests.
2. Implement Pydantic models for better data validation and serialization.
3. Adding detailed error handling, logging, and monitoring.
4. Implementing advanced caching strategies with expiration policies.
5. Config based approach to set parameters like number of events to fetch, cache location, etc.
