from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.login_info import LoginInfo
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: LoginInfo,
) -> Dict[str, Any]:
    url = "{}/auth/login".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Error, Token]]:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise Exception(f"Unexpected status code: {response.status_code}")


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Error, Token]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a developer to nile

    Args:
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a developer to nile

    Args:
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a developer to nile

    Args:
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a developer to nile

    Args:
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
