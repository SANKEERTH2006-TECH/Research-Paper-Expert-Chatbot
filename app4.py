import streamlit as st
import pandas as pd

from src.chatbot import (
    search_and_answer,
    clear_history,
    get_history
)

st.set_page_config(
    page_title="Research Paper Expert Chatbot",
    page_icon="📚",
    layout="wide"
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title("📚 Research Paper Expert")

    st.markdown("---")

    st.write("### Features")

    st.success("Semantic Paper Search")

    st.success("Research Paper Summaries")

    st.success("Concept Explanation")

    st.success("Conversation Memory")

    st.success("Follow-up Questions")

    st.success("Vector Database")

    st.markdown("---")

    if st.button("🗑 Clear Conversation"):

        clear_history()

        st.success("Conversation Cleared!")

# ----------------------------------------------------
# Title
# ----------------------------------------------------

st.title("📚 Research Paper Expert Chatbot")

st.write(
"""
Ask questions about Computer Science research papers.

The chatbot searches the vector database,
retrieves the most relevant papers,
summarizes them,
and explains the concepts in simple language.
"""
)

st.markdown("---")

# ----------------------------------------------------
# Search Box
# ----------------------------------------------------

question = st.text_input(

    "Ask a Research Question",

    placeholder="Example: Explain Reinforcement Learning"

)

search = st.button(

    "🔍 Search",

    use_container_width=True

)
# ----------------------------------------------------
# Search Logic
# ----------------------------------------------------

if search:

    if question.strip() == "":
        st.warning("Please enter a research question.")

    else:

        with st.spinner("Searching research papers..."):

            result = search_and_answer(question)

        st.markdown("---")

        # Explanation
        st.subheader("🤖 AI Explanation")
        st.write(result["answer"])

        st.markdown("---")

        # Summary
        st.subheader("📝 Research Summary")
        st.write(result["summary"])

        st.markdown("---")

        # Retrieved Papers
        st.subheader("📄 Retrieved Papers")

        if len(result["papers"]) == 0:
            st.info("No papers found.")

        else:

            for i, paper in enumerate(result["papers"], 1):

                with st.expander(f"📄 Paper {i}"):

                    st.write(f"**Title:** {paper['title']}")
                    st.write(f"**Authors:** {paper['authors']}")
                    st.write(f"**Category:** {paper['category']}")
                    st.write(f"**Similarity Score:** {paper['score']}")
st.markdown("---")

st.subheader("💬 Conversation History")

history = get_history()

if len(history) == 0:

    st.info("No conversation yet.")

else:

    for chat in history:

        st.write("**Question:**", chat["question"])
        st.write("**Answer:**", chat["answer"])
        st.markdown("---")                   