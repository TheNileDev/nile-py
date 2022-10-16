from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.login_info import LoginInfo
from ...models.error import Error
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    *,
    info: LoginInfo,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/auth/login".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": info.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Token]]:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Token]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    info: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a developer to nile

    Returns:
        Response[Union[Error, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        info=info,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    info: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a developer to nile

    Returns:
        Response[Union[Error, Token]]
    """

    return sync_detailed(
        client=client,
        info=info,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    info: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a developer to nile

    Returns:
        Response[Union[Error, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        info=info,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    info: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a developer to nile

    Returns:
        Response[Union[Error, Token]]
    """

    return (
        await asyncio_detailed(
            client=client,
            info=info,
        )
    ).parsed
