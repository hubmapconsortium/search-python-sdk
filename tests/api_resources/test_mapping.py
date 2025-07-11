# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_search_sdk import HubmapSearchSDK, AsyncHubmapSearchSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMapping:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_default(self, client: HubmapSearchSDK) -> None:
        mapping = client.mapping.retrieve_default()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_default(self, client: HubmapSearchSDK) -> None:
        response = client.mapping.with_raw_response.retrieve_default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = response.parse()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_default(self, client: HubmapSearchSDK) -> None:
        with client.mapping.with_streaming_response.retrieve_default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = response.parse()
            assert_matches_type(object, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_index(self, client: HubmapSearchSDK) -> None:
        mapping = client.mapping.retrieve_index(
            "index_name",
        )
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_index(self, client: HubmapSearchSDK) -> None:
        response = client.mapping.with_raw_response.retrieve_index(
            "index_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = response.parse()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_index(self, client: HubmapSearchSDK) -> None:
        with client.mapping.with_streaming_response.retrieve_index(
            "index_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = response.parse()
            assert_matches_type(object, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_index(self, client: HubmapSearchSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.mapping.with_raw_response.retrieve_index(
                "",
            )


class TestAsyncMapping:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_default(self, async_client: AsyncHubmapSearchSDK) -> None:
        mapping = await async_client.mapping.retrieve_default()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_default(self, async_client: AsyncHubmapSearchSDK) -> None:
        response = await async_client.mapping.with_raw_response.retrieve_default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = await response.parse()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_default(self, async_client: AsyncHubmapSearchSDK) -> None:
        async with async_client.mapping.with_streaming_response.retrieve_default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = await response.parse()
            assert_matches_type(object, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_index(self, async_client: AsyncHubmapSearchSDK) -> None:
        mapping = await async_client.mapping.retrieve_index(
            "index_name",
        )
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_index(self, async_client: AsyncHubmapSearchSDK) -> None:
        response = await async_client.mapping.with_raw_response.retrieve_index(
            "index_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mapping = await response.parse()
        assert_matches_type(object, mapping, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_index(self, async_client: AsyncHubmapSearchSDK) -> None:
        async with async_client.mapping.with_streaming_response.retrieve_index(
            "index_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mapping = await response.parse()
            assert_matches_type(object, mapping, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_index(self, async_client: AsyncHubmapSearchSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.mapping.with_raw_response.retrieve_index(
                "",
            )
