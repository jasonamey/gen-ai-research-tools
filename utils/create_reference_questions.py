import re
from json import load as load_json, dumps as dump_json
from openai import OpenAI
from dotenv import load_dotenv


def process_openai_response(response):
    questions = []
    content = response.content
    first_item_info = re.search("1\.", content)
    start, end = first_item_info.span()
    content = content[start:].split("\n")
    for item in content:
        question_nums = re.search("[0-9]\.", item)
        if question_nums:
            start, end = question_nums.span()
            questions.append(item[end + 1 :])
    return questions


def create_reference_questions(subjects):
    load_dotenv()
    client = OpenAI()
    questions_collection = []
    for subject in subjects:
        question_container = {}
        question_container["subject"] = subject
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an information expert, knowledgeable on where to find trusted resources.",
                },
                {
                    "role": "user",
                    "content": "can you find me 10 reference questions on " + subject,
                },
            ],
        )
        response = completion.choices[0].message
        questions = process_openai_response(response)
        question_container["questions"] = questions
        questions_collection.append(question_container)
    return questions_collection


if __name__ == "__main__":
    with open("../data/subjects.json") as fh:
        data = load_json(fh)
        subjects = data["subjects"]
        question_data = create_reference_questions(subjects)
        json_object = dump_json(question_data, indent=4)
        with open("../data/reference-questions.json", "w") as fh_2:
            fh_2.write(json_object)
