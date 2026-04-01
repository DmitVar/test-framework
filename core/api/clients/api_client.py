from typing import Any

import allure
from httpx import Client, QueryParams, Response, URL

from httpx._types import RequestData, RequestFiles, RequestContent


class APIClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> Response:
        """
        Make GET request
        :param headers: Headers
        :param url: URL - address endpoint
        :param params: GET - request parameters
        :return: Response object
        """
        return self.client.get(url, params=params, headers=headers, **kwargs)

    @allure.step("Make POST request to {url}")
    def post(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        content: RequestContent | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        """
        Make POST request
        :param url: URL - address endpoint
        :param json: Data in JSON formate
        :param data: Formatted form data
        :param files: Files to upload to the server
        :param content: Raw byte transfers
        :param headers: Passing custom headers
        :return: Response object
        """
        return self.client.post(
            url, json=json, data=data, files=files, content=content, headers=headers
        )

    @allure.step("Make PUT request to {url}")
    def put(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        content: RequestContent | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        """
        Make PUT request
        :param url: URL - address endpoint
        :param json: Data in JSON formate
        :param data: Formatted form data
        :param files: Files to upload to the server
        :param content: Raw byte transfers
        :param headers: Passing custom headers
        :return: Response object
        """
        return self.client.put(
            url, json=json, data=data, files=files, content=content, headers=headers
        )

    @allure.step("Make PATCH request to {url}")
    def patch(
        self,
        url: URL | str,
        json: Any | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        content: RequestContent | None = None,
        headers: dict[str, str] | None = None,
    ):
        """
        Make PATCH request
        :param url: URL - address endpoint
        :param json: Data in JSON formate
        :param data: Formatted form data
        :param files: Files to upload to the server
        :param content: Raw byte transfers
        :param headers: Passing custom headers
        :return: Response object
        """
        return self.client.patch(
            url, json=json, data=data, files=files, content=content, headers=headers
        )

    @allure.step("Make DELETE request to {url}")
    def delete(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> Response:
        """
        Make DELETE request
        :param url: URL - address endpoint
        :param params: DELETE - request parameters
        :return: Response object
        """
        return self.client.delete(url, params=params, headers=headers, **kwargs)
