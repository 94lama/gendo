#!/bin/bash
# To install effectively the variables, run:  
# ```source ./login```
# from this directory.

echo "Adding the directory to PATH"
export PATH=$PATH:$PWD

echo "Insert you OPENAI API key:"
read api_key
export OPENAI_API_KEY=$api_key
