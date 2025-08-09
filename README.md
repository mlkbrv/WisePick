# 🚀 WisePick - AI-Powered PC Component Comparison

> **Your AI-Powered Guide to Building the Perfect PC** 🎯

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 What is WisePick?

WisePick is an intelligent web application that helps users build the perfect PC by providing smart recommendations for CPU, GPU, and RAM combinations. Our AI-powered system analyzes compatibility, performance, and value to suggest optimal component pairings for your specific needs.

### 🎯 Key Features

- 🤖 **AI-Powered Recommendations** - Get smart suggestions based on your requirements
- 💻 **Comprehensive Database** - Latest CPUs, GPUs, and RAM from Intel, AMD, and NVIDIA
- ⚡ **Performance Analysis** - Detailed benchmarks and compatibility checks
- 🎮 **Gaming Optimized** - Specialized recommendations for gaming builds
- 💰 **Budget-Friendly** - Find the best value for your money
- 📊 **Real-time Comparisons** - Compare different component combinations
- 🆕 **PC Comparison by Need** - Compare full PC configurations based on user needs

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | 🐍 Python 3.8+ |
| **Framework** | 🎯 Django 4.2+ |
| **Database** | 🗄️ SQLite/PostgreSQL |
| **Frontend** | 🎨 HTML5, CSS3, JavaScript |
| **AI Engine** | 🤖 OpenAI API (OpenRouter) |
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
- ✅ PC comparison by need

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