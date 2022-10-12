from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/openapi".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, str]]:
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
) -> Response[Union[Error, str]]:
    """Get the OpenAPI specification for all events and entities in this workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, str]]
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
) -> Optional[Union[Error, str]]:
    """Get the OpenAPI specification for all events and entities in this workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, str]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
) -> Response[Union[Error, str]]:
    """Get the OpenAPI specification for all events and entities in this workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, str]]
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
) -> Optional[Union[Error, str]]:
    """Get the OpenAPI specification for all events and entities in this workspace

    Args:
        workspace (str):

    Returns:
        Response[Union[Error, str]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
        )
    ).parsed
