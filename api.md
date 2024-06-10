# Models

Types:

```python
from lucere.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/lucere/resources/models.py">list</a>() -> <a href="./src/lucere/types/model_list_response.py">object</a></code>

# ChatCompletions

Types:

```python
from lucere.types import ChatCompletionCreateResponse, ChatCompletionTestResponse
```

Methods:

- <code title="post /chat/completions">client.chat_completions.<a href="./src/lucere/resources/chat_completions.py">create</a>() -> <a href="./src/lucere/types/chat_completion_create_response.py">object</a></code>
- <code title="post /chat/completions/test">client.chat_completions.<a href="./src/lucere/resources/chat_completions.py">test</a>() -> <a href="./src/lucere/types/chat_completion_test_response.py">object</a></code>
