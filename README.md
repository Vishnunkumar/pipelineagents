# PipelineAgents

Replication of transfomers agents using huggingface pipelines

```bash
pip install -u pipelineagents
```

## Implementation

```python
agent = PipelineAgent("Classify the image:working/sample.jpg")
res = agent.run_pipeline()
```

## Results

**Input & Output**

<p float="left">
<img src="/bill7.png" width="350" height="600">
<img src="/output.png" width="350" height="600">
</p>

**Table**

- After saving to csv the result looks like the following

| LABEL | TEXT                               |
| ----- | ---------------------------------- |
| title | CREDIT CARD VOUCHER ANY RESTAURANT |
| title | ANYWHERE                           |
| key   | DATE:                              |
| value | 02/02/2014                         |
| key   | TIME:                              |
| value | 11:11                              |
| key   | CARD                               |
| key   | TYPE:                              |
| value | MC                                 |
| key   | ACCT:                              |
| value | XXXX XXXX XXXX                     |
| value | 1111                               |
| key   | TRANS                              |
| key   | KEY:                               |
| value | HYU8789798234                      |
| key   | AUTH                               |
| key   | CODE:                              |
| value | 12345                              |
| key   | EXP                                |
| key   | DATE:                              |
| value | XX/XX                              |
| key   | CHECK:                             |
| value | 1111                               |
| key   | TABLE:                             |
| value | 11/11                              |
| key   | SERVER:                            |
| value | 34                                 |
| value | MONIKA                             |
| key   | Subtotal:                          |
| value | $1969                              |
| value | .69                                |
| key   | Gratuity: Total:                   |

## Code credits

[@HuggingFace](https://huggingface.co/)

- Please note that this is still in development phase and will be improved in the near future
