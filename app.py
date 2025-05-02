import streamlit as st

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

    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    result = None
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")
        
        if result is not None:
            st.success(f"Result: {result}")

# --- To-Do List Section ---
elif selection == "To-Do List":
    st.title("📝 To-Do List")

    st.write("Add and manage your daily tasks.")

    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("Enter a new task")
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.success("Task added!")
        else:
            st.warning("Please enter a task before adding.")

    st.subheader("Your Tasks")
    updated_tasks = []
    for i, task in enumerate(st.session_state.tasks):
        is_done = st.checkbox(task["task"], value=task["done"], key=f"task_{i}")
        updated_tasks.append({"task": task["task"], "done": is_done})

    st.session_state.tasks = updated_tasks

    if st.button("Clear Completed Tasks"):
        st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
        st.success("Completed tasks removed.")
