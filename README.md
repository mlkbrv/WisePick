# WisePick

A Django-based API for CPU comparison and analysis using AI-powered insights.

## Description

WisePick is a REST API that allows users to compare CPU processors and get AI-generated analysis and visualizations. The system uses machine learning to provide detailed comparisons between different processors based on their specifications.

## Features

- **CPU Management**: CRUD operations for CPU data
- **AI-Powered Comparison**: Intelligent comparison between two processors
- **JSON Data Generation**: Structured data for visualization
- **Performance Scoring**: Automated performance calculation based on CPU specifications
- **REST API**: Full RESTful API endpoints

## Technology Stack

- **Backend**: Django 5.2.4
- **API**: Django REST Framework
- **AI Integration**: OpenRouter API (DeepSeek model)
- **Database**: SQLite (development)
- **Environment**: Python 3.x

## Installation

### Prerequisites

- Python 3.8+
- pip
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd WisePick
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### CPU Management

- `GET /core/cpu/` - List all CPUs
- `POST /core/cpu/` - Create a new CPU
- `GET /core/cpu/{id}` - Get specific CPU details
- `PUT /core/cpu/{id}` - Update CPU
- `DELETE /core/cpu/{id}` - Delete CPU

### CPU Comparison

- `GET /core/compare/{cpu1_name}/{cpu2_name}` - Compare two CPUs

## CPU Model Fields

- `name` - Processor name
- `clock_speed_ghz` - Clock speed in GHz
- `core_count` - Number of cores
- `thread_count` - Number of threads
- `cache_size_l1` - L1 cache size
- `cache_size_l2` - L2 cache size
- `cache_size_l3` - L3 cache size
- `tdp_watts` - Thermal Design Power in watts
- `architecture_generation` - Architecture generation
- `ipc` - Instructions per clock

## Usage Examples

### Adding a CPU
```bash
curl -X POST http://localhost:8000/core/cpu/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Intel Core i7-12700K",
    "clock_speed_ghz": 3.6,
    "core_count": 12,
    "thread_count": 20,
    "cache_size_l1": 480,
    "cache_size_l2": 12288,
    "cache_size_l3": 25600,
    "tdp_watts": 125,
    "architecture_generation": "Alder Lake",
    "ipc": 1.2
  }'
```

### Comparing CPUs
```bash
curl http://localhost:8000/core/compare/Intel%20Core%20i7-12700K/AMD%20Ryzen%207%205800X
```

## AI Integration

The project uses OpenRouter API with the DeepSeek model to generate intelligent comparisons and performance analysis. The AI provides:

- Performance scoring based on specifications
- Structured JSON data for visualization
- Comparative analysis between processors

## Project Structure

```
WisePick/
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── ai.py          # AI integration logic
│   ├── apps.py
│   ├── migrations/
│   ├── models.py      # CPU model
│   ├── serializers.py # API serializers
│   ├── tests.py
│   ├── urls.py        # URL routing
│   └── views.py       # API views
├── WisePick/
│   ├── __init__.py
│   ├── settings.py    # Django settings
│   ├── urls.py        # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
└── README.md
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
The project follows PEP 8 guidelines for Python code style.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the repository.

## Acknowledgments

- Django REST Framework for the API framework
- OpenRouter for AI integration
- DeepSeek for the AI model 