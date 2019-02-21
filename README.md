# SuggestBot API
SuggestBot API

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
