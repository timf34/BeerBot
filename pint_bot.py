import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
import time

# OpenAI API configuration
openai.api_key = 'YOUR_OPENAI_API_KEY'


def generate_poem():
    prompt = "Compose an original Irish poem."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    poem = response.choices[0].message['content'].strip()
    return poem


def send_whatsapp_message(poem, headless=False, edge_path=None, user_agent=None, edge_driver_path=None):
    # Configure Edge WebDriver
    options = EdgeOptions()
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    try:
        # Open WhatsApp Web
        driver.get('https://web.whatsapp.com')
        print("Please scan the QR code to log in to WhatsApp Web if not already logged in.")
        time.sleep(15)  # Wait for WhatsApp Web to load

        # Find the channel or group
        channel_name = 'oisin English number'  # Replace with your channel name
        search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
        search_box.click()
        search_box.send_keys(channel_name)
        time.sleep(2)
        search_box.send_keys(u'\ue007')  # Press Enter key
        time.sleep(2)

        # Send the message
        message_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
        message_box.click()
        message_box.send_keys(poem)
        message_box.send_keys(u'\ue007')  # Press Enter key to send
        print("Message sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    # poem = generate_poem()
    poem = "this is gonna work..."
    send_whatsapp_message(poem)
