# Indices

Types:

```python
from hubmap_search_sdk.types import IndexListResponse
```

Methods:

- <code title="get /indices">client.indices.<a href="./src/hubmap_search_sdk/resources/indices.py">list</a>() -> <a href="./src/hubmap_search_sdk/types/index_list_response.py">IndexListResponse</a></code>

# Search

Types:

```python
from hubmap_search_sdk.types import SearchExecuteIndexQueryResponse, SearchExecuteQueryResponse
```

Methods:

- <code title="post /{index_name}/search">client.search.<a href="./src/hubmap_search_sdk/resources/search.py">execute_index_query</a>(index_name, \*\*<a href="src/hubmap_search_sdk/types/search_execute_index_query_params.py">params</a>) -> <a href="./src/hubmap_search_sdk/types/search_execute_index_query_response.py">object</a></code>
- <code title="post /search">client.search.<a href="./src/hubmap_search_sdk/resources/search.py">execute_query</a>(\*\*<a href="src/hubmap_search_sdk/types/search_execute_query_params.py">params</a>) -> <a href="./src/hubmap_search_sdk/types/search_execute_query_response.py">object</a></code>

# ParamSearch

Types:

```python
from hubmap_search_sdk.types import ParamSearchExecuteResponse
```

Methods:

- <code title="get /param-search/{entity_type}">client.param_search.<a href="./src/hubmap_search_sdk/resources/param_search.py">execute</a>(entity_type, \*\*<a href="src/hubmap_search_sdk/types/param_search_execute_params.py">params</a>) -> <a href="./src/hubmap_search_sdk/types/param_search_execute_response.py">object</a></code>

# Reindex

Methods:

- <code title="put /reindex/{identifier}">client.reindex.<a href="./src/hubmap_search_sdk/resources/reindex.py">update</a>(identifier) -> None</code>
