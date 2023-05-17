import random
from transformers import pipeline

class PipelineAgent:
    
    def __init__(self, prompt, question='Noting'):
        self.prompt = prompt
        self.question = question
    
    def get_task(self):
        
        ts = {
            
            'question document file': 'document-question-answering',
            'fill missing value': 'fill-mask',
            'classify label image':'image-classification',
            'generate caption image': 'image-to-text',
            'detect image':'object-detection',
            'context':'question-answering',
            'summarize':'summarization',
            'translate convert':'text2text-generation',
            'identify ner entities tokens prompt text':'token-classification',
            'image question answer':'visual-question-answering',
            'text sentiment classify label': 'zero-shot-classification'
        
        }
        
        model_list = {
            
            'document-question-answering': 'tiennvcs/layoutlmv2-base-uncased-finetuned-docvqa',
            'fill-mask': 'google/electra-small-generator',
            'image-classification':'apple/mobilevit-small',
            'image-to-text': 'Salesforce/blip-image-captioning-base',
            'OCR image text':'microsoft/trocr-small-printed',
            'object-detection':'hustvl/yolos-small',
            'question-answering':'mrm8488/bert-small-finetuned-squadv2',
            'summarization':'mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization',
            'text2text-generation':'google/t5-small-ssm',
            'token-classification':'dslim/bert-base-NER',
            'visual-question-answering':'microsoft/git-base-textvqa',
            'zero-shot-classification': 'cross-encoder/nli-deberta-v3-small'
        
        }
        
        zero_pipe = pipeline('zero-shot-classification', model="cross-encoder/nli-deberta-v3-small")
        prompt = self.prompt.split(':')[0]
        res = zero_pipe(prompt, list(ts.keys()))
        task_name = ts[res['labels'][0]]
        print("Identified as {} task".format(task_name))
        task = pipeline(task_name, model_list[task_name])
        
        return task, task_name
    
    def run_task(self, task_pipe, task_name, labels=['label1', 'label2']):
        
        self.task_pipe = task_pipe
        self.labels = labels
        self.task_name = task_name
        
        task_input = self.prompt.split(':')[-1]
        
        if self.task_name == "zero-shot-classification":
            task_output = self.task_pipe(task_input, self.labels)
            task_output = task_ou
        
        elif self.task_name in ["question-answering"]:
            QA ={
                "question":self.question,
                "context":task_input
            }
            task_output = self.task_pipe(QA)
            task_output = task_output[0]
        
        elif self.task_name in ['object-detection']:
            task_output = self.task_pipe(task_input)
            output = []
            for x in task_output:
                if x['label'] in self.prompt.split(':')[0]:
                    output.append(x)
            task_output = output
            
        else:
            task_output = self.task_pipe(task_input)
            task_output = task_output[0]

        return task_output
    
    def run_pipeline(self):
        
        task, task_name = self.get_task()
        result = self.run_task(task, task_name)
        
        return result
