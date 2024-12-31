import subprocess
import sys

def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", "requirements.txt"])

def start_app():
    subprocess.check_call([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    install_dependencies()
    start_app()
