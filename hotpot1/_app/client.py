import requests
from lime.common.inference.cpl_client import (
    CPLModelObj,
)

base_url = 'http://localhost:5000/'
end_point = 'infer'

obj = CPLModelObj('my_cpl_basic')

def send_infer(
        question: str,
    ) -> str:
    data = {
        'question': question,
        'style': 'basic',
    }
    response = requests.post(base_url + end_point, json=data)
    if response.status_code == 200:
        result = response.json()
        return result.get('answer')

if __name__ == "__main__":

    # question = 'What is the capital of France?'
    # answer = infer_cpl(question)
    # print(answer)

    # question = "Where is Amelia Earhart from?"
    # answer = send_infer(question)
    # print(answer)

    print(f'check_cpl: {obj.check_valid()}')