from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

def generate_ad_copy(brand_name,product_desc,target_audience,tone="Exciting"):
    prompt = (
        f"Write a catchy ad headline and a 2-3 sentence marketing description "
        f"in an {tone} tone for {brand_name}, a company offering {product_desc}, "
        f"targeting {target_audience}. Format the output as:\n"
        f"Headline: [your headline]\n"
        f"Description: [your description]"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.9,  
    )

    output = response.choices[0].message.content.strip()

   
    try:
        headline = output.split("Headline:")[1].split("Description:")[0].strip()
        description = output.split("Description:")[1].strip()
    except IndexError:
        headline = "Something went wrong!"
        description = "Couldn’t generate a proper ad copy. Try again!"

    return headline, description


if __name__ == "__main__":
    h, d = generate_ad_copy("GreenVibe", "Eco-friendly reusable water bottles", "Eco-conscious consumers")
    print(f"Headline: {h}\nDescription: {d}")