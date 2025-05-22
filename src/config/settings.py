"""Configuration settings for the OpenAI Chatbot."""

import streamlit as st
from typing import Optional
import os

class Settings:
    """Application settings and configuration."""
    
    # OpenAI Configuration
    DEFAULT_MODEL = "gpt-3.5-turbo"
    AVAILABLE_MODELS = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"]
    
    # UI Configuration
    APP_TITLE = "💬 Chatbot"
    PAGE_ICON = "🤖"
    LAYOUT = "centered"
    
    # API Configuration
    MAX_TOKENS = 4096
    TEMPERATURE = 0.7
    
    @staticmethod
    def get_openai_api_key() -> Optional[str]:
        """Get OpenAI API key from secrets or user input."""
        # Try to get from Streamlit secrets first
        try:
            return st.secrets.get("OPENAI_API_KEY")
        except:
            # Fallback to environment variable
            return os.getenv("OPENAI_API_KEY")
    
    @staticmethod
    def get_app_config() -> dict:
        """Get Streamlit app configuration."""
        return {
            "page_title": Settings.APP_TITLE,
            "page_icon": Settings.PAGE_ICON,
            "layout": Settings.LAYOUT,
            "initial_sidebar_state": "expanded"
        }
