"""
    this file is to rename some special variables to facilitate their uses  
"""

import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("LLM_MODEL_NAME")
MAX_TOKENS = int(os.getenv("max_tokens"))