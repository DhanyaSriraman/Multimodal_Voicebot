from flask import Flask, render_template, jsonify
from flask import request
import requests
import html5lib
from bs4 import BeautifulSoup
from pipelines import pipeline
from transformers import pipeline as p
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import corpus_bleu
import torch
from sentence_transformers import SentenceTransformer
from googlesearch import search

app = Flask(__name__)


ques_ans = {}
majority_l = {}
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    ll = [x for x in request.form.values()]
    head = ll[0]
    text = ll[1]
    print(text)
    link_list = take_text(head)
    print(link_list)
    nlp = pipeline("multitask-qa-qg")
    question_ans = nlp(text)
    only_question = []
    ques_ans_dict = {}
    ans_all = []
    for dictionary in question_ans:
        only_question.append(dictionary['question'])
        ques_ans_dict[dictionary['question']] = dictionary['answer']
    print(ques_ans_dict)
    print(only_question)
    query_search_text(link_list, only_question, ans_all)
    print(ans_all)
    dict_ans = []
    get_answers(ques_ans_dict, dict_ans)
    maj_list = getMajority(ans_all)
    print(maj_list)
    finalList = []
    importf(dict_ans, maj_list)
    verdict = metrics(dict_ans, maj_list, finalList)
    verdict2 = metrics2(dict_ans, maj_list)
    verdict3 = sbertSimilarity(dict_ans, maj_list)
    score = round(verdict3 * 100, 2)
    if score >= 50:
        return render_template('index.html', prediction_text='This Article is Trustworthy with a S-Bert Score of {}'.format(score))
    else:
        return render_template('index.html', prediction_text='This Article is Fake with a S-Bert Score of {}'.format(score))

@app.route('/ques_ans')
def ques_ans():
    mylist = print_ques_ans()
    return render_template('table.html', prediction_text = mylist)
def take_text(head):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    print(head)
    query = head.split("\n")[0]
    print(query)
    link_list = []
    for j in search(query, tld="co.in", num=4, stop=4, pause=2):
        link_list.append(j)
    return link_list


def query_search_text(link_list, only_question, ans_all):
    new_list = link_list[0: 2]
    for link in new_list:
        print(link)
        URL = link
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        #session = requests.Session()
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        tags = soup.find_all('h1')
        #
        heading = ""
        i = 0
        for t in tags:
            try:
                if i == 0:
                    heading = t.text
                    i += 1
                # print(t.text)
            except:
                continue

        tags1 = soup.find_all('p')
        para = ""
        i = 0
        for t in tags1:
            try:
                # print(t.text)
                para += t.text
            except:
                continue
        answer_from_link(para, only_question, ans_all)

def answer_from_link(para, only_question, ans_obtained_all):
    print(para)
    with torch.no_grad():
        question_answerer = p("question-answering", model='distilbert-base-cased-distilled-squad')
        context = para
        ans = []
        for question in only_question:
            result = question_answerer(question=question, context=context)
            ans.append(result['answer'])
        ans_obtained_all.append(ans)


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

def getMajority(ans):
  n = len(ans)
  m = len(ans[0])
  final = []
  for i in range(0, m):
    temp = []
    for j in range(0, n):
      temp.append(ans[j][i])
    element = most_frequent(temp)
    final.append(element)
  return final

def metrics(list1, list2, newList):
  n = len(list1)
  m = len(list2)
  print(n)
  print(m)
  i = 0
  j = 0
  matching = 0
  non_matching = 0
  while (i < n and j < m):
      if (list1[i] == list2[j]):
          matching += 1
          newList.append(list1[i])
      else:
          non_matching += 1
          newList.append(list2[i])
      i += 1
      j += 1
  score = (matching / len(list1)) * 100
  if matching >= non_matching:
      return "Claim is true" + str(score)
  else :
      return "Claim is false" + str(score)

def metrics2(ans_list, maj_list):
    score = sentence_bleu([ans_list], maj_list, weights=(1, 0, 0, 0))
    print(score)
    if score > 0.7:
        return "Article is Trustworthy and It's Score is" + str(score)
    else:
        return "Article is Fake and It's Score is" + str(score)


def get_answers(dict, ans):
    for ques in dict:
        ans.append(dict[ques])

def sbertSimilarity(ans, maj):
    sentence_transformer_model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = sentence_transformer_model.encode(ans)
    sentence_embeddings2 = sentence_transformer_model.encode(maj)
    cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
    output = torch.mean(cos(torch.tensor(sentence_embeddings), torch.tensor(sentence_embeddings2))).item()
    print(output)
    return output

def importf(dict, list):
    ques_ans = dict
    majority_l = list

def print_ques_ans():
    print_list = []
    # for key in ques_ans:
    #     print_list.append("Ques:- " + key + " ans:- " + ques_ans[key])
    for i in majority_l:
        print_list.appned(" obtained ans:- " + i)
    return print_list


if __name__ == '__main__':
    app.run(debug=True)
