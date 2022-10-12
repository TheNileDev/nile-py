from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.policy import Policy
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}/access/policies".format(
        client.base_url, workspace=workspace, org=org
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


def _parse_response(*, response: httpx.Response) -> Optional[List[Policy]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Policy.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Policy]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    org: str,
    *,
    client: Client,
) -> Response[List[Policy]]:
    """List all access policies

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[List[Policy]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
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
    *,
    client: Client,
) -> Optional[List[Policy]]:
    """List all access policies

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[List[Policy]]
    """

    return sync_detailed(
        workspace=workspace,
        org=org,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    org: str,
    *,
    client: Client,
) -> Response[List[Policy]]:
    """List all access policies

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[List[Policy]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    org: str,
    *,
    client: Client,
) -> Optional[List[Policy]]:
    """List all access policies

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[List[Policy]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            client=client,
        )
    ).parsed
