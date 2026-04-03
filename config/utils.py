import os
import json
from typing import Dict, Any, Optional, List
import logging

logger = logging.getLogger(__name__)

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file {file_path}: {e}")
        return None

def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Write data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
        return True
    except (IOError, TypeError) as e:
        logger.error(f"Error writing JSON file {file_path}: {e}")
        return False

def ensure_directory_exists(dir_path: str) -> bool:
    """Ensure a directory exists; create if it doesn't."""
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except OSError as e:
        logger.error(f"Error creating directory {dir_path}: {e}")
        return False

def get_file_extension(file_path: str) -> str:
    """Get the file extension from a file path."""
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def list_files_in_directory(dir_path: str, extensions: Optional[List[str]] = None) -> List[str]:
    """List files in a directory, optionally filtered by extensions."""
    if not os.path.isdir(dir_path):
        logger.error(f"Directory {dir_path} does not exist")
        return []

    files = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            if extensions is None or get_file_extension(file_path) in extensions:
                files.append(file_path)
    return files