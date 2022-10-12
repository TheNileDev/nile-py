from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.instance import Instance
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    type: str,
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}/instances/{type}/{id}".format(
        client.base_url, workspace=workspace, org=org, type=type, id=id
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


def _parse_response(*, response: httpx.Response) -> Optional[Instance]:
    if response.status_code == 200:
        response_200 = Instance.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Instance]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    org: str,
    type: str,
    id: str,
    *,
    client: Client,
) -> Response[Instance]:
    """Get an instance

    Args:
        workspace (str):
        org (str):
        type (str):
        id (str):

    Returns:
        Response[Instance]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        type=type,
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
    org: str,
    type: str,
    id: str,
    *,
    client: Client,
) -> Optional[Instance]:
    """Get an instance

    Args:
        workspace (str):
        org (str):
        type (str):
        id (str):

    Returns:
        Response[Instance]
    """

    return sync_detailed(
        workspace=workspace,
        org=org,
        type=type,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    org: str,
    type: str,
    id: str,
    *,
    client: Client,
) -> Response[Instance]:
    """Get an instance

    Args:
        workspace (str):
        org (str):
        type (str):
        id (str):

    Returns:
        Response[Instance]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        type=type,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    org: str,
    type: str,
    id: str,
    *,
    client: Client,
) -> Optional[Instance]:
    """Get an instance

    Args:
        workspace (str):
        org (str):
        type (str):
        id (str):

    Returns:
        Response[Instance]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            type=type,
            id=id,
            client=client,
        )
    ).parsed
