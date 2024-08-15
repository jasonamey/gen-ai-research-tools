from json import load as load_json, dumps as dump_json
from utils.openapi import get_gpt_query
from utils.perplexity import get_perplexity_query
from utils.exa import process_exa_question


def get_initial_data():
    with open("data/reference-questions.json") as fh:
        data = load_json(fh)
        final = []
        for item in data:
            subject_with_q_and_a = {}
            subject_with_q_and_a["subject"] = item["subject"]
            subject_with_q_and_a["questions"] = []
            for question in item["questions"]:
                question_asked = {}
                question_asked["question"] = question
                question_asked["gpt"] = get_gpt_query(question)
                question_asked["exa"] = process_exa_question(question)
                question_asked["perplexity"] = get_perplexity_query(question)
                subject_with_q_and_a["questions"].append(question_asked)
            final.append(subject_with_q_and_a)
        json_object = dump_json(final, indent=4)
        with open("data/gen-ai-reference-questions-data.json", "w") as fh_2:
            fh_2.write(json_object)


def get_sources_from_perplexity():
    with open("data/gen-ai-data.json") as fh:
        data = load_json(fh)
        final = []
        for item in data:
            subject_with_q_and_a = {}
            subject_with_q_and_a["subject"] = item["subject"]
            subject_with_q_and_a["questions"] = []
            for question in item["questions"]:
                question_asked["perplexity"] = get_perplexity_query(question)
                subject_with_q_and_a["questions"].append(question_asked)
            final.append(subject_with_q_and_a)
        json_object = dump_json(final, indent=4)
        with open("data/academic-resources.json", "w") as fh_2:
            fh_2.write(json_object)
