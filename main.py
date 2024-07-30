# main.py
import streamlit as st
from frontend import initialize_session, display_chat_interface

def main():
    initialize_session()
    display_chat_interface()

if __name__ == "__main__":
    main()