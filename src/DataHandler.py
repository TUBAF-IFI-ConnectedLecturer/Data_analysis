import pandas as pd

from ConfigManager import ConfigManager

class DataHandler:
    """Class for loading and saving data from/to files based on YAML configuration."""
    
    def __init__(self, config_path: str):
        """Initialize with the path to the configuration file."""
        self.config_path = config_path
        self.config_manager = ConfigManager(config_path)
    
    def load_data(self, config_entry):
        """Load data from a file and return it as a DataFrame."""
        # Load the configuration
        self.config_manager.load()
        
        # Get the data path from the configuration
        data_path = self.config_manager.get(config_entry)
        
        # Show which file is being loaded
        from pathlib import Path
        file_name = Path(data_path).name
        print(f"📂 Lade: {file_name}")
        
        # Load the DataFrame from the specified path
        df = pd.read_pickle(data_path)
        
        print(f"   ✅ Geladen: {df.shape[0]:,} Zeilen × {df.shape[1]} Spalten")
        return df
    
    def save_data(self, df: pd.DataFrame, config_entry: str):
        """Save a DataFrame to a file specified in the configuration."""
        import os
        from datetime import datetime
        from pathlib import Path
        
        # Load the configuration
        self.config_manager.load()
        
        # Get the data path from the configuration
        data_path = self.config_manager.get(config_entry)
        data_path = Path(data_path)
        
        # Create directory if it doesn't exist
        data_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Record start time
        start_time = datetime.now()
        
        # Save the DataFrame to the specified path
        df.to_pickle(data_path)
        
        # Record end time and calculate duration
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Get file size
        if data_path.exists():
            file_size_bytes = os.path.getsize(data_path)
            file_size_mb = file_size_bytes / (1024 * 1024)
            
            # Format file size
            if file_size_mb < 1:
                size_str = f"{file_size_bytes / 1024:.1f} KB"
            elif file_size_mb < 1024:
                size_str = f"{file_size_mb:.1f} MB"
            else:
                size_str = f"{file_size_mb / 1024:.1f} GB"
        else:
            size_str = "Unknown"
        
        # Print detailed save information
        print(f"💾 Datei gespeichert: {data_path.name}")
        print(f"   📁 Pfad: {data_path}")
        print(f"   📊 DataFrame: {df.shape[0]:,} Zeilen × {df.shape[1]} Spalten")
        print(f"   📏 Dateigröße: {size_str}")
        print(f"   🕐 Zeitstempel: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   ⏱️  Speicherdauer: {duration:.2f} Sekunden")
