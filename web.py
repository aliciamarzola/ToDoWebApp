import func
import streamlit as st

todos = func.get_todos()

def add():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func.write_todos(todos)
    
def complete(checkbox):
    todos = func.get_todos()
    todos.remove(checkbox)
    func.write_todos(todos)

st.title("My To-Do App")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
    
st.text_input(label="", placeholder="Add new todo...",
              on_change=add, key='new_todo')