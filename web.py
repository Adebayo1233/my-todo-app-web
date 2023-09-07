import streamlit as st
import fuctions
todos = fuctions.get_todos()


def add_todo():
    new_todo = st.session_state['todo_add'] + "\n"
    todos.append(new_todo)
    fuctions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is use for you daily activities")

for index , todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fuctions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo:", placeholder="Add a new todo....", on_change=add_todo, key='todo_add')


st.session_state
