import streamlit as st

# Page setup
st.set_page_config(page_title="ChatSphere", layout="wide")

# Sidebar with emoji logo
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;">
            <span style="font-size:60px;">💬</span>
            <h2 style="margin-top:-10px;">ChatSphere</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("A clean & modern Streamlit chat interface.")
    st.markdown("---")
    st.subheader("Menu")
    st.write("• 💬 Chat")
    st.write("• ⚙ Settings (coming soon)")
    st.write("• 📁 Files (coming soon)")

# Main title
st.title("💬 ChatSphere – Smart & Minimal Chat App")

# Session to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat Input
user_input = st.chat_input("Type your message...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Bot simple reply
    bot_reply = f"Echo: {user_input}"
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").markdown(bot_reply)
