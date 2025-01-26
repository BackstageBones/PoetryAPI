# PoetryDB API Client and Tests

This repository contains a Python client for interacting with the PoetryDB API and a suite of tests to ensure its functionality. The client uses a Singleton design pattern to manage a single instance of the API client.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Step-by-Step Guide](#step-by-step-guide)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/poetrydb-api-client.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd poetrydb-api-client
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The `PoetryDBAPI` class provides methods to fetch random poems and poems by a specific author.

Example:
```python
from poetry_api import PoetryDBAPI

client = PoetryDBAPI()
random_poem = client.get_random_poem()
print(random_poem)

author_poems = client.get_poem_by_author("Emily Dickinson")
print(author_poems)
```

## Running tests
```bash
     pytest .\test_poetry.py
   ```

| Test Case               | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| `test_get_random_poem`  | Fetches a random poem and checks that the response contains the keys `title`, `author`, and `lines`. |
| `test_get_poem_by_author` | Fetches poems by a specific author (e.g., Emily Dickinson) and verifies the structure and content of the response. |
