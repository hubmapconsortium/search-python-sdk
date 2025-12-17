# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import add, mget, search, update, indices, mapping, reindex, clear_docs, param_search, scroll_search
    from .resources.add import AddResource, AsyncAddResource
    from .resources.mget import MgetResource, AsyncMgetResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.update import UpdateResource, AsyncUpdateResource
    from .resources.indices import IndicesResource, AsyncIndicesResource
    from .resources.mapping import MappingResource, AsyncMappingResource
    from .resources.reindex import ReindexResource, AsyncReindexResource
    from .resources.clear_docs import ClearDocsResource, AsyncClearDocsResource
    from .resources.param_search import ParamSearchResource, AsyncParamSearchResource
    from .resources.scroll_search import ScrollSearchResource, AsyncScrollSearchResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HubmapSearchSDK",
    "AsyncHubmapSearchSDK",
    "Client",
    "AsyncClient",
]


class HubmapSearchSDK(SyncAPIClient):
    # client options
    bearer_token: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous HubmapSearchSDK client instance."""
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("HUBMAP_SEARCH_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://search.api.hubmapconsortium.org/v3/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def indices(self) -> IndicesResource:
        from .resources.indices import IndicesResource

        return IndicesResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def param_search(self) -> ParamSearchResource:
        from .resources.param_search import ParamSearchResource

        return ParamSearchResource(self)

    @cached_property
    def reindex(self) -> ReindexResource:
        from .resources.reindex import ReindexResource

        return ReindexResource(self)

    @cached_property
    def mget(self) -> MgetResource:
        from .resources.mget import MgetResource

        return MgetResource(self)

    @cached_property
    def mapping(self) -> MappingResource:
        from .resources.mapping import MappingResource

        return MappingResource(self)

    @cached_property
    def update(self) -> UpdateResource:
        from .resources.update import UpdateResource

        return UpdateResource(self)

    @cached_property
    def add(self) -> AddResource:
        from .resources.add import AddResource

        return AddResource(self)

    @cached_property
    def clear_docs(self) -> ClearDocsResource:
        from .resources.clear_docs import ClearDocsResource

        return ClearDocsResource(self)

    @cached_property
    def scroll_search(self) -> ScrollSearchResource:
        from .resources.scroll_search import ScrollSearchResource

        return ScrollSearchResource(self)

    @cached_property
    def with_raw_response(self) -> HubmapSearchSDKWithRawResponse:
        return HubmapSearchSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubmapSearchSDKWithStreamedResponse:
        return HubmapSearchSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHubmapSearchSDK(AsyncAPIClient):
    # client options
    bearer_token: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHubmapSearchSDK client instance."""
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("HUBMAP_SEARCH_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://search.api.hubmapconsortium.org/v3/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def indices(self) -> AsyncIndicesResource:
        from .resources.indices import AsyncIndicesResource

        return AsyncIndicesResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def param_search(self) -> AsyncParamSearchResource:
        from .resources.param_search import AsyncParamSearchResource

        return AsyncParamSearchResource(self)

    @cached_property
    def reindex(self) -> AsyncReindexResource:
        from .resources.reindex import AsyncReindexResource

        return AsyncReindexResource(self)

    @cached_property
    def mget(self) -> AsyncMgetResource:
        from .resources.mget import AsyncMgetResource

        return AsyncMgetResource(self)

    @cached_property
    def mapping(self) -> AsyncMappingResource:
        from .resources.mapping import AsyncMappingResource

        return AsyncMappingResource(self)

    @cached_property
    def update(self) -> AsyncUpdateResource:
        from .resources.update import AsyncUpdateResource

        return AsyncUpdateResource(self)

    @cached_property
    def add(self) -> AsyncAddResource:
        from .resources.add import AsyncAddResource

        return AsyncAddResource(self)

    @cached_property
    def clear_docs(self) -> AsyncClearDocsResource:
        from .resources.clear_docs import AsyncClearDocsResource

        return AsyncClearDocsResource(self)

    @cached_property
    def scroll_search(self) -> AsyncScrollSearchResource:
        from .resources.scroll_search import AsyncScrollSearchResource

        return AsyncScrollSearchResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHubmapSearchSDKWithRawResponse:
        return AsyncHubmapSearchSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubmapSearchSDKWithStreamedResponse:
        return AsyncHubmapSearchSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HubmapSearchSDKWithRawResponse:
    _client: HubmapSearchSDK

    def __init__(self, client: HubmapSearchSDK) -> None:
        self._client = client

    @cached_property
    def indices(self) -> indices.IndicesResourceWithRawResponse:
        from .resources.indices import IndicesResourceWithRawResponse

        return IndicesResourceWithRawResponse(self._client.indices)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def param_search(self) -> param_search.ParamSearchResourceWithRawResponse:
        from .resources.param_search import ParamSearchResourceWithRawResponse

        return ParamSearchResourceWithRawResponse(self._client.param_search)

    @cached_property
    def reindex(self) -> reindex.ReindexResourceWithRawResponse:
        from .resources.reindex import ReindexResourceWithRawResponse

        return ReindexResourceWithRawResponse(self._client.reindex)

    @cached_property
    def mget(self) -> mget.MgetResourceWithRawResponse:
        from .resources.mget import MgetResourceWithRawResponse

        return MgetResourceWithRawResponse(self._client.mget)

    @cached_property
    def mapping(self) -> mapping.MappingResourceWithRawResponse:
        from .resources.mapping import MappingResourceWithRawResponse

        return MappingResourceWithRawResponse(self._client.mapping)

    @cached_property
    def update(self) -> update.UpdateResourceWithRawResponse:
        from .resources.update import UpdateResourceWithRawResponse

        return UpdateResourceWithRawResponse(self._client.update)

    @cached_property
    def add(self) -> add.AddResourceWithRawResponse:
        from .resources.add import AddResourceWithRawResponse

        return AddResourceWithRawResponse(self._client.add)

    @cached_property
    def clear_docs(self) -> clear_docs.ClearDocsResourceWithRawResponse:
        from .resources.clear_docs import ClearDocsResourceWithRawResponse

        return ClearDocsResourceWithRawResponse(self._client.clear_docs)

    @cached_property
    def scroll_search(self) -> scroll_search.ScrollSearchResourceWithRawResponse:
        from .resources.scroll_search import ScrollSearchResourceWithRawResponse

        return ScrollSearchResourceWithRawResponse(self._client.scroll_search)


class AsyncHubmapSearchSDKWithRawResponse:
    _client: AsyncHubmapSearchSDK

    def __init__(self, client: AsyncHubmapSearchSDK) -> None:
        self._client = client

    @cached_property
    def indices(self) -> indices.AsyncIndicesResourceWithRawResponse:
        from .resources.indices import AsyncIndicesResourceWithRawResponse

        return AsyncIndicesResourceWithRawResponse(self._client.indices)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def param_search(self) -> param_search.AsyncParamSearchResourceWithRawResponse:
        from .resources.param_search import AsyncParamSearchResourceWithRawResponse

        return AsyncParamSearchResourceWithRawResponse(self._client.param_search)

    @cached_property
    def reindex(self) -> reindex.AsyncReindexResourceWithRawResponse:
        from .resources.reindex import AsyncReindexResourceWithRawResponse

        return AsyncReindexResourceWithRawResponse(self._client.reindex)

    @cached_property
    def mget(self) -> mget.AsyncMgetResourceWithRawResponse:
        from .resources.mget import AsyncMgetResourceWithRawResponse

        return AsyncMgetResourceWithRawResponse(self._client.mget)

    @cached_property
    def mapping(self) -> mapping.AsyncMappingResourceWithRawResponse:
        from .resources.mapping import AsyncMappingResourceWithRawResponse

        return AsyncMappingResourceWithRawResponse(self._client.mapping)

    @cached_property
    def update(self) -> update.AsyncUpdateResourceWithRawResponse:
        from .resources.update import AsyncUpdateResourceWithRawResponse

        return AsyncUpdateResourceWithRawResponse(self._client.update)

    @cached_property
    def add(self) -> add.AsyncAddResourceWithRawResponse:
        from .resources.add import AsyncAddResourceWithRawResponse

        return AsyncAddResourceWithRawResponse(self._client.add)

    @cached_property
    def clear_docs(self) -> clear_docs.AsyncClearDocsResourceWithRawResponse:
        from .resources.clear_docs import AsyncClearDocsResourceWithRawResponse

        return AsyncClearDocsResourceWithRawResponse(self._client.clear_docs)

    @cached_property
    def scroll_search(self) -> scroll_search.AsyncScrollSearchResourceWithRawResponse:
        from .resources.scroll_search import AsyncScrollSearchResourceWithRawResponse

        return AsyncScrollSearchResourceWithRawResponse(self._client.scroll_search)


class HubmapSearchSDKWithStreamedResponse:
    _client: HubmapSearchSDK

    def __init__(self, client: HubmapSearchSDK) -> None:
        self._client = client

    @cached_property
    def indices(self) -> indices.IndicesResourceWithStreamingResponse:
        from .resources.indices import IndicesResourceWithStreamingResponse

        return IndicesResourceWithStreamingResponse(self._client.indices)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def param_search(self) -> param_search.ParamSearchResourceWithStreamingResponse:
        from .resources.param_search import ParamSearchResourceWithStreamingResponse

        return ParamSearchResourceWithStreamingResponse(self._client.param_search)

    @cached_property
    def reindex(self) -> reindex.ReindexResourceWithStreamingResponse:
        from .resources.reindex import ReindexResourceWithStreamingResponse

        return ReindexResourceWithStreamingResponse(self._client.reindex)

    @cached_property
    def mget(self) -> mget.MgetResourceWithStreamingResponse:
        from .resources.mget import MgetResourceWithStreamingResponse

        return MgetResourceWithStreamingResponse(self._client.mget)

    @cached_property
    def mapping(self) -> mapping.MappingResourceWithStreamingResponse:
        from .resources.mapping import MappingResourceWithStreamingResponse

        return MappingResourceWithStreamingResponse(self._client.mapping)

    @cached_property
    def update(self) -> update.UpdateResourceWithStreamingResponse:
        from .resources.update import UpdateResourceWithStreamingResponse

        return UpdateResourceWithStreamingResponse(self._client.update)

    @cached_property
    def add(self) -> add.AddResourceWithStreamingResponse:
        from .resources.add import AddResourceWithStreamingResponse

        return AddResourceWithStreamingResponse(self._client.add)

    @cached_property
    def clear_docs(self) -> clear_docs.ClearDocsResourceWithStreamingResponse:
        from .resources.clear_docs import ClearDocsResourceWithStreamingResponse

        return ClearDocsResourceWithStreamingResponse(self._client.clear_docs)

    @cached_property
    def scroll_search(self) -> scroll_search.ScrollSearchResourceWithStreamingResponse:
        from .resources.scroll_search import ScrollSearchResourceWithStreamingResponse

        return ScrollSearchResourceWithStreamingResponse(self._client.scroll_search)


class AsyncHubmapSearchSDKWithStreamedResponse:
    _client: AsyncHubmapSearchSDK

    def __init__(self, client: AsyncHubmapSearchSDK) -> None:
        self._client = client

    @cached_property
    def indices(self) -> indices.AsyncIndicesResourceWithStreamingResponse:
        from .resources.indices import AsyncIndicesResourceWithStreamingResponse

        return AsyncIndicesResourceWithStreamingResponse(self._client.indices)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def param_search(self) -> param_search.AsyncParamSearchResourceWithStreamingResponse:
        from .resources.param_search import AsyncParamSearchResourceWithStreamingResponse

        return AsyncParamSearchResourceWithStreamingResponse(self._client.param_search)

    @cached_property
    def reindex(self) -> reindex.AsyncReindexResourceWithStreamingResponse:
        from .resources.reindex import AsyncReindexResourceWithStreamingResponse

        return AsyncReindexResourceWithStreamingResponse(self._client.reindex)

    @cached_property
    def mget(self) -> mget.AsyncMgetResourceWithStreamingResponse:
        from .resources.mget import AsyncMgetResourceWithStreamingResponse

        return AsyncMgetResourceWithStreamingResponse(self._client.mget)

    @cached_property
    def mapping(self) -> mapping.AsyncMappingResourceWithStreamingResponse:
        from .resources.mapping import AsyncMappingResourceWithStreamingResponse

        return AsyncMappingResourceWithStreamingResponse(self._client.mapping)

    @cached_property
    def update(self) -> update.AsyncUpdateResourceWithStreamingResponse:
        from .resources.update import AsyncUpdateResourceWithStreamingResponse

        return AsyncUpdateResourceWithStreamingResponse(self._client.update)

    @cached_property
    def add(self) -> add.AsyncAddResourceWithStreamingResponse:
        from .resources.add import AsyncAddResourceWithStreamingResponse

        return AsyncAddResourceWithStreamingResponse(self._client.add)

    @cached_property
    def clear_docs(self) -> clear_docs.AsyncClearDocsResourceWithStreamingResponse:
        from .resources.clear_docs import AsyncClearDocsResourceWithStreamingResponse

        return AsyncClearDocsResourceWithStreamingResponse(self._client.clear_docs)

    @cached_property
    def scroll_search(self) -> scroll_search.AsyncScrollSearchResourceWithStreamingResponse:
        from .resources.scroll_search import AsyncScrollSearchResourceWithStreamingResponse

        return AsyncScrollSearchResourceWithStreamingResponse(self._client.scroll_search)


Client = HubmapSearchSDK

AsyncClient = AsyncHubmapSearchSDK
