from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.entity import Entity
from ...types import Response


def _get_kwargs(
    workspace: str,
    type: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/entities/{type}".format(
        client.base_url, workspace=workspace, type=type
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


def _parse_response(*, response: httpx.Response) -> Optional[Entity]:
    if response.status_code == 200:
        response_200 = Entity.from_dict(response.json())

        return response_200

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise Exception(f"Unexpected status code: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Entity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    type: str,
    *,
    client: Client,
) -> Response[Entity]:
    """Get an entity

    Args:
        workspace (str):
        type (str):

    Returns:
        Response[Entity]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        type=type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    type: str,
    *,
    client: Client,
) -> Optional[Entity]:
    """Get an entity

    Args:
        workspace (str):
        type (str):

    Returns:
        Response[Entity]
    """

    return sync_detailed(
        workspace=workspace,
        type=type,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    type: str,
    *,
    client: Client,
) -> Response[Entity]:
    """Get an entity

    Args:
        workspace (str):
        type (str):

    Returns:
        Response[Entity]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        type=type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    type: str,
    *,
    client: Client,
) -> Optional[Entity]:
    """Get an entity

    Args:
        workspace (str):
        type (str):

    Returns:
        Response[Entity]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            type=type,
            client=client,
        )
    ).parsed
