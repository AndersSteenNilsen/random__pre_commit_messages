## How to use:
Insert 
```yaml
  - repo: https://github.com/AndersSteenNilsen/random_pre_commit_messages
    rev: v0.1.0
    hooks:
      - id: random-git-messsage
```
into your `.pre-commit-config.yaml` and every time you want a random commit message just put *"random"* as your message. e.g: `commit -m "random"`

### The commit_message.txt
Stole list of commit messages from [commitment](https://github.com/ngerakines/commitment).
