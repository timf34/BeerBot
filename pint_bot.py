import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

def send_whatsapp_message(poem):
    # Configure Selenium WebDriver (use Chrome in this example)
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')  # To maintain the session
    driver = webdriver.Chrome(options=options)

    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com')
    time.sleep(15)  # Wait for WhatsApp Web to load

    # Find the channel or group
    channel_name = 'Your Channel Name'
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(channel_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Send the message
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.click()
    message_box.send_keys(poem)
    message_box.send_keys(Keys.ENTER)

    # Close the browser
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    poem = generate_poem()
    send_whatsapp_message(poem)
