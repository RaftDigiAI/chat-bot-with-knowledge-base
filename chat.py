from langchain.agents import AgentExecutor
from langchain.callbacks.base import BaseCallbackHandler
import streamlit as st
from streamlit_chat import message
from src.agents.setup_agents import setup_agents

from src.prompt_processor.user_message_processor import UserMessageProcessor

prompt_processor = UserMessageProcessor()

agent_executor: AgentExecutor = setup_agents()


def generate_response(user_input):
    return agent_executor.run(input=user_input, callbacks=[BaseCallbackHandler()])


st.title("Ритейл бот")
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
user_input = st.text_input(
    "",
    key="input",
)
if user_input:
    output = generate_response(user_input)
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
