import random
import requests
import time
from openai import OpenAI
from config import OPENAI_KEY, INDIVIDUAL_RECIPIENT_PHONE_NUMBER, WHATSAPP_GROUPCHAT_GROUP_ID, MEETING_TIME, MODEL, CANDIDATE_PUBS

client = OpenAI(api_key=OPENAI_KEY)

system_prompt = ("You are a lyrical old Irish man with great knowledge of the ways of the pint, and keen to poetically encourage"
                 "students out for pints, naming a specific pub and a specific time")


def generate_poem(pub_name: str, meeting_time: str = "9pm") -> str:
    prompt = (
        f"Compose an original Irish poem encouraging friends to meet for a pint at {pub_name} at {meeting_time} this evening. "
        "Keep it short and concise, following the traditional Irish pub song structure with any number of quatrains. "
        "Use alliteration with two words in each line. Write with aicill rhyme, where the end word of line 3 internally rhymes with line 4. "
        "Keep it to 4 lines, finish with a poetic line to meet at the specified pub at 9pm. "
        f"You must mention '{meeting_time}', the location which is {pub_name}, and follow old Irish style and references."
    )

    max_attempts = 10  # Maximum number of attempts to generate a poem that mentions the pub
    for attempt in range(max_attempts):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7  # Adjust for creativity (higher -> more creative)
            )
            poem = response.choices[0].message.content.strip()
            if pub_name.lower() in poem.lower():  # Ensure the pub name is mentioned in the poem
                return poem
            else:
                print(f"Attempt {attempt + 1}: Pub name not mentioned. Retrying...")
                time.sleep(1)  # Brief pause before retrying
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return None
    print("Failed to generate a poem mentioning the pub after multiple attempts.")
    return None


def send_poem(poem: str, recipient_type: str ='individual') -> None:
    if poem is None:
        print("No poem to send. Exiting...")
        return
    poem += "\n\nWith love,\nBeerBot"
    print(f"Sending poem:\n{poem}")
    try:
        if recipient_type == 'group':
            pywhatkit.sendwhatmsg_to_group_instantly(WHATSAPP_GROUPCHAT_GROUP_ID, poem, wait_time=5, tab_close=True, close_time=3)
        else:
            pywhatkit.sendwhatmsg_instantly(INDIVIDUAL_RECIPIENT_PHONE_NUMBER, poem, wait_time=5, tab_close=True, close_time=3)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")


def is_internet_available(test_url="https://www.google.com", timeout=5):
    try:
        requests.get(test_url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


def wait_for_internet_connection(max_retries=60, delay=5):
    retries = 0
    while retries < max_retries:
        if is_internet_available():
            print("Internet connection established!")
            return True
        else:
            print(f"No internet connection. Retrying in {delay} seconds... (Attempt {retries + 1}/{max_retries})")
            time.sleep(delay)
            retries += 1

    print("Max retries reached. Unable to establish a stable internet connection.")
    return False


if __name__ == "__main__":
    if wait_for_internet_connection():
        import pywhatkit
        selected_pub = random.choice(CANDIDATE_PUBS)
        poem = generate_poem(selected_pub, MEETING_TIME)
        send_poem(poem, recipient_type='group')
    else:
        print("No internet connection:') Find a way to get users attention respectfully")