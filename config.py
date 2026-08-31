import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
MESHY_API_KEY = os.getenv('MESHY_API_KEY', '')
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN', '')
HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY', '')

# Printer specifications (in mm)
PRINTERS = {
    'P1S': {
        'name': 'Bambu Lab P1S',
        'max_x': 256,
        'max_y': 256,
        'max_z': 256,
        'nozzle_diameter': 0.4,
    },
    'A1_MINI': {
        'name': 'Bambu Lab A1 mini',
        'max_x': 165,
        'max_y': 165,
        'max_z': 180,
        'nozzle_diameter': 0.4,
    }
}

# Connector specifications
CONNECTORS = {
    'NONE': {'name': 'No connectors', 'description': 'Just parts'},
    'TONGUE_GROOVE': {'name': 'Tongue & Groove', 'tongue_width': 5, 'groove_depth': 3},
    'PIN': {'name': 'Pin Joint', 'pin_diameter': 6, 'tolerance': 0.2},
    'MAGNETIC': {'name': 'Magnetic', 'magnet_diameter': 10, 'magnet_depth': 5},
}

# Relief specifications
RELIEF_TYPES = {
    'FULL_3D': {'name': '3D All sides'},
    'RELIEF_FLAT': {'name': 'Relief front / Flat back', 'relief_depth_percent': [5, 10, 15, 20]},
}

# Project paths
PROJECTS_DIR = 'projects'
if not os.path.exists(PROJECTS_DIR):
    os.makedirs(PROJECTS_DIR)

# ИИ сервисы для 3D из фото
AI_SERVICES = {
    'meshy': {
        'name': 'Meshy.ai',
        'free_quota': 10,
        'quality': 'High',
        'speed': 'Medium',
        'requires_api_key': True,
    },
    'replicate': {
        'name': 'Replicate',
        'free_quota': 'Unlimited (but slow)',
        'quality': 'Medium-High',
        'speed': 'Slow',
        'requires_api_key': True,
    },
    'huggingface': {
        'name': 'Hugging Face',
        'free_quota': 'Unlimited',
        'quality': 'Medium',
        'speed': 'Medium',
        'requires_api_key': True,
    },
}
