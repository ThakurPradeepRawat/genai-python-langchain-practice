import streamlit as st
from chat import call_model

st.set_page_config(
    page_title="Pradeep Second Memory",
    page_icon="💬",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #ffffff;
    }

    /* Remove default top padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 6rem;
        max-width: 900px;
    }

    /* Header */
    .chat-header {
        text-align: center;
        padding: 15px 0 25px 0;
    }

    .chat-header h1 {
        font-size: 28px;
        font-weight: 600;
        margin-bottom: 5px;
    }

    .chat-header p {
        color: #6b7280;
        font-size: 14px;
    }

    /* Chat bubbles */
    .user-message {
        background-color: #f0f0f0;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 12px 0 12px auto;
        max-width: 70%;
        width: fit-content;
        line-height: 1.5;
    }

    .ai-message {
        padding: 12px 16px;
        margin: 12px 0;
        max-width: 80%;
        line-height: 1.6;
    }

    /* Input */
    div[data-testid="stChatInput"] {
        padding-bottom: 20px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f7f7f8;
    }

    .sidebar-title {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ---------- Sidebar ----------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">💬 AI Chat</div>',
        unsafe_allow_html=True
    )

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []

    st.divider()

    st.markdown("**Recent Chats**")

    st.button(
        "Python FastAPI Project",
        use_container_width=True
    )

    st.button(
        "LangChain Learning",
        use_container_width=True
    )

    st.button(
        "GATE Preparation",
        use_container_width=True
    )

    st.divider()

    st.caption("AI Chat Interface")


# ---------- Header ----------
st.markdown("""
<div class="chat-header">
    <h1>AI Assistant</h1>
    <p>How can I help you today?</p>
</div>
""", unsafe_allow_html=True)


# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f'<div class="user-message">{message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="ai-message">{message["content"]}</div>',
            unsafe_allow_html=True
        )


# ---------- Chat Input ----------
prompt = st.chat_input("Message AI Assistant...")

if prompt:
    res = call_model(prompt)

    # UI only — temporary message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Dummy response for UI testing
    st.session_state.messages.append({
        "role": "assistant",
        "content": res
    })

    st.rerun()