import streamlit



def main():
    streamlit.title('Hello world')
    streamlit.button('Click Here')
    if streamlit.button('Click Me'):
        streamlit.write('buton presed')
    streamlit.checkbox('Click Here')
    user_input = streamlit.text_input("Enter Text","Sample")
    age = streamlit.number_input('Enter Age', min_value=0, max_value=100)


if __name__ == '__main__':
    main()
