from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.entity import Entity
from ...models.create_entity_request import CreateEntityRequest
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    json_body: CreateEntityRequest,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/entities".format(
        client.base_url, workspace=workspace
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_body.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Entity]:
    if response.status_code == 200:
        response_200 = Entity.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Entity]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    json_body: CreateEntityRequest,
    client: Client,
) -> Response[Entity]:
    """Create Entity

    Args:
        workspace (str):

    Returns:
        Response[Entity]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    *,
    json_body: CreateEntityRequest,
    client: Client,
) -> Optional[Entity]:
    """Create Entity

    Args:
        workspace (str):

    Returns:
        Response[Entity]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    json_body: CreateEntityRequest,
    client: Client,
) -> Response[Entity]:
    """Create Entity

    Args:
        workspace (str):

    Returns:
        Response[Entity]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    json_body: CreateEntityRequest,
    client: Client,
) -> Optional[Entity]:
    """Create Entity

    Args:
        workspace (str):

    Returns:
        Response[Entity]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
