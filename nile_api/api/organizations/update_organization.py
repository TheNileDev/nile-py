from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.organization import Organization
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}".format(
        client.base_url, workspace=workspace, org=org
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


def _parse_response(*, response: httpx.Response) -> Optional[Organization]:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Organization]:
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
) -> Response[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[Organization]
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
) -> Optional[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[Organization]
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
) -> Response[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[Organization]
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
) -> Optional[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):

    Returns:
        Response[Organization]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            client=client,
        )
    ).parsed
