import os
from openai import OpenAI
from dotenv import load_dotenv


def create_message(question):
    return [
        {
            "role": "system",
            "content": "You are a librarian and you need to offer resources in a helpful, detailed, polite conversation with a user.",
        },
        {
            "role": "user",
            "content": f"{question}",
        },
    ]


def get_perplexity_query(question):
    load_dotenv()
    client = OpenAI(
        api_key=os.environ["PERPLEXITY_API_KEY"], base_url="https://api.perplexity.ai"
    )
    response = client.chat.completions.create(
        model="mistral-7b-instruct",
        messages=create_message(question),
    )
    answer = {}
    print("here is response:", response)
    answer["answer"] = response.choices[0].message.content
    return answer


QUESTION = "can you find me scholarly journal articles on the question of: What impact did the Silk Road have on cultural exchange between East and West Asia?"

print(get_perplexity_query(QUESTION))

# {'answer': "Hello there! I'd be happy to help answer your question. When it comes to international investments, there are indeed some risks that are important to be aware of. Here are some of the major risks:\n\n1. Political Instability: Political instability in a foreign country can lead to economic instability, which can negatively impact your investments. This can include things like government instability, civil unrest, or changes in regulations that can make it difficult for foreign investors to operate.\n2. Currency Risk: When you invest in a foreign country, you are exposing yourself to the risk of currency fluctuations. If the value of the currency in which your investment is denominated declines relative to your home currency, the value of your investment may decrease as well.\n3. Economic Instability: Economic instability in a foreign country can also negatively impact your investments. This can include things like high inflation rates, high levels of debt, or a weak economy.\n4. Legal and Regulatory Risks: Differences in laws and regulations between your home country and the foreign country where you are investing can create risks. This can include things like different accounting standards, different tax laws, or different securities regulations.\n5. Cultural Differences: Cultural differences can also pose risks when it comes to international investments. For example, there may be differences in business practices, communication styles, or attitudes towards risk that can make it difficult to navigate the investment environment.\n\nI hope this information is helpful! If you have any further questions, please don't hesitate to ask. I'm here to help."}
