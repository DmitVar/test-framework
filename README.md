
```
test-framework/
├── .env                          # Environment variables
├── .flake8                       # Flake8 linter configuration
├── .gitignore                    # Git ignore rules
├── .pre-commit-config.yaml       # Pre-commit hooks configuration
├── config.py                     # Project configuration settings
├── conftest.py                   # Pytest configuration and global fixtures
├── pyproject.toml                # Project metadata and tool configuration
├── pytest.ini                    # Pytest settings and markers
├── README.md                     # Project documentation
│
├── core/                         # Core business logic and domain layer
│   ├── api/                      # API client and services
│   │   ├── clients/              # API clients (REST, GraphQL, etc.)
│   └── web_ui/                   # Web UI components and page objects
│       ├── components/           # Reusable UI components
│       ├── elements/             # Base UI elements
│       ├── pages/                # Page Object Model classes
│       └── __init__.py
│
├── fixtures/                     # Pytest fixtures for test setup/teardown
│   ├── api/                      # API-related fixtures
│   ├── web_ui/                   # Web UI fixtures
│   ├── allure.py                 # Allure reporting fixtures
│   └── __init__.py
│
├── tests/                        # Test suites
│   ├── api/                      # API tests
│   ├── web_ui/                   # Web UI tests
│   └── __init__.py
├── tools/                        # Test utilities and helpers
│   ├── allure/                   # Allure reporting tests
│   ├── assertion/                # Custom assertion helpers
│   ├── http/                     # HTTP client wrappers
│   ├── playwright/               # Playwright integration
│   ├── logger.py                 # Playwright logging utilities
│   └── __init__.py
│
├── allure-results/               # Allure test reports output
├── coverage-results/             # Test coverage reports
├── tracing/                      # Trace logs and debugging artifacts
├── video/                        # Video recordings of test executions
│
└── venv/                         # Python virtual environment
```

```bash
# Clone the repository
git clone https://github.com/DmitVar/test-framework.git

# Navigate to the directory
cd test-framework

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```
```bash
# Run tests
# All tests
pytest

# Only UI tests
pytest -m "ui"
# Only API tests
pytest -m "api"
# Smoke tests
pytest -m "smoke"
```