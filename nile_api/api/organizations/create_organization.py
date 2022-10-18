from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.create_organization_request import CreateOrganizationRequest
from ...models.organization import Organization
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    json_body: CreateOrganizationRequest,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs".format(client.base_url, workspace=workspace)

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


def _parse_response(*, response: httpx.Response) -> Optional[Organization]:
    if response.status_code == 201:
        response_201 = Organization.from_dict(response.json())

        return response_201
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
    *,
    json_body: CreateOrganizationRequest,
    client: Client,
) -> Response[Organization]:
    """Create a new organization

    Args:
        workspace (str):

    Returns:
        Response[Organization]
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
    json_body: CreateOrganizationRequest,
    client: Client,
) -> Optional[Organization]:
    """Create a new organization

    Args:
        workspace (str):

    Returns:
        Response[Organization]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    json_body: CreateOrganizationRequest,
    client: Client,
) -> Response[Organization]:
    """Create a new organization

    Args:
        workspace (str):

    Returns:
        Response[Organization]
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
    json_body: CreateOrganizationRequest,
    client: Client,
) -> Optional[Organization]:
    """Create a new organization

    Args:
        workspace (str):

    Returns:
        Response[Organization]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
