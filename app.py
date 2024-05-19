import streamlit as st

def main():
    st.title("Hello Streamlit App")
    
    # Text input field for user to enter "hello"
    user_input = st.text_input("Enter 'hello' here:")
    
    # Check if user input is "hello" and display "hello" if it is
    if user_input.lower() == "hello":
        st.write("Hello")

if __name__ == "__main__":
    main()
