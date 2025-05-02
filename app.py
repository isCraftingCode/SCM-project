import streamlit as st
from datetime import datetime

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Calculator", "To-Do List"])

# --- Home Section ---
if selection == "Home":
    st.title("Simple Utility Tool 🛠️")
    st.subheader("Welcome to the Streamlit Utility App!")
    st.write("""
    This app demonstrates version control and release management for a simple Python utility tool. 
    You can explore two main features using the sidebar:
    
    - 📟 Calculator: Perform basic arithmetic.
    - 📝 To-Do List: Keep track of your tasks.
    
    The app was built as part of a Software Configuration Management course project to practice Git operations like branching, tagging, and merge conflict resolution.
    """)

# --- Calculator Section ---
elif selection == "Calculator":
    st.title("📟 Calculator")

    st.write("Perform basic operations:")

    num1 = st.number_input("Enter first number", step=1.0)
    num2 = st.number_input("Enter second number", step=1.0)

    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Power"])

    result = None
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Power":
            result = num1**num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")
        
        if result is not None:
            st.markdown(
                f"""
                <div style="background-color:#1f375e;padding:10px;border-radius:5px;border:1px solid #d0e9c6;">
                <h4> ✅ Result: {result}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    

# --- To-Do List Section ---
elif selection == "To-Do List":
    st.title("📝 To-Do List")

    st.write("Add and manage your daily tasks.")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    with st.form("task_form", clear_on_submit=True):
        task_text = st.text_input("Enter a new task")
        priority = st.selectbox("Priority",["Low", "Medium", "High"])
        submitted = st.form_submit_button("Add Task")
        if submitted and task_text:
            st.session_state.tasks.append({
                "task": task_text,
                "priority": priority,
                "done": False,
                "created": datetime.now()
            })
            st.success("✅ Task added successfully")

    st.subheader("📋 Your Tasks")
    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.05, 0.65, 0.15, 0.15])
        done = cols[0].checkbox("", value=task["done"], key=f"done_{i}")
        cols[1].markdown(
            f"""
            <div style="padding: 5px;">
                <b>{task['task']}</b>
                <span style="font-size:12px;color:gray;">({task['priority']})</span><br>
                <span style="font-size:11px;color:#888;">Added: {task['created'].strftime('%Y-%m-%d %H:%M:%S')}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        delete = cols[2].button("🗑️", key=f"del_{i}")
        edit = cols[3].button("✏️", key=f"edit_{i}")
        st.session_state.tasks[i]["done"] = done
        if delete:
            st.session_state.tasks.pop(i)
            st.rerun()

        if edit:
            new_text = st.text_input("Edit task", task["task"], key=f"edit_input_{i}")
            if st.button("Save", key=f"save_{i}"):
                st.session_state.tasks[i]["task"] = new_text
                st.rerun()
                



    if st.button("🧹 Clear Completed Tasks"):
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
        st.success("Completed tasks cleared.")
