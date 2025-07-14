import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()

class Config:
    """Centralized configuration management for environment variables."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_PROJECT: Optional[str] = os.getenv("OPENAI_PROJECT")
    MODEL: str = os.getenv("MODEL", "o4-mini")
    
    # File Paths
    README_PATH: str = os.getenv("README_PATH", "/README.md")
    
    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that required environment variables are set."""
        required_vars = ["OPENAI_API_KEY"]
        missing_vars = []
        
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            return False
        
        return True
    
    @classmethod
    def print_config(cls):
        """Print current configuration (excluding sensitive data)."""
        print("📋 Current Configuration:")
        for key, value in cls.__annotations__.items():
            if key == "OPENAI_API_KEY":
                # Mask sensitive data
                api_key = getattr(cls, key)
                display_value = f"{api_key[:8]}..." if api_key else "Not set"
                print(f"  {key}: {display_value}")
            else:
                print(f"  {key}: {getattr(cls, key)}")

# Create a global config instance
config = Config() 