from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

def generate_ad_copy(brand_name, product_desc, target_audience, tone="Exciting"):
    """This func generates a dope ad copy using OpenAI."""
    
    # Simple logs in English
    print(f"===> Starting ad generation for {brand_name}")
    print(f"===> Inputs: Product={product_desc}, Audience={target_audience}, Tone={tone}")

    # Super improved prompt - short, punchy, and creative
    prompt = (
        f"You’re a top-tier ad guru! Craft a killer headline (8 words max) "
        f"and a crisp 4-5 sentence description (40-50 words max) in an {tone} tone "
        f"for {brand_name}, which offers {product_desc}, targeting {target_audience}. "
        f"Make it bold, unique, and irresistible! Output format:\n"
        f"Headline: [your headline]\n"
        f"Description: [your description]"
    )

    # Hit the OpenAI API - hope it works smooth
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Sticking with 3.5 for speed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,  # Tight limit for concise output
            temperature=0.85,  # Creative but controlled
        )
        print("===> API call worked fine!")
    except Exception as e:
        print(f"===> API messed up: {e}")
        return "Oops!", "Something broke, couldn’t get your ad copy."

    # Grab the output
    output = response.choices[0].message.content.strip()

    # Split into headline and desc - fingers crossed for format
    try:
        headline = output.split("Headline:")[1].split("Description:")[0].strip()
        description = output.split("Description:")[1].strip()
        print(f"===> Got Headline: {headline}")
        print(f"===> Got Description: {description}")
    except IndexError:
        print("===> Output format sucks, using fallback")
        headline = "Ad vibes gone wrong!"
        description = "Couldn’t make a proper ad, try again bhai!"

    return headline, description

# Test it out if you run this file
# if __name__ == "__main__":
#     h, d = generate_ad_copy("FitPulse", "High-performance gym wear", "Fitness enthusiasts", "Exciting")
#     print(f"Headline: {h}\nDescription: {d}")