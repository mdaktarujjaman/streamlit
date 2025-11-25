import streamlit as st

st.title("Chapter Three: Advanced Topics")

col1, col2 = st.columns(2)


with col1:
    st.header("Section 1: Deep Dive into Concepts")
    st.image("https://i.pinimg.com/736x/ec/78/c7/ec78c719d00fa8a62adda8402fc07d94.jpg",  width=200)
    vot1 = st.button("Explore More")

with col2:
    st.header("Section 2: Practical Applications")
    st.image("https://i.pinimg.com/1200x/35/88/16/358816306725b20d22e06555b4573ab4.jpg", width=200)
    vot2 = st.button("Get Started")
    
if vot1:
    st.success("You clicked on Explore More!")
elif vot2:
    st.success("You clicked on Get Started!")


name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Choose your favorite tea:", ["Green Tea", "Black Tea", "Oolong Tea", "Herbal Tea"])

st.write(f"Hello, {name}! Enjoy your {tea} while learning advanced topics.")

with st.expander("Additional Resources"):
    st.markdown("""
    - [Resource 1](https://example.com/resource1)
    - [Resource 2](https://example.com/resource2)
    - [Resource 3](https://example.com/resource3)
    """)
    
    
with st.expander("Additional Resources"):
    st.write("""
             - [Resource 1](https://example.com/resource1)
             - [Resource 2](https://example.com/resource2)
             - [Resource 3](https://example.com/resource3)
        """)
    
st.markdown("### Conclusion")
st.markdown("> Blockquote")