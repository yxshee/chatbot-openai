"""OpenAI API service for chat completions."""

from openai import OpenAI
from typing import List, Dict, Generator
import streamlit as st

class OpenAIService:
    """Service class for OpenAI API interactions."""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """Initialize OpenAI service."""
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def create_chat_completion(
        self, 
        messages: List[Dict[str, str]], 
        stream: bool = True,
        temperature: float = 0.7,
        max_tokens: int = 4096
    ) -> Generator:
        """Create a chat completion with streaming."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=stream,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response
        except Exception as e:
            st.error(f"Error creating chat completion: {str(e)}")
            return None
    
    def validate_api_key(self) -> bool:
        """Validate the OpenAI API key."""
        try:
            self.client.models.list()
            return True
        except Exception:
            return False
