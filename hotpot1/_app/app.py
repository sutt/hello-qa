from lime.modules.inference.cpl_server import (
    CPLBaseServer,
    CONFIGS,
)
import dspy

# completion functions and helpers

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

def basic_dspy_infer(question: str) -> str:
    turbo = dspy.OpenAI(
        model='gpt-3.5-turbo', 
        api_key=CONFIGS['secrets']['openai_api_key'],
    )

    dspy.settings.configure(
        lm=turbo, 
    )
    generate_answer = dspy.Predict(BasicQA)
    pred = generate_answer(question=question)

    if hasattr(pred, 'answer'):
        answer = pred.answer
    else:
        try: answer = pred.completions[0].answer
        except: print(pred)
        return 'Error in dspy model completion'
    return answer

def rag_dspy_infer(question: str, load_compiled: bool = False) -> str:
    turbo = dspy.OpenAI(
        model='gpt-3.5-turbo', 
        api_key=CONFIGS['secrets']['openai_api_key'],
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


def infer_switch(question: str, model: str = 'basic') -> str:
    if model == 'basic':
        return basic_dspy_infer(question)
    elif model == 'rag':
        return rag_dspy_infer(question)
    else:
        return 'Error: Model not found'

MODEL_TYPE = 'basic'

class MyPipeline(CPLBaseServer):
    def __init__(self, config):
        super().__init__(config)

    def generate_answer(self, question, **kwargs):
        global MODEL_TYPE
        return infer_switch(question, model=MODEL_TYPE)


if __name__ == '__main__':
    
    MODEL_TYPE = 'rag'  # 'basic'

    configs = {}
    # configs = {
    #     'settings': {
    #         'host': 'localhost',
    #         'port': 5000,
    #         'debug': True,
    #     }
    # }
    
    my_cpl = MyPipeline(config=configs)
    my_cpl.run()
    
