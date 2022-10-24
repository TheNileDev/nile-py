from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.access_token_info import AccessTokenInfo
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/access-tokens".format(
        client.base_url, workspace=workspace
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Error, List[AccessTokenInfo]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AccessTokenInfo.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Union[Error, List[AccessTokenInfo]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[Union[Error, List[AccessTokenInfo]]]:
    """List access tokens in a workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, List[AccessTokenInfo]]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    client: Client,
) -> Optional[Union[Error, List[AccessTokenInfo]]]:
    """List access tokens in a workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, List[AccessTokenInfo]]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[Union[Error, List[AccessTokenInfo]]]:
    """List access tokens in a workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, List[AccessTokenInfo]]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: Client,
) -> Optional[Union[Error, List[AccessTokenInfo]]]:
    """List access tokens in a workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, List[AccessTokenInfo]]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
