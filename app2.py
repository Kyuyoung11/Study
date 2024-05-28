import streamlit as st

def main():
    st.subheader("KY's TEST")

    menu = ['HOME', 'EDA', 'ML', 'About']

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'HOME':
        st.subheader('HOME')
    
    elif choice == 'EDA':
        st.subheader('탐색적 자료 분석(EDA)')
    
    elif choice == 'ML':
        st.subheader('머신러닝(ML)')
    
    else :
        st.subheader('About')


if __name__ == "__main__":
    main()