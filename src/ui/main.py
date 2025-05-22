"""Main UI module for the OpenAI Chatbot."""

import streamlit as st
from ..config.settings import Settings
from ..services.openai_service import OpenAIService
from ..utils.session_manager import SessionManager
from .components import UIComponents

def main():
    """Main application function."""
    # Configure the Streamlit page
    st.set_page_config(**Settings.get_app_config())
    
    # Initialize session state
    SessionManager.initialize_session_state()
    
    # Render header
    UIComponents.render_header()
    
    # Render sidebar and get configuration
    config = UIComponents.render_sidebar()
    
    # Get API key
    api_key = Settings.get_openai_api_key()
    if not api_key:
        api_key = UIComponents.render_api_key_input()
    
    if not api_key:
        st.stop()
    
    # Initialize OpenAI service
    openai_service = OpenAIService(
        api_key=api_key, 
        model=config["model"]
    )
    
    # Validate API key
    if not st.session_state.api_key_validated:
        if openai_service.validate_api_key():
            st.session_state.api_key_validated = True
            st.success("✅ API key validated successfully!")
        else:
            st.error("❌ Invalid API key. Please check your key and try again.")
            st.stop()
    
    # Render existing chat messages
    UIComponents.render_chat_messages()
    
    # Handle new user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to session state and display
        SessionManager.add_message("user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            stream = openai_service.create_chat_completion(
                messages=SessionManager.get_messages(),
                temperature=config["temperature"]
            )
            
            if stream:
                response = st.write_stream(stream)
                SessionManager.add_message("assistant", response)
            else:
                st.error("Failed to generate response. Please try again.")

if __name__ == "__main__":
    main()
