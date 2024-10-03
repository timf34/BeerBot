import pywhatkit
import openai
from secrets import OPENAI_KEY

client = openai.Client(api_key=OPENAI_KEY)

specific_contact = "+353834551238"
specific_group_id = "JKjj0IEW4pLK87sBj53jBY"  # Group ID is found from the invite link of the group chat


def generate_poem():
    prompt = "Compose an original Irish poem, encouraging one's friends to get a pint with them at 9pm this evening. Specifically we'll meet at Chaplines Pub at 9pm. Keep it short and concise, and following the typical old trad music/ traditional Irish pub structure of written in any number of quatrains. alliterated, 2 word alliteration in each line. written with aicill rhyme, the end word of L3 internally rhymes with L4. But keep it to 4 lines long, finishing with a poetic line to meet at Chaplins at 9pm, you must mention 9pm, and follow old Irish style and references"
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    print(response)
    poem = response.choices[0].message.content.strip()
    return poem

poem = generate_poem()
poem += "\nWith love, \nBeerBot"

print(poem)
pywhatkit.sendwhatmsg_to_group_instantly(specific_contact, poem)