import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def write_ad(
    prompt="Write a creative ad for the following product to run on Facebook aimed at lovers:\n\nProduct: Ferrero Bouquet is a collection of quality red roses and 12 pieces of chocolate to express love this Valentine's Day.",
):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response["choices"][0]["text"]


# >>> response["choices"][0]["text"]
# "\n\nLove is in the air! Show your special someone how much you care this Valentine's Day with a Ferrero Bouquet. Our beautiful red roses and 12 pieces of delicious Ferrero chocolate will make your loved one feel truly special. Express your love and make this Valentine's Day unforgettable with a Ferrero Bouquet!"
