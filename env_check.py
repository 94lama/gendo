#!/usr/bin/env python3
"""
Environment variable checker and validator.
Run this script to check if all required environment variables are set.
"""

from config import config

def main():
    print("🔍 Checking environment variables...")
    print()
    
    # Print current configuration
    config.print_config()
    print()
    
    # Validate configuration
    if config.validate():
        print("✅ All required environment variables are set!")
        return 0
    else:
        print("❌ Some required environment variables are missing.")
        print("Please check env_template.txt for the required variables.")
        return 1

if __name__ == "__main__":
    exit(main()) 