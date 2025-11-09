import sys
import os

# Get the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')

# Add the backend directory to the Python path
sys.path.insert(0, BACKEND_DIR)

# Change working directory to backend so relative paths work
os.chdir(BACKEND_DIR)

from main import app

# Export the FastAPI app for Vercel
handler = app
