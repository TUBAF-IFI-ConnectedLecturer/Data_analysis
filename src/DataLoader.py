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
        print(data_path)
        
        # Load the data into a DataFrame
        df = pd.read_pickle(data_path)
        
        return df
    
    def save_data(self, df: pd.DataFrame, config_entry: str):
        """Save a DataFrame to a file specified in the configuration."""
        # Load the configuration
        self.config_manager.load()
        
        # Get the data path from the configuration
        data_path = self.config_manager.get(config_entry)
        
        # Save the DataFrame to the specified path
        df.to_pickle(data_path)
