# 🚀 WisePick - Smart PC Component Selector

> **Your AI-Powered Guide to Building the Perfect PC** 🎯

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 What is WisePick?

WisePick is an intelligent web application that helps users build the perfect PC by providing smart recommendations for CPU and GPU combinations. Our AI-powered system analyzes compatibility, performance, and value to suggest optimal component pairings for your specific needs.

### 🎯 Key Features

- 🤖 **AI-Powered Recommendations** - Get smart suggestions based on your requirements
- 💻 **Comprehensive Database** - Latest CPUs and GPUs from Intel, AMD, and NVIDIA
- ⚡ **Performance Analysis** - Detailed benchmarks and compatibility checks
- 🎮 **Gaming Optimized** - Specialized recommendations for gaming builds
- 💰 **Budget-Friendly** - Find the best value for your money
- 📊 **Real-time Comparisons** - Compare different component combinations

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | 🐍 Python 3.8+ |
| **Framework** | 🎯 Django 4.2+ |
| **Database** | 🗄️ SQLite/PostgreSQL |
| **Frontend** | 🎨 HTML5, CSS3, JavaScript |
| **AI Engine** | 🤖 Custom ML Models |
| **Deployment** | ☁️ Docker Ready |

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
│   └── 📄 ai.py               # AI recommendation engine
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

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t wisepick .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 wisepick
   ```

### Production Deployment

1. **Set production settings**
   ```bash
   export DJANGO_SETTINGS_MODULE=WisePick.settings.production
   ```

2. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn WisePick.wsgi:application
   ```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 **Fork the repository**
2. 🌿 **Create a feature branch**
3. 💻 **Make your changes**
4. ✅ **Add tests**
5. 📝 **Update documentation**
6. 🔄 **Submit a pull request**

### 🎯 Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests
- Update documentation for new features
- Use meaningful commit messages

---

## 📈 Roadmap

### 🎯 Version 1.0 (Current)
- ✅ Basic CPU/GPU database
- ✅ AI recommendation engine
- ✅ Web interface
- ✅ Compatibility checking

### 🚀 Version 2.0 (Planned)
- 🔮 Advanced AI algorithms
- 📱 Mobile application
- 🌐 API for third-party integration
- 💰 Price tracking and alerts

### 🌟 Version 3.0 (Future)
- 🤖 Machine learning improvements
- 🎮 Gaming benchmark integration
- 📊 Real-time market analysis
- 🌍 Multi-language support

---

## 🏆 Why Choose WisePick?

### 🎯 **Smart & Accurate**
Our AI engine provides precise recommendations based on real-world performance data.

### ⚡ **Fast & Efficient**
Lightning-fast search and comparison tools help you make decisions quickly.

### 💰 **Value-Focused**
Find the best components for your budget without compromising performance.

### 🔄 **Always Updated**
Regular database updates ensure you have access to the latest components.

### 🎮 **Gaming Optimized**
Specialized algorithms for gaming performance and compatibility.

---

## 📞 Support

### 🐛 Bug Reports
Found a bug? Please report it with detailed information about your system and the steps to reproduce.

### 💡 Feature Requests
Have an idea for a new feature? We'd love to hear about it!

### 📚 Documentation
Need help? Check our comprehensive documentation and tutorials.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- 🎮 **Gaming Community** - For feedback and testing
- 🤖 **AI/ML Community** - For inspiration and algorithms
- 💻 **Open Source Community** - For amazing tools and libraries
- 🎯 **Django Community** - For the excellent framework

---

## 🎉 Get Started Today!

Ready to build your perfect PC? Start with WisePick and let our AI guide you to the best component combinations!

```bash
git clone <repository-url>
cd WisePick
python manage.py runserver
```

**Happy Building! 🚀💻🎮**

---

*Made with ❤️ by the WisePick Team* 