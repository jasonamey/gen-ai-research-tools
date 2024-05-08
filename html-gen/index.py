from json import load as load_json


def create_page(subject, content):
    HTML_BASE = '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title>  <style> * {font-family: sans-serif;} h1 {font-size: 40px;} p {line-height: 1.4}</style></head><body>'
    page = HTML_BASE
    HTML_TAIL = "</body></html>"
    with open(f"{subject}.html", "w") as fh:
        page += content
        page += HTML_TAIL
        fh.write(page)


def create_paragraph(text):
    return f"<p >{text}</p>"


def create_h1(text, h1_class):
    return f"<h1 class='{h1_class}'>{text}</h1>"


def create_h2(text, h2_class):
    return f"<h2 class='{h2_class}'>{text}</h2>"


def create_h3(text, h3_class):
    return f"<h2 class='{h3_class}'>{text}</h2>"


def create_link(link_href, link_text):
    return f"<a href={link_href}>{link_text}</a>"


def create_exa_entry(exa_item):
    pass


def create_gpt_entry(gpt_item):
    content = create_h3("GPT 3.5:", "")
    content += create_paragraph(gpt_item["answer"])
    return content


def create_perplexity_entry(perplexity_item):
    content = create_h3("Perplexity:", "")
    content += create_paragraph(perplexity_item["answer"])
    return content


def create_content_for_page(response_item):
    page_content = ""
    page_content += create_h1("subject: " + response_item["subject"].title(), "")
    for question in response_item["questions"]:
        page_content += create_h2(question["question"], "")
        page_content += create_gpt_entry(question["gpt"])
        page_content += create_perplexity_entry(question["perplexity"])
        page_content += "<hr/>"
    return page_content


with open("../data/gen-ai-data.json") as fh:
    item = load_json(fh)
    for answer in item:
        subject = "".join(answer["subject"].lower().split(" "))
        create_page(subject, create_content_for_page(answer))
