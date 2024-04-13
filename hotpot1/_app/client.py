import json
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
    if response.status_code < 400:
        result = response.json()
        return result.get('answer')
    else:
        print('error on repsponse')
        try: res_data = response.json()
        except Exception as e: print(f'error on response.json(): {str(e)}')
        print(json.dumps(res_data, indent=4))
        

if __name__ == "__main__":

    # question = 'What is the capital of France?'
    # answer = infer_cpl(question)
    # print(answer)
    
    print(f'check_cpl: {obj.check_valid()}')

    question = "Where is Amelia Earhart from?"
    answer = send_infer(question)
    print(answer)
