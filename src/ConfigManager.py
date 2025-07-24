import yaml
import os
import json
from contextlib import contextmanager
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigManager:
    """Class for managing YAML configuration files."""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize with optional config path."""
        self.config_path = config_path
        self._data = None
        
        # Register custom YAML constructors
        yaml.add_constructor('!join', self._join_constructor, Loader=yaml.SafeLoader)
        
    @staticmethod
    def _join_constructor(loader, node):
        """Custom YAML constructor for !join tag."""
        seq = loader.construct_sequence(node)
        return ''.join([str(i) for i in seq])
    
    @staticmethod
    @contextmanager
    def _safe_open_file(file_path: str, mode: str = 'r'):
        """Safely open and close a file using context manager."""
        try:
            file = open(file_path, mode)
            yield file
        except Exception as e:
            print(f"Error opening file {file_path}: {e}")
            raise
        finally:
            if 'file' in locals() and not file.closed:
                file.close()
    
    def load(self, config_path: Optional[str] = None) -> Dict[str, Any]:
        """Load and parse a YAML config file with custom constructor."""
        # Use provided path or instance path
        path = config_path or self.config_path
        if not path:
            raise ValueError("No config path provided")
            
        if not os.path.exists(path):
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        try:
            with self._safe_open_file(path) as f:
                yaml_content = f.read()
            
            # Use SafeLoader for better security
            self._data = yaml.load(yaml_content, Loader=yaml.SafeLoader)
            return self._data
            
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            raise
    
    @property
    def data(self) -> Dict[str, Any]:
        """Access the loaded configuration data."""
        if self._data is None:
            raise ValueError("No configuration data loaded. Call load() first.")
        return self._data
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value by key with optional default.
        Supports dot notation for accessing nested values (e.g., 'files.df_aimeta').
        
        Args:
            key: The key to look up in the configuration, can be dot-separated for nested access
            default: The default value if key is not found
            
        Returns:
            The value for the given key, or the default if not found
        """
        if self._data is None:
            raise ValueError("No configuration data loaded. Call load() first.")
        
        # Handle nested keys with dot notation
        if '.' in key:
            parts = key.split('.')
            value = self._data
            
            for part in parts:
                if isinstance(value, dict) and part in value:
                    value = value[part]
                else:
                    return default
            
            return value
        else:
            # Simple key lookup
            return self._data.get(key, default)
    
    def pretty_print(self, indent: int = 2, sort_keys: bool = True) -> None:
        """
        Pretty print the configuration data in a readable format.
        
        Args:
            indent: Number of spaces for indentation (default: 2)
            sort_keys: Whether to sort the keys alphabetically (default: True)
        """
        if self._data is None:
            raise ValueError("No configuration data loaded. Call load() first.")
        
        # Use JSON for pretty printing as it's one of the best formatters
        formatted_data = json.dumps(self._data, indent=indent, sort_keys=sort_keys, 
                                   ensure_ascii=False, default=str)
        
        print("\n===== Configuration Data =====")
        print(formatted_data)
        print("=============================\n")