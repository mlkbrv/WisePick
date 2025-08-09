# WisePick - AI-Powered PC Component Comparison

WisePick is a Django application for comparing computer components using artificial intelligence.

## Features

- CPU, GPU, and RAM component comparison
- **NEW**: PC configuration comparison based on user needs
- AI-powered performance analysis
- REST API for integration

## New Feature: PC Comparison by Need

### Description

Now you can compare complete PC configurations based on specific user needs (gaming, work, video editing, 3D rendering, etc.) without the need to create PC objects.

### Usage

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
GET /api/compare_pc/Intel%20Core%20i7-12700K/NVIDIA%20RTX%203080/Corsair%20Vengeance%2032GB/AMD%20Ryzen%207%205800X/NVIDIA%20RTX%203070/G.Skill%20Ripjaws%2016GB?need=gaming
```

### Supported Needs

- **Gaming**: GPU priority (60%), CPU (30%), RAM (10%)
- **Video editing**: CPU priority (50%), RAM (30%), GPU (20%)
- **General work**: CPU priority (40%), RAM (40%), GPU (20%)
- **3D rendering**: GPU priority (50%), CPU (30%), RAM (20%)

### Comparison Algorithm

1. **Component extraction**: Retrieving CPU, GPU, and RAM from database
2. **Performance calculation**: Computing performance score for each component
3. **Need analysis**: Determining component weights based on need
4. **AI analysis**: Using OpenAI API for detailed comparison
5. **Result formation**: Structured JSON with recommendations

## Installation and Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables (OPENROUTER_API_KEY)
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Database Population

### Populate RAM Database

To populate the RAM database with popular RAM modules, run:

```bash
# Using Django management command (recommended)
python manage.py populate_ram

# Or using the standalone script
python populate_ram_data.py
```

This will add popular RAM modules from manufacturers like:
- **Corsair**: Vengeance LPX, Vengeance RGB Pro, Dominator Platinum
- **G.Skill**: Ripjaws V, Trident Z RGB, Trident Z Royal
- **Crucial**: Ballistix, Ballistix MAX
- **Kingston**: Fury Beast, Fury Renegade
- **TeamGroup**: T-Force Vulcan Z, T-Force Delta RGB

**Includes:**
- 🟢 DDR4 modules (8GB, 16GB, 32GB, 64GB) at 3200-4000MHz
- 🔵 DDR5 modules (16GB, 32GB, 64GB) at 4800-5600MHz
- 🎨 RGB and non-RGB variants
- 💰 Budget to high-end options

### Populate CPU and GPU Data

Similar scripts are available for CPU and GPU data:

```bash
# Populate CPU data
python manage.py populate_cpu

# Populate GPU data  
python manage.py populate_gpu

# Populate all data at once
python manage.py populate_all
```

## API Endpoints

- `GET /api/cpu/` - CPU list
- `GET /api/gpu/` - GPU list
- `GET /api/ram/` - RAM list
- `GET /api/compare_cpu/<cpu1>/<cpu2>` - CPU comparison
- `GET /api/compare_gpu/<gpu1>/<gpu2>` - GPU comparison
- `GET /api/compare_ram/<ram1>/<ram2>` - RAM comparison
- `POST /api/compare_pc_by_need/` - **NEW**: PC comparison by need
- `GET /api/compare_pc/<cpu1>/<gpu1>/<ram1>/<cpu2>/<gpu2>/<ram2>` - PC comparison via URL 