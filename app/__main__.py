"""Entry point for launching the app"""
from app import build_app

if __name__ == "__main__":
    build_app().run('localhost', port=5000, debug=True)
