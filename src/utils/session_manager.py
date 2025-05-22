"""Session state management utilities."""

import streamlit as st
from typing import List, Dict

class SessionManager:
    """Manage Streamlit session state for the chatbot."""
    
    @staticmethod
    def initialize_session_state():
        """Initialize session state variables."""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        if "api_key_validated" not in st.session_state:
            st.session_state.api_key_validated = False
        
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = "gpt-3.5-turbo"
    
    @staticmethod
    def add_message(role: str, content: str):
        """Add a message to the session state."""
        st.session_state.messages.append({"role": role, "content": content})
    
    @staticmethod
    def get_messages() -> List[Dict[str, str]]:
        """Get all messages from session state."""
        return st.session_state.messages
    
    @staticmethod
    def clear_messages():
        """Clear all messages from session state."""
        st.session_state.messages = []
    
    @staticmethod
    def export_conversation() -> str:
        """Export conversation as text."""
        messages = st.session_state.messages
        conversation = []
        
        for msg in messages:
            role = msg["role"].capitalize()
            content = msg["content"]
            conversation.append(f"{role}: {content}\n")
        
        return "\n".join(conversation)
