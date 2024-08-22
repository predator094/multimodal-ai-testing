import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def my_function():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Find the search box and type 'doraemon'
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("doraemon")

        # Press Enter
        search_box.send_keys(Keys.RETURN)

        st.write("Google opened in a new tab and 'doraemon' searched!")
    finally:
        # Close the WebDriver
        driver.quit()


def main():
    st.title("Streamlit Button Example")

    # Center-aligning the button
    col1, col2, col3 = st.columns([1, 4, 1])

    # Placing the button in the center column
    with col2:
        if st.button("Click me"):
            my_function()


if __name__ == "__main__":
    main()
