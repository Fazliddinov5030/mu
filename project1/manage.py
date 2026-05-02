#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Get the absolute path of this script
    base_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(base_dir))
    
    # Load environment variables from .env file
    try:
        from dotenv import load_dotenv
        env_file = base_dir / '.env'
        if env_file.exists():
            load_dotenv(env_file)
    except ImportError:
        pass  # python-dotenv not installed, continue anyway
    
    # Set default settings module
    settings_module = os.environ.get(
        'DJANGO_SETTINGS_MODULE',
        'config.settings.local'  # Default to local development
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
