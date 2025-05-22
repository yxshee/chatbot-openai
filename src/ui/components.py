"""Reusable UI components for the chatbot interface."""

import streamlit as st
from typing import Optional
from ..config.settings import Settings

class UIComponents:
    """Collection of reusable UI components."""
    
    @staticmethod
    def render_header():
        """Render the application header."""
        st.title(Settings.APP_TITLE)
        st.write(
            "This is a simple chatbot that uses OpenAI's GPT models to generate responses. "
            "To use this app, you need to provide an OpenAI API key, which you can get "
            "[here](https://platform.openai.com/account/api-keys). "
        )
    
    @staticmethod
    def render_api_key_input() -> Optional[str]:
        """Render API key input and return the key."""
        api_key = st.text_input(
            "OpenAI API Key", 
            type="password",
            help="Enter your OpenAI API key to start chatting"
        )
        
        if not api_key:
            st.info("Please add your OpenAI API key to continue.", icon="🗝️")
            return None
        
        return api_key
    
    @staticmethod
    def render_sidebar():
        """Render the sidebar with configuration options."""
        with st.sidebar:
            st.header("⚙️ Configuration")
            
            # Model selection
            selected_model = st.selectbox(
                "Choose Model",
                Settings.AVAILABLE_MODELS,
                index=0,
                help="Select the OpenAI model to use"
            )
            st.session_state.selected_model = selected_model
            
            # Temperature setting
            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=2.0,
                value=Settings.TEMPERATURE,
                step=0.1,
                help="Higher values make output more random"
            )
            
            # Clear conversation button
            if st.button("🗑️ Clear Conversation", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
            
            # Export conversation
            if st.session_state.messages:
                from ..utils.session_manager import SessionManager
                conversation_text = SessionManager.export_conversation()
                st.download_button(
                    label="📥 Export Conversation",
                    data=conversation_text,
                    file_name="chatbot_conversation.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            return {"model": selected_model, "temperature": temperature}
    
    @staticmethod
    def render_chat_messages():
        """Render existing chat messages."""
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
