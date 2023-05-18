# PipelineAgents

Replication of transfomers agents using huggingface pipelines

```bash
pip install -u pipelineagents
```

## Implementation

```python
# task:path, question
# Image Classification example
agent = PipelineAgent("Classify the image:working/sample.jpg")
res = agent.run_pipeline()
```

## Note
- document-question-answering: Please have detectron installed to make use of this, sample input = PipelineAgent("In the document:image_path", "question")
- fill-mask: sample input = PipelineAgent("fill the missing value:text [MASK] text")
- image-classification: sample input = PipelineAgent("Classify the image:image_path")
- image-to-text: sample input = PipelineAgent("Generate caption for the image:image_path")
- object-detection: sample input = PipelineAgent("Detect [object] in the image:image_path")
- question-answering: sample imput = PipelineAgent("Context: text", "question")
- summarization: sample imput = PipelineAgent("Summarize: text")
- text2text-generation: 
- token-classification: sample imput = PipelineAgent("Identify the entities: text")
- visual-question-answering: sample imput = PipelineAgent("In the image: image_path", "question")
- zero-shot-classification: sample imput = PipelineAgent("Classify the text: text", ["label1", "label2"])
