import nlpcloud

class myapp:
    def sentiment(self,text):

        client = nlpcloud.Client("finetuned-llama-3-70b", "86736d4cf356d8f6284fda36d682c2c03a7e1f63", gpu=True)
        response = client.sentiment(text,target="NLP Cloud")
        return response
    def language_detection(self,text):
        client = nlpcloud.Client("python-langdetect", "86736d4cf356d8f6284fda36d682c2c03a7e1f63", gpu=False)
        response = client.langdetection(text)
        return response
    def headline_generation(self,text):

        client = nlpcloud.Client("t5-base-en-generate-headline", "86736d4cf356d8f6284fda36d682c2c03a7e1f63", gpu=False)
        response = client.summarization(text)
        return response
    
