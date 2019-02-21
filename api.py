from flask import Flask
from flask import request
from flask import jsonify
from collections import OrderedDict

from lib.search import search
from lib.search import get_sentences

# For evidence classification

def init_evidence_classifier():
    # TODO: 필요한 모델 초기화 수행
    # TODO: 초기화된 모델 반환
    return []

evidence_classifier = init_evidence_classifier()

def is_evidence(claim, evidence_sentence):
    """
        Args:
            claim (str): 주제문
            evidence_sentence (str): 증거 후보 문장
        Returns:
            is_evidence (bool): True or False
    """
    # TODO: Classify using BERT
    # TODO: cut by score (threshold?)
    # TODO: `is_evidence` - result
    # TODO: evidence_classifier.predict?
    return True


# main
app = Flask(__name__)

@app.route("/", methods=['GET'])
def evidence():
    claim = request.args.get('claim', '')

    # Fetch evidence documents
    docs = [doc['text'] for doc in search(claim)['documents']]

    # Classify evidence sentences
    candidates = get_sentences(docs)
    evidences = []
    for cd in candidates:
        if is_evidence(claim, cd):
            evidences.append({
                'claim': claim,
                'evidence': cd,
                'stance': 'NOT IMPLEMENTED! (SUPPORTS | REFUTES)'
            })

    # build result
    res = OrderedDict({
        'claim': claim,
        'evidences': evidences
    })

    return jsonify(res)