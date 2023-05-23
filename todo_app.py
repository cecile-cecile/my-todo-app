import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My TODO App")
st.subheader("Things to do")
st.markdown(":sunglasses: Let's cross these off!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        # Update todos list
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a new TODO:", placeholder="TODO",
              on_change=add_todo, key="new_todo")


st.session_state
