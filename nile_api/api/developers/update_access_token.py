from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.access_token_info import AccessTokenInfo
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/access-tokens/{id}".format(
        client.base_url, workspace=workspace, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AccessTokenInfo, Error]]:
    if response.status_code == 200:
        response_200 = AccessTokenInfo.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AccessTokenInfo, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Response[Union[AccessTokenInfo, Error]]:
    """Update an access token

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[Union[AccessTokenInfo, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Optional[Union[AccessTokenInfo, Error]]:
    """Update an access token

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[Union[AccessTokenInfo, Error]]
    """

    return sync_detailed(
        workspace=workspace,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Response[Union[AccessTokenInfo, Error]]:
    """Update an access token

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[Union[AccessTokenInfo, Error]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Optional[Union[AccessTokenInfo, Error]]:
    """Update an access token

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[Union[AccessTokenInfo, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            id=id,
            client=client,
        )
    ).parsed
