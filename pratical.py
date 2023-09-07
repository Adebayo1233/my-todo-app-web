import streamlit as st
import fuctions

todos = fuctions.get_todos()
def add_todo():
    new_todooo = st.session_state["new_todo"] + "\n"
    todos.append(new_todooo)
    fuctions.write_todos(todos)

st.title("")
st.header("")
st.text("")
for index, todo in enumerate(todos):
    check = st.checkbox(todo, key= todo)
    todos.pop(index)
    fuctions.write_todos(todos)
    del session_state[todo]
    st.experimental_rerun()


st.text_input(label="enter a todo", placeholder="Enter a todo", on_change=add_todo, key="new_todo")
