# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lucere import Lucere, AsyncLucere
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lucere) -> None:
        chat_completion = client.chat_completions.create()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lucere) -> None:
        response = client.chat_completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lucere) -> None:
        with client.chat_completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_test(self, client: Lucere) -> None:
        chat_completion = client.chat_completions.test()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_raw_response_test(self, client: Lucere) -> None:
        response = client.chat_completions.with_raw_response.test()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    def test_streaming_response_test(self, client: Lucere) -> None:
        with client.chat_completions.with_streaming_response.test() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChatCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLucere) -> None:
        chat_completion = await async_client.chat_completions.create()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLucere) -> None:
        response = await async_client.chat_completions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = await response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLucere) -> None:
        async with async_client.chat_completions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = await response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_test(self, async_client: AsyncLucere) -> None:
        chat_completion = await async_client.chat_completions.test()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_raw_response_test(self, async_client: AsyncLucere) -> None:
        response = await async_client.chat_completions.with_raw_response.test()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_completion = await response.parse()
        assert_matches_type(object, chat_completion, path=["response"])

    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncLucere) -> None:
        async with async_client.chat_completions.with_streaming_response.test() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_completion = await response.parse()
            assert_matches_type(object, chat_completion, path=["response"])

        assert cast(Any, response.is_closed) is True
