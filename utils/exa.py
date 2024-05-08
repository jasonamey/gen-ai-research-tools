import os
import json
from dotenv import load_dotenv
from exa_py import Exa


def get_exa_query(question):
    load_dotenv()
    exa = Exa(os.environ["EXA_API_KEY"])
    response = exa.search_and_contents(
        question,
        highlights=True,
    )
    return response.results


# def process_questions(subject, submitted_questions):
#     exa_responses = {}
#     exa_responses["subject"] = subject
#     exa_responses["questions"] = []
#     for question in submitted_questions:
#         question_response = {}
#         question_response["question"] = question
#         answers = []
#         exa_response = get_exa_query(question)
#         for response in exa_response:
#             response_data = {}
#             response_data["url"] = response.url
#             response_data["title"] = response.title
#             response_data["highlights"] = response.highlights
#             answers.append(response_data)
#         question_response["answers"] = answers
#         exa_responses["questions"].append(question_response)
#     return exa_responses


def process_exa_question(question):
    exa_response = get_exa_query(question)
    final = ""
    for idx, source in enumerate(exa_response):
        item = f"{idx}.\nurl: {source.url}\ntitle:{source.title}\n"
        if source.highlights:
            item += "highlights: "
            for highlight in source.highlights:
                item += f"{highlight}\n"
        item += "+-+-+\n"
        final += item
    answer = {}
    answer["answer"] = final
    return answer

    # response_data = {}
    # response_data["url"] = exa_response.url
    # response_data["title"] = exa_response.title
    # response_data["highlights"] = exa_response.highlights
    # return exa_response


# subject = "asian studies"
# questions = [
#     "What impact did the Silk Road have on cultural exchange between East and West Asia?",
#     "How did Confucianism influence societal structures and governance in East Asian countries?",
# ]

# QUESTION = "How did Confucianism influence societal structures and governance in East Asian countries?"


# print(process_exa_question(QUESTION))

# {'answer': '0.\nurl: https://www.universiteitleiden.nl/en/staffmembers/kiri-paramore\ntitle:Kiri Paramore\nhighlights: His work is positioned in the field of global intellectual history, with a focus on the early modern period in East Asia. He has written on the intellectual histories of Confucianism, Christianity and liberalism in East Asia, focusing on their impacts in mainstream politics. He has more recently written a number of articles and interventions attempting to historicize present debates on the Confucian resurgence underway in contemporary East Asia. He is currently working on a new longue durée history which engages these contemporary issues under the tentative book title The Global Politics of Confucianism: from cosmopolitanism to fascism. Paramore was born and grew up in Sydney and studied Asian Studies and Asian History at the Australian National University, Canberra (B.A.S.\n+-+-+\n1.\nurl: https://www.ias.edu/scholars/yvonne-chiu\ntitle:Yvonne Chiu\nhighlights: Yvonne Chiu is studying the soft authoritarianism in East Asia which, unlike the Middle East and Russia, bears the hallmarks of modernity and achieves significant economic growth. These phenomena interact uniquely with authoritarianism\'s accompanying self-censorship, withdrawal from public life in favor of self-interested material accumulation, and anomie.\n+-+-+\n2.\nurl: https://history.nd.edu/people/liang-cai/\ntitle:Liang - Cai | Department of History | University of Notre Dame\nhighlights: In the light of great divergence between East and West, this book attempts to answer a fundamental question in the formative age of Chinese bureaucratic empires ( 221 BCE -23 CE): could law or morality be sources of power independent from the government and thereby compete with political authority? Witchcraft and the Rise of the First Confucian Empire. Albany, NY: State University of New York Press, 2014. Pg. 300.\n+-+-+\n3.\nurl: https://www.kent.edu/philosophy/jung-yeup-kim\ntitle:Jung-Yeup Kim\nhighlights: Springer Press. 2017 Zhang Zai’s Philosophy of Qi: A Practical Understanding. Lexington Books. 2015. "Economic Equity, the Well-Field System, and Ritual Propriety in the Confucian Philosophy of Qi" Philosophy East and West 64:4, October 2014. “Confucian Ethical Practice as a Method of Creating and Sustaining Whiteheadian Beauty.” Frontiers of Philosophy in China 9:2 (Brill), June 2014.\n+-+-+\n4.\nurl: https://www.ias.edu/scholars/franciscus-verellen\ntitle:Franciscus Verellen\nhighlights: Franciscus Verellen is writing about the origin and growth of \'Heavenly Master\' Daoism in medieval China. His project is to elucidate how ritual relates to communal organization in China\'s indigenous religion, against the backdrop of the propagation of Buddhism and its impact on Chinese thought and society.\n+-+-+\n5.\nurl: https://sunypress.edu/Books/C/Confucianism-A-Habit-of-the-Heart\ntitle:Confucianism, A Habit of the Heart\nhighlights: This book explores this question, bringing the insights of Robert Bellah to a consideration of various expressions of the contemporary Confucian revival. Bellah identified American civil religion as a religious dimension of life that can be found throughout US culture, but one without any formal institutional structure. Rather, this "civil" form of religion provides the ethical principles that command reverence and by which a nation judges itself. Extending Bellah\'s work, contributors from both the social sciences and the humanities conceive of East Asia\'s Confucian revival as a "habit of the heart," an underlying belief system that guides a society, and examine how Confucianism might function as a civil religion in China, Korea, and Japan. They discuss what aspects of Confucian tradition and thought are being embraced; some of the social movements, political factors, and opportunities connected with the revival of the tradition; and why Confucianism has not traveled much beyond East Asia.\n+-+-+\n6.\nurl: http://www.sciea.org/jciea11\ntitle:JCIEA, Vol.11\nhighlights: Chun-chieh HUANG 黃俊傑, Translated by Jan Vrhovski The Opposition of Confucians to Catholicism in the Early Qing Dynasty: Yang Guangxian and Kangxi Calendar Lawsuit (1664-1665) Review of John H. Sagers, Confucian Capitalism: Shibusawa Eiichi, Business Ethics, and Economic Development in Meiji Japan. (Palgrave Studies in Economic History, Palgrave Macmillan, 2018) Review of Patrick Fridenson and Kikkawa Takeo, eds, Ethical Capitalism: Shibusawa Eiichi and Business Leadership in Global Perspective.\n+-+-+\n7.\nurl: https://asia.ubc.ca/profile/donald-baker/\ntitle:Donald Baker - Department of Asian Studies\nhighlights: “The Korean Dilemma: Assuming Perfectibility but Recognizing Moral Frailty” Acta Koreana 22:2 (Dec. 2019), 287-304. “Prioritizing Ki: The Shift Toward Energy and Transformation that Emerged in 19th Century Korea,” Journal of Koreanology (Hanguk Minjok Munhwa) 61 (2016), 123-150. “The Emergence of a Religious Market in Twentieth-Century Korea” Review of Korean Studies. 19:1 (June, 2016), 7-39 *“Privatization of Buddhism in the Chosŏn Dynasty” Sungkyun Journal of East Asian Studies 14:2 (October, 2014), pp. 1-17.\n+-+-+\n8.\nurl: https://medium.com/@ycao0606/how-chinese-cultural-traditions-led-to-political-or-social-change-in-other-east-asian-societies-798c68742047?source=post_internal_links---------3----------------------------\ntitle:How Chinese Cultural traditions led to political or social change in other East Asian societies…\nhighlights: Combing the analysis of three subjects, Japan, Korea, and Vietnam, I would first admit the China’s casting momentous influence on its surrounding neighbors in East Asia, but unfortunately during this particular time period, 1200–1450, many factors, including power shift in China itself, geographical position, political difference, and cultural collisions, collectively triggered the sinification to wane in all three regions.\n+-+-+\n9.\nurl: https://www.ou.edu/cas/philosophy/people/faculty/amy-olberding\ntitle:Amy Olberding\nhighlights: My research is largely concentrated on the ethical aspects of ordinary life, especially as these feature as prominent concerns in early Confucianism. My most recent book, The Wrong of Rudeness, considers just what might tempt us to rudeness and incivility, and reflects on the moral, social, and political reasons we shouldn’t be easy and free with rudeness and incivility. In addition to the everyday ethics of interpersonal interactions, I am interested in how role models, or exemplars, work to inform both moral learning and abstract moral reasoning. Some of my work seeks to examine early Confucian sources and their robustly emulation based orientation, seeking to frame early Chinese moral discourse with reference to exemplars. Finally, I am interested in early Chinese debates about death, grief, and mourning, especially as these offer novel perspectives not commonly found in western-lineage philosophical tradition.\n+-+-+\n'}
