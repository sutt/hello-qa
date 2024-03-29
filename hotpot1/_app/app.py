from typing import (
    Any,
)
from lime.common.inference.cpl_server import (
    CPLBaseServer,
)
import dspy

# helpers functions

class BasicQA(dspy.Signature):
    """Answer questions with short factoid answers."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")

class GenerateAnswer(dspy.Signature):
    """Answer questions with short factoid answers."""

    context = dspy.InputField(desc="may contain relevant facts")
    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")

class BasicRAG(dspy.Module):
    def __init__(self, num_passages=3):
        super().__init__()

        self.retrieve = dspy.Retrieve(k=num_passages)
        self.generate_answer = dspy.ChainOfThought(GenerateAnswer)
    
    def forward(self, question):
        context = self.retrieve(question).passages
        prediction = self.generate_answer(context=context, question=question)
        return dspy.Prediction(context=context, answer=prediction.answer)

def parse_pred_obj(pred: Any) -> Any:
    if hasattr(pred, 'answer'):
        answer = pred.answer
    else:
        try: answer = pred.completions[0].answer
        except: print(pred)
        return 'Error in dspy model completion'
    return answer

# completion functions

def basic_dspy_infer(question: str, api_key: str) -> str:
    turbo = dspy.OpenAI(
        model='gpt-3.5-turbo', 
        api_key=api_key,
    )
    dspy.settings.configure(
        lm=turbo, 
    )
    generate_answer = dspy.Predict(BasicQA)
    pred = generate_answer(question=question)
    return parse_pred_obj(pred)
    

def rag_dspy_infer(question: str, api_key: str) -> str:
    turbo = dspy.OpenAI(
        model='gpt-3.5-turbo', 
        api_key=api_key,
    )

    colbertv2_wiki17_abstracts = dspy.ColBERTv2(
        url='http://20.102.90.50:2017/wiki17_abstracts'
    )
    
    dspy.settings.configure(
        lm=turbo, 
        rm=colbertv2_wiki17_abstracts,
    )

    generate_answer = BasicRAG()
    pred = generate_answer(question=question)
    
    if hasattr(pred, 'answer'):
        answer = pred.answer
    else:
        try: answer = pred.completions[0].answer
        except: print(pred)
        return 'Error in dspy model completion'
    return answer
    

# Here's where the magic happens: we add our methods to the base class

class MyPipeline(CPLBaseServer):
    
    def __init__(self, server_config={}, server_params={}):
        super().__init__(server_config, server_params)
        if self.server_params.get('flag'):
            print('flag is set!')
        else:
            print('flag is not set!')
        # could set this, but we'll leave it optional for now
        # self.required_infer_keys = ['style']

    def generate_answer(self, question, **kwargs):
        
        api_key = self.secrets.get('OPENAI_API_KEY')
        if api_key is None:
            raise ValueError('OpenAI API key not found in secrets')
        
        infer_style = (
            kwargs.get('style') or 
            self.server_params.get('style') or
            'basic'
        )
        
        if infer_style == 'basic':
            return basic_dspy_infer(question, api_key)
        
        elif infer_style == 'rag':
            return rag_dspy_infer(question, api_key)
        
        else:
            raise ValueError(f'Invalid infer_style: {infer_style}')
        


if __name__ == '__main__':

    configs = {}

    # configs = {
    #     'host': 'localhost',
    #     'port': 5000,
    #     'debug': True,
    # }
    
    my_cpl = MyPipeline(server_config=configs)
    my_cpl.run()
    
