import streamlit as st
import Function
todos = Function.get_todos()


def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    Function.write_todos(todos)


st.title("My TODO App")
st.subheader("This is my daily item list")
st.write("Lets see what I got on list")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        Function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New Todo", placeholder='Add new todo',
              on_change=add_todo, key='new_todo')
