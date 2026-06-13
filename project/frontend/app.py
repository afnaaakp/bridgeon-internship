import streamlit as st
import pandas as pd
from datetime import date

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Task Manager Pro",
    page_icon="🗂️",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Register"

if "users" not in st.session_state:
    st.session_state.users = {}

if "user" not in st.session_state:
    st.session_state.user = ""

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

# --------------------------------------------------
# GLOBAL STYLE (PRO UI)
# --------------------------------------------------

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #F5F7FB 0%, #EEF2F7 100%);
}

/* Title */
.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    color: #111827;
}

.subtitle {
    text-align: center;
    color: #6B7280;
    margin-bottom: 20px;
}

/* Buttons */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    font-weight: 600;
    height: 42px;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

/* Card UI */
.card {
    padding: 16px;
    border-radius: 14px;
    background: white;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 12px;
}

/* Metric card */
.metric {
    padding: 20px;
    border-radius: 12px;
    background: white;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("<div class='main-title'>🗂️ Task Manager Pro</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Modern productivity dashboard</div>", unsafe_allow_html=True)

# --------------------------------------------------
# REGISTER
# --------------------------------------------------

def register():
    st.subheader("Create Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not username or not email or not password:
            st.error("All fields required")
            return

        if email in st.session_state.users:
            st.error("User already exists")
            return

        st.session_state.users[email] = {
            "username": username,
            "password": password
        }

        st.success("Account created successfully 🎉")
        st.session_state.page = "Login"
        st.rerun()

# --------------------------------------------------
# LOGIN
# --------------------------------------------------

def login():
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in st.session_state.users and st.session_state.users[email]["password"] == password:

            st.session_state.logged_in = True
            st.session_state.user = st.session_state.users[email]["username"]

            st.success("Login successful 🚀")
            st.rerun()

        else:
            st.error("Invalid credentials")

# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

def dashboard():

    st.markdown(f"## 👋 Welcome, {st.session_state.user}")

    # ---------------- METRICS ----------------
    total = len(st.session_state.tasks)
    completed = sum(t["completed"] for t in st.session_state.tasks)
    pending = total - completed

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"<div class='metric'><h3>📋 Total</h3><h2>{total}</h2></div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"<div class='metric'><h3>✅ Completed</h3><h2>{completed}</h2></div>", unsafe_allow_html=True)

    with col3:
        st.markdown(f"<div class='metric'><h3>⏳ Pending</h3><h2>{pending}</h2></div>", unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- ADD TASK ----------------
    st.subheader("➕ Add New Task")

    col1, col2 = st.columns(2)

    with col1:
        task_name = st.text_input("Task Name")

    with col2:
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    description = st.text_area("Description")
    due_date = st.date_input("Due Date", min_value=date.today())

    if st.button("Create Task"):
        if task_name and description:

            st.session_state.tasks.append({
                "id": st.session_state.next_id,
                "task_name": task_name,
                "description": description,
                "priority": priority,
                "due_date": str(due_date),
                "completed": False
            })

            st.session_state.next_id += 1
            st.success("Task created 🚀")
            st.rerun()

        else:
            st.error("Please fill all fields")

    st.markdown("---")

    # ---------------- TASK LIST ----------------
    st.subheader("📌 Your Tasks")

    if not st.session_state.tasks:
        st.info("No tasks yet. Create your first task 🚀")
        return

    for t in st.session_state.tasks:

        color = "#22C55E" if t["completed"] else "#F59E0B"

        st.markdown(f"""
        <div class="card" style="border-left:6px solid {color}">
            <h4 style="margin:0">{t['task_name']}</h4>
            <p style="color:#6B7280;margin:6px 0">{t['description']}</p>
            <small>📅 {t['due_date']} | 🎯 {t['priority']}</small>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if not t["completed"]:
                if st.button("Mark Done", key=f"done_{t['id']}"):
                    t["completed"] = True
                    st.rerun()

        with col2:
            if st.button("Delete", key=f"del_{t['id']}"):
                st.session_state.tasks = [
                    task for task in st.session_state.tasks
                    if task["id"] != t["id"]
                ]
                st.rerun()

    st.markdown("---")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.page = "Login"
        st.rerun()

# --------------------------------------------------
# APP FLOW
# --------------------------------------------------

if st.session_state.logged_in:
    dashboard()

else:
    if st.session_state.page == "Register":
        register()

        if st.button("Go to Login"):
            st.session_state.page = "Login"
            st.rerun()

    else:
        login()

        if st.button("Go to Register"):
            st.session_state.page = "Register"
            st.rerun()