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

## Results
