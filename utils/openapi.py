from openai import OpenAI
from dotenv import load_dotenv


def get_gpt_query(question):
    load_dotenv()
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an information expert, knowledgeable on where to find trusted resources.",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    answer = {}
    answer["answer"] = completion.choices[0].message.content
    return answer


# def process_gpt_question(question):
#     answer = {}
#     open_api_response = get_gpt_query(question)
#     answer["answer"] = open_api_response.content
#     return answer


# subject = "asian studies"
# questions = [
#     "What impact did the Silk Road have on cultural exchange between East and West Asia?",
#     "How did Confucianism influence societal structures and governance in East Asian countries?",
# ]
# q = "How did Confucianism influence societal structures and governance in East Asian countries?"


# print(get_gpt_query(q))

# {'answer': 'Confucianism has had a profound impact on societal structures and governance in East Asian countries such as China, Korea, Japan, and Vietnam. Some key ways in which Confucianism has influenced these societies include:\n\n1. **Hierarchy and Social Order**: Confucianism emphasizes the importance of hierarchy and social order, with a focus on the relationships between rulers and subjects, parents and children, husbands and wives, and older and younger siblings. This hierarchical structure has influenced traditional East Asian societies and shaped their social norms and values.\n\n2. **Meritocracy and Education**: Confucianism places a strong emphasis on education and the cultivation of virtues such as wisdom, filial piety, and righteousness. This emphasis on meritocracy has influenced governmental systems in East Asian countries, where civil service examinations based on Confucian teachings were often used to select government officials.\n\n3. **Ethics and Morality**: Confucianism promotes ethics and morality as essential components of governance. Rulers and officials were expected to govern with integrity, benevolence, and wisdom, and to prioritize the well-being of the people. This emphasis on ethical governance has had a lasting impact on the political culture of East Asian countries.\n\n4. **Community and Harmony**: Confucianism emphasizes the importance of harmony within the community and the maintenance of social stability. This emphasis on social cohesion has shaped governance structures in East Asian countries, with a focus on consensus-building, conflict resolution, and the prioritization of the common good.\n\n5. **Continuation of Tradition**: Confucianism places a strong emphasis on the importance of tradition, ritual, and continuity with the past. This emphasis has influenced the governance structures of East Asian countries, where respect for tradition and cultural heritage continues to play a significant role in shaping societal values and norms.\n\nOverall, Confucianism has played a significant role in shaping societal structures and governance in East Asian countries, influencing everything from leadership styles and bureaucratic systems to social values and cultural norms.'}
