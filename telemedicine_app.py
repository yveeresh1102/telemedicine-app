import streamlit as st
from datetime import datetime

# Sample data for the sake of this app
users = {"user1": {"password": "pass1", "name": "John Doe"}}
doctors = {"dr1": {"name": "Dr. Smith", "specialty": "General Practitioner"}}

# Function to authenticate user
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]
    else:
        return None

# Main app layout
def main():
    st.title("Telemedicine Virtual Assistance")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ("Login", "Register", "Book Appointment", "Enter Symptoms", "Video Call"))

    if page == "Login":
        login_page()

    elif page == "Register":
        register_page()

    elif page == "Book Appointment":
        book_appointment()

    elif page == "Enter Symptoms":
        enter_symptoms()

    elif page == "Video Call":
        video_call()

# Login Page
def login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = authenticate(username, password)
        if user:
            st.session_state.user = user
            st.session_state.username = username
            st.success(f"Welcome {user['name']}")
        else:
            st.error("Invalid credentials")

# Register Page (for new users)
def register_page():
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    name = st.text_input("Full Name")
    
    if st.button("Register"):
        if username not in users:
            users[username] = {"password": password, "name": name}
            st.success("User registered successfully")
        else:
            st.error("Username already exists")

# Book Appointment Page
def book_appointment():
    st.subheader("Book an Appointment")
    if 'user' not in st.session_state:
        st.warning("Please login first")
        return
    
    doctor = st.selectbox("Select a Doctor", [doctor['name'] for doctor in doctors.values()])
    date = st.date_input("Choose a Date", min_value=datetime.today())
    time = st.time_input("Choose a Time")
    
    if st.button("Book Appointment"):
        st.success(f"Appointment booked with {doctor} on {date} at {time}")

# Enter Symptoms Page
def enter_symptoms():
    st.subheader("Enter Symptoms")
    if 'user' not in st.session_state:
        st.warning("Please login first")
        return
    
    symptoms = st.text_area("Describe your symptoms")
    
    if st.button("Submit Symptoms"):
        st.success("Symptoms submitted. A doctor will review them shortly.")

# Video Call Page (Placeholder for integration)
def video_call():
    st.subheader("Video Call with Doctor")
    if 'user' not in st.session_state:
        st.warning("Please login first")
        return
    
    st.write("This is a placeholder for video calls.")
    st.write("You can integrate APIs like Twilio for actual video calling.")

if __name__ == "__main__":
    main()
