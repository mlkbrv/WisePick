# 🚀 WisePick - AI-Powered PC Component Comparison

> **Your AI-Powered Guide to Building the Perfect PC** 🎯

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Redis](https://img.shields.io/badge/Redis-Caching-red.svg)](https://redis.io)

---

## 🌟 What is WisePick?

WisePick is an intelligent web application that helps users build the perfect PC by providing smart recommendations for CPU, GPU, and RAM combinations. Our AI-powered system analyzes compatibility, performance, and value to suggest optimal component pairings for your specific needs.

### 🎯 Key Features

- 🤖 **AI-Powered Recommendations** - Get smart suggestions based on your requirements using OpenAI API
- 💻 **Comprehensive Database** - Latest CPUs, GPUs, and RAM from Intel, AMD, and NVIDIA
- ⚡ **Performance Analysis** - Detailed benchmarks and compatibility checks with weighted scoring
- 🎮 **Gaming Optimized** - Specialized recommendations for gaming builds
- 💰 **Budget-Friendly** - Find the best value for your money
- 📊 **Real-time Comparisons** - Compare different component combinations with detailed analysis
- 🆕 **PC Comparison by Need** - Compare full PC configurations based on user needs (gaming, work, video editing, etc.)
- 🚀 **RESTful API** - Complete API for third-party integrations
- 📈 **Caching** - Redis-powered caching for improved performance
- 🐳 **Docker Ready** - Easy deployment with Docker and Docker Compose

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|------------|---------|
| **Backend** | 🐍 Python | 3.12+ |
| **Framework** | 🎯 Django | 5.2+ |
| **Database** | 🗄️ SQLite | Default |
| **Cache** | 📈 Redis | 7+ |
| **API** | 🚀 Django REST Framework | 3.16+ |
| **AI Engine** | 🤖 OpenAI API (OpenRouter) | Latest |
| **Documentation** | 📚 DRF Spectacular | 0.28+ |
| **Deployment** | 🐳 Docker & Docker Compose | Latest |
| **CORS** | 🌐 django-cors-headers | 4.3+ |

---

## 🚀 Quick Start

### 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### 🔧 Installation

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

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   ```
   http://localhost:8000
   ```

---

## 📚 API Documentation

### 🔗 Base URL
```
http://localhost:8000/api/
```

### 📋 Available Endpoints

#### 🖥️ CPU Endpoints
- `GET /api/cpu/` - List all CPUs (with pagination and search)
- `POST /api/cpu/` - Create new CPU
- `GET /api/cpu/{id}/` - Get specific CPU details
- `PUT /api/cpu/{id}/` - Update CPU
- `DELETE /api/cpu/{id}/` - Delete CPU
- `GET /api/compare_cpu/{cpu1}/{cpu2}/` - Compare two CPUs

#### 🎮 GPU Endpoints
- `GET /api/gpu/` - List all GPUs (with pagination and search)
- `POST /api/gpu/` - Create new GPU
- `GET /api/gpu/{id}/` - Get specific GPU details
- `PUT /api/gpu/{id}/` - Update GPU
- `DELETE /api/gpu/{id}/` - Delete GPU
- `GET /api/compare_gpu/{gpu1}/{gpu2}/` - Compare two GPUs

#### 💾 RAM Endpoints
- `GET /api/ram/` - List all RAM modules (with pagination and search)
- `POST /api/ram/` - Create new RAM
- `GET /api/ram/{id}/` - Get specific RAM details
- `PUT /api/ram/{id}/` - Update RAM
- `DELETE /api/ram/{id}/` - Delete RAM
- `GET /api/compare_ram/{ram1}/{ram2}/` - Compare two RAM modules

#### 🎯 Needs Endpoints
- `GET /api/needs/` - List all needs (with pagination and search)
- `POST /api/needs/` - Create new need
- `GET /api/needs/{id}/` - Get specific need details
- `PUT /api/needs/{id}/` - Update need
- `DELETE /api/needs/{id}/` - Delete need

#### 🖥️ PC Comparison Endpoints
- `GET /api/compare_pc/{cpu1}/{gpu1}/{ram1}/{cpu2}/{gpu2}/{ram2}/{need}/` - Compare two PC configurations

### 🔍 Query Parameters

#### Pagination
- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20 for components, 5 for needs)

#### Search
- `search` - Search term (searches in name field)

#### Example Requests
```bash
# Get first page of CPUs
GET /api/cpu/?page=1&page_size=10

# Search for Intel CPUs
GET /api/cpu/?search=Intel

# Compare two CPUs
GET /api/compare_cpu/Intel%20Core%20i7-12700K/AMD%20Ryzen%207%205800X

# Compare two PC configurations for gaming
GET /api/compare_pc/Intel%20Core%20i7-12700K/NVIDIA%20RTX%203080/Corsair%20Vengeance%2032GB/AMD%20Ryzen%207%205800X/NVIDIA%20RTX%203070/G.Skill%20Ripjaws%2016GB/gaming
```

### 📊 Response Examples

#### CPU List Response
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/cpu/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Intel Core i7-12700K",
            "clock_speed_ghz": 3.6,
            "core_count": 12,
            "thread_count": 20,
            "cache_size_l1": 384,
            "cache_size_l2": 12288,
            "cache_size_l3": 25600,
            "tdp_watts": 125,
            "architecture_generation": "Alder Lake",
            "ipc": 1.2
        }
    ]
}
```

#### CPU Comparison Response
```json
[
    {
        "name": "Intel Core i7-12700K",
        "cores_threads": "12c / 20t",
        "tdp": 125,
        "clock_speed": 3.6,
        "l3_cache": 25.6,
        "performance_score": 5184.0
    },
    {
        "name": "AMD Ryzen 7 5800X",
        "cores_threads": "8c / 16t",
        "tdp": 105,
        "clock_speed": 3.8,
        "l3_cache": 32.0,
        "performance_score": 3648.0
    }
]
```

### 🔐 Authentication
Currently, the API does not require authentication for read operations. Write operations (POST, PUT, DELETE) may require authentication in production environments.

### 📈 Rate Limiting
The API implements caching to improve performance:
- CPU/GPU/RAM lists: 15 seconds cache
- Component comparisons: 15 seconds cache
- PC comparisons: 2 minutes cache

---

## 🆕 New Feature: PC Comparison by Need

### 🎯 Description

Now you can compare complete PC configurations based on specific user needs (gaming, work, video editing, 3D rendering, etc.) without the need to create PC objects. Our AI analyzes the components and provides detailed recommendations.

### 🎮 Usage Examples

#### 1. Via API (POST request)

```bash
POST /api/compare_pc_by_need/
```

**Example request:**
```json
{
    "pc1": {
        "cpu_name": "Intel Core i7-12700K",
        "gpu_name": "NVIDIA RTX 3080",
        "ram_name": "Corsair Vengeance 32GB"
    },
    "pc2": {
        "cpu_name": "AMD Ryzen 7 5800X",
        "gpu_name": "NVIDIA RTX 3070",
        "ram_name": "G.Skill Ripjaws 16GB"
    },
    "need": "gaming"
}
```

**Example response:**
```json
{
    "comparison": [
        {
            "pc_name": "PC1",
            "overall_score": 85.6,
            "cpu_score": 2450.8,
            "gpu_score": 1250000.0,
            "ram_score": 51200.0,
            "recommendation": "Excellent choice for gaming thanks to the powerful RTX 3080 GPU",
            "strengths": ["Powerful GPU", "Large RAM capacity", "High CPU performance"],
            "weaknesses": ["High power consumption", "Expensive configuration"]
        },
        {
            "pc_name": "PC2",
            "overall_score": 72.3,
            "cpu_score": 1980.5,
            "gpu_score": 980000.0,
            "ram_score": 25600.0,
            "recommendation": "Good choice for mid-level gaming",
            "strengths": ["Balanced performance", "Energy efficiency"],
            "weaknesses": ["Less VRAM", "Less RAM"]
        }
    ],
    "winner": "PC1",
    "reasoning": "PC1 outperforms PC2 for gaming thanks to the more powerful RTX 3080 GPU with larger VRAM and higher CPU performance"
}
```

#### 2. Via Python code

```python
from core.ai import get_pc_comparison_json

# PC configurations
pc1 = {
    'cpu_name': 'Intel Core i7-12700K',
    'gpu_name': 'NVIDIA RTX 3080',
    'ram_name': 'Corsair Vengeance 32GB'
}

pc2 = {
    'cpu_name': 'AMD Ryzen 7 5800X',
    'gpu_name': 'NVIDIA RTX 3070',
    'ram_name': 'G.Skill Ripjaws 16GB'
}

# Comparison for gaming
result = get_pc_comparison_json(pc1, pc2, "gaming")
print(result)
```

#### 3. Via URL (GET request)

```bash
GET /api/compare_pc/Intel%20Core%20i7-12700K/NVIDIA%20RTX%203080/Corsair%20Vengeance%2032GB/AMD%20Ryzen%207%205800X/NVIDIA%20RTX%203070/G.Skill%20Ripjaws%2016GB/gaming
```

### 🎯 Supported Needs

- 🎮 **Gaming**: GPU priority (60%), CPU (30%), RAM (10%)
- 🎬 **Video editing**: CPU priority (50%), RAM (30%), GPU (20%)
- 💼 **General work**: CPU priority (40%), RAM (40%), GPU (20%)
- 🎨 **3D rendering**: GPU priority (50%), CPU (30%), RAM (20%)

### 🧠 AI Comparison Algorithm

1. **🔍 Component extraction**: Retrieving CPU, GPU, and RAM from database
2. **📊 Performance calculation**: Computing performance score for each component
3. **🎯 Need analysis**: Determining component weights based on need
4. **🤖 AI analysis**: Using OpenAI API for detailed comparison
5. **📋 Result formation**: Structured JSON with recommendations

---

## 📊 Database Population

### 🎮 Populate with GPU Data

```bash
python populate_gpu_data.py
```

**Includes:**
- 🟢 NVIDIA RTX 40xx Series (4090, 4080, 4070 Ti, 4070, 4060 Ti, 4060)
- 🔴 AMD RX 7000 Series (7900 XTX, 7900 XT, 7800 XT, 7700 XT, 7600)
- 🔵 Intel Arc Series (A770, A750, A580)
- 📈 Previous Generation Models (RTX 3090, RTX 3080, RX 6900 XT, RX 6800 XT)

### 🖥️ Populate with CPU Data

```bash
python populate_cpu_data.py
```

**Includes:**
- 🔵 Intel Core 13-14th Gen (i9-14900K, i7-14700K, i5-14600K, i9-13900K, i7-13700K)
- 🔴 AMD Ryzen 7000 Series (7950X, 7900X, 7700X, 7600X, 5950X)
- 💻 Mobile Processors (i9-13900H, i7-13700H, Ryzen 9 7945HX, Ryzen 7 7840HS)

### 🎯 Populate All Data

```bash
python populate_all_data.py
```

**This will populate both CPUs and GPUs with comprehensive data and show detailed statistics.**

---

## 🏗️ Project Structure

```
WisePick/
├── 📁 core/                    # Main application
│   ├── 📄 models.py           # Database models
│   ├── 📄 views.py            # View logic
│   ├── 📄 urls.py             # URL routing
│   ├── 📄 serializers.py      # API serializers
│   ├── 📄 ai.py               # AI recommendation engine
│   └── 📁 templates/          # HTML templates
├── 📁 WisePick/               # Project settings
│   ├── 📄 settings.py         # Django settings
│   ├── 📄 urls.py             # Main URL configuration
│   └── 📄 wsgi.py             # WSGI configuration
├── 📄 manage.py               # Django management script
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md              # This file
```

---

## 🎮 Features Overview

### 🤖 AI Recommendations
- **Smart Matching**: AI analyzes compatibility between CPUs and GPUs
- **Performance Prediction**: Predicts gaming and workstation performance
- **Bottleneck Detection**: Identifies potential performance bottlenecks
- **Value Analysis**: Finds the best price-to-performance ratios

### 📊 Component Database
- **Latest Models**: Up-to-date with newest releases
- **Detailed Specs**: Complete technical specifications
- **Benchmark Data**: Real-world performance metrics
- **Price Tracking**: Current market prices (when available)

### 🎯 Use Cases
- 🎮 **Gaming PCs**: Optimized for high FPS and smooth gameplay
- 💼 **Workstations**: Professional applications and content creation
- 🏠 **Home PCs**: Everyday computing and multimedia
- 🎨 **Creative Work**: Video editing, 3D rendering, and design

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
OPENROUTER_API_KEY=your-openrouter-api-key-here
```

### Database Settings

The project supports multiple database backends:

- **SQLite** (default) - Good for development
- **PostgreSQL** - Recommended for production
- **MySQL** - Alternative option

---

## 🧪 Testing

### Run Tests

```bash
python manage.py test
```

### Run with Coverage

```bash
coverage run --source='.' manage.py test
coverage report
```

---

## 🚀 Deployment

### 🐳 Docker Deployment (Recommended)

#### Quick Start with Docker Compose
```bash
# Clone the repository
git clone <repository-url>
cd WisePick

# Create .env file
cp env.example .env
# Edit .env with your settings

# Start the application (migrations and data population happen automatically)
docker-compose up -d

# Access the application
# http://localhost:8000
# Admin panel: http://localhost:8000/admin/ (admin/admin123)
# API: http://localhost:8000/api/
```

#### Manual Docker Build
```bash
# Build the image
docker build -t wisepick .

# Run with environment variables
docker run -p 8000:8000 \
  -e DEBUG=True \
  -e SECRET_KEY=your-secret-key \
  -e OPENROUTER_API_KEY=your-api-key \
  wisepick
```

### 🏭 Production Deployment

#### Environment Setup
```bash
# Set production settings
export DJANGO_SETTINGS_MODULE=WisePick.settings
export DEBUG=False
export SECRET_KEY=your-production-secret-key
export ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
export OPENROUTER_API_KEY=your-production-api-key
export REDIS_URL=redis://your-redis-server:6379/0
```

#### Database Migration
```bash
# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser
```

#### Web Server Configuration

##### With Gunicorn
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn --bind 0.0.0.0:8000 WisePick.wsgi:application
```

##### With Nginx (Production)
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/your/staticfiles/;
    }

    location /media/ {
        alias /path/to/your/media/;
    }
}
```

#### Docker Production Setup
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-production-secret-key
      - ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    restart: unless-stopped

volumes:
  redis_data:
```

### 🔧 Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - defaults to SQLite)
DATABASE_URL=sqlite:///db.sqlite3

# AI API
OPENROUTER_API_KEY=your-openrouter-api-key-here

# Redis Cache
REDIS_URL=redis://127.0.0.1:6379/0

# CORS Settings
CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_CREDENTIALS=True
```

---

## 👨‍💻 Development Guide

### 🛠️ Development Setup

#### Prerequisites
- Python 3.12+
- Redis server
- Git

#### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd WisePick

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # If available

# Set up environment variables
cp .env.example .env
# Edit .env with your settings

# Start Redis (if not using Docker)
redis-server

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

#### Development with Docker
```bash
# Start development environment (migrations and data population happen automatically)
docker-compose up -d

# Access Django shell
docker-compose exec web python manage.py shell

# View logs
docker-compose logs -f web

# Rebuild if you made changes
docker-compose up --build -d
```

### 🧪 Testing

#### Run Tests
```bash
# Run all tests
python manage.py test

# Run specific test
python manage.py test core.tests.TestCPUComparison

# Run with coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

#### Test Database Population
```bash
# Populate with sample data
python manage.py shell
>>> from core.models import CPU, GPU, RAM
>>> # Add sample data or use management commands
```

### 🔧 Code Quality

#### Linting
```bash
# Install linting tools
pip install flake8 black isort

# Run linting
flake8 .
black .
isort .
```

#### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### 📊 Database Management

#### Migrations
```bash
# Create migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
```

#### Data Population Scripts
```bash
# Populate GPU data
python populate_gpu_data.py

# Populate CPU data
python populate_cpu_data.py

# Populate all data
python populate_all_data.py
```

### 🐛 Debugging

#### Django Debug Toolbar
```bash
# Install debug toolbar
pip install django-debug-toolbar

# Add to INSTALLED_APPS in settings.py
INSTALLED_APPS = [
    # ... other apps
    'debug_toolbar',
]

# Add to MIDDLEWARE
MIDDLEWARE = [
    # ... other middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

#### Logging Configuration
```python
# In settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### 🚀 Performance Optimization

#### Caching
- Redis is used for caching API responses
- Cache keys are prefixed for different views
- Cache duration varies by endpoint (15s-2min)

#### Database Optimization
- Use `select_related()` and `prefetch_related()` for queries
- Add database indexes for frequently queried fields
- Use pagination for large datasets

#### API Optimization
- Implement rate limiting for production
- Use compression for API responses
- Consider implementing API versioning

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🚀 Getting Started

1. 🍴 **Fork the repository**
2. 🌿 **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. 💻 **Make your changes**
4. ✅ **Add tests** for new functionality
5. 📝 **Update documentation** for any changes
6. 🔄 **Submit a pull request**

### 🎯 Development Guidelines

#### Code Style
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions small and focused

#### Testing
- Write comprehensive tests for new features
- Maintain test coverage above 80%
- Test both success and error cases
- Use descriptive test names

#### Documentation
- Update README.md for user-facing changes
- Add docstrings to new functions/classes
- Update API documentation for new endpoints
- Include examples in documentation

#### Commit Messages
Use conventional commit format:
```
type(scope): description

feat(api): add new CPU comparison endpoint
fix(ai): resolve OpenAI API timeout issue
docs(readme): update installation instructions
test(core): add tests for GPU comparison
```

#### Pull Request Process
1. Ensure all tests pass
2. Update documentation
3. Add screenshots for UI changes
4. Provide clear description of changes
5. Link to any related issues

### 🐛 Bug Reports

When reporting bugs, please include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots if applicable

### 💡 Feature Requests

For feature requests, please:
- Check existing issues first
- Provide clear use case
- Explain the expected behavior
- Consider implementation complexity

### 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

---

## 📈 Roadmap

### 🎯 Version 1.0 (Current) ✅
- ✅ Basic CPU/GPU/RAM database
- ✅ AI recommendation engine with OpenAI API
- ✅ RESTful API with Django REST Framework
- ✅ Web interface with HTML templates
- ✅ Component compatibility checking
- ✅ PC comparison by need (gaming, work, etc.)
- ✅ Redis caching for performance
- ✅ Docker containerization
- ✅ Comprehensive documentation

### 🚀 Version 2.0 (Planned) 🔄
- 🔮 Advanced AI algorithms with custom models
- 📱 Mobile application (React Native/Flutter)
- 🌐 Enhanced API with authentication
- 💰 Price tracking and market analysis
- 📊 Advanced analytics dashboard
- 🎮 Gaming performance benchmarks
- 🔍 Advanced search and filtering
- 📈 Performance prediction models

### 🌟 Version 3.0 (Future) 🔮
- 🤖 Machine learning improvements
- 🎮 Real-time gaming benchmark integration
- 📊 Real-time market analysis
- 🌍 Multi-language support
- 🔗 Third-party marketplace integration
- 🏆 Community features and reviews
- 📱 Progressive Web App (PWA)
- 🧠 Personalized recommendations

### 🎯 Version 4.0 (Vision) 🚀
- 🌐 Cloud-native architecture
- 🔄 Real-time component updates
- 🤖 AI-powered build optimization
- 📱 Cross-platform mobile apps
- 🎮 VR/AR integration
- 🔗 IoT device integration
- 🌍 Global marketplace
- 🏢 Enterprise features

---

## 🏆 Why Choose WisePick?

### 🎯 **Smart & Accurate**
Our AI engine provides precise recommendations based on real-world performance data and advanced algorithms.

### ⚡ **Fast & Efficient**
Lightning-fast search and comparison tools with Redis caching help you make decisions quickly.

### 💰 **Value-Focused**
Find the best components for your budget without compromising performance using our intelligent scoring system.

### 🔄 **Always Updated**
Regular database updates ensure you have access to the latest components from Intel, AMD, and NVIDIA.

### 🎮 **Gaming Optimized**
Specialized algorithms for gaming performance and compatibility with detailed analysis.

### 🚀 **Developer Friendly**
Complete REST API, comprehensive documentation, and Docker support for easy integration.

### 🔧 **Production Ready**
Built with Django best practices, Redis caching, and Docker containerization for reliable deployment.

### 📊 **Data-Driven**
Advanced performance scoring and comparison algorithms based on real-world benchmarks.

---

## 📞 Support

### 🐛 Bug Reports
Found a bug? Please report it with detailed information:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots if applicable

### 💡 Feature Requests
Have an idea for a new feature? We'd love to hear about it!
- Check existing issues first
- Provide clear use case
- Explain the expected behavior
- Consider implementation complexity

### 📚 Documentation
Need help? Check our comprehensive documentation:
- [API Documentation](#-api-documentation)
- [Development Guide](#-development-guide)
- [Deployment Guide](#-deployment)
- [Contributing Guide](#-contributing)

### 💬 Community
- GitHub Issues for bug reports and feature requests
- GitHub Discussions for questions and ideas
- Pull Requests for contributions

### 🔧 Troubleshooting

#### Common Issues
1. **Redis Connection Error**
   ```bash
   # Make sure Redis is running
   redis-server
   # Or with Docker
   docker run -d -p 6379:6379 redis:7-alpine
   ```

2. **OpenAI API Error**
   ```bash
   # Check your API key in .env file
   OPENROUTER_API_KEY=your-api-key-here
   ```

3. **Database Migration Issues**
   ```bash
   # Reset migrations
   python manage.py migrate --fake-initial
   ```

4. **Docker Build Issues**
   ```bash
   # Clean Docker cache
   docker system prune -a
   docker-compose build --no-cache
   ```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- 🎮 **Gaming Community** - For feedback and testing
- 🤖 **AI/ML Community** - For inspiration and algorithms
- 💻 **Open Source Community** - For amazing tools and libraries
- 🎯 **Django Community** - For the excellent framework
- 🚀 **Django REST Framework** - For the powerful API framework
- 📈 **Redis Community** - For the fast caching solution
- 🐳 **Docker Community** - For containerization support
- 🌐 **OpenAI/OpenRouter** - For AI capabilities
- 📚 **Documentation Contributors** - For improving our docs
- 🧪 **Test Contributors** - For ensuring code quality

---

## 🎉 Get Started Today!

Ready to build your perfect PC? Start with WisePick and let our AI guide you to the best component combinations!

### 🚀 Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd WisePick

# Start with Docker (Recommended)
docker-compose up -d

# Or start locally
python manage.py runserver
```

### 🌐 Access the Application
- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/schema/swagger-ui/
- **Admin Panel**: http://localhost:8000/admin/

### 📱 Try the API
```bash
# Get all CPUs
curl http://localhost:8000/api/cpu/

# Compare two CPUs
curl "http://localhost:8000/api/compare_cpu/Intel%20Core%20i7-12700K/AMD%20Ryzen%207%205800X"

# Compare PC configurations
curl "http://localhost:8000/api/compare_pc/Intel%20Core%20i7-12700K/NVIDIA%20RTX%203080/Corsair%20Vengeance%2032GB/AMD%20Ryzen%207%205800X/NVIDIA%20RTX%203070/G.Skill%20Ripjaws%2016GB/gaming"
```

**Happy Building! 🚀💻🎮**

---

*Made with ❤️ by the WisePick Team*

### 📊 Project Stats
- **Lines of Code**: 1000+
- **API Endpoints**: 15+
- **Supported Components**: 100+
- **AI Models**: OpenAI GPT
- **Caching**: Redis
- **Containerization**: Docker 