# SuggestBot API
SuggestBot API

## TODO
* `api.py` 파일의 `is_evidence(claim, evidence_sentence)` 함수 구현
* `is_evidence()`
  * claim과 evidence_sentence를 받고, `True`/`False` 반환

## Install

### Install dependencies
* `pip install -r requirements.txt`

### Prepare models
* `python -m spacy download en_core_web_md` (spaCy)

## Start Server
`FLASK_APP=api.py FLASK_DEBUG=1 flask run`

Sample: `http://localhost:5000/?claim=This%20is%20a%20claim`

## API
- GET /
        - Request evidences (Wikipedia) relevent to a given claim.

        - Request

            ```sh
            curl -i -X GET \
            'http://localhost:5000/?claim=This%20is%20a%20claim'
            ```

        - Response

            ```js
            {
                "claim": "This", 
                "evidences": [
                    {
                    "claim": "This", 
                    "evidence": "List of postage stamps of Pakistan from 1967 to 1976\n\nPakistan has, over its 60-year history, issued over 600 issues and 1,100 stamps and souvenir sheets.", 
                    "stance": "NOT IMPLEMENTED! (SUPPORTS | REFUTES)"
                    },
                    ...
                ]
            }
            ```
