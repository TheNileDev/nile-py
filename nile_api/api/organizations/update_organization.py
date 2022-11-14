from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.error import Error
from ...models.organization import Organization
from ...models.update_organization_request import UpdateOrganizationRequest
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    *,
    client: Client,
    json_body: UpdateOrganizationRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}".format(
        client.base_url, workspace=workspace, org=org
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Organization]:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

        return response_200

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise RuntimeError(f"Unexpected status code: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Organization]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    org: str,
    *,
    client: Client,
    json_body: UpdateOrganizationRequest,
) -> Response[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):
        json_body (UpdateOrganizationRequest):

    Returns:
        Response[Organization]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
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
    org: str,
    *,
    client: Client,
    json_body: UpdateOrganizationRequest,
) -> Optional[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):
        json_body (UpdateOrganizationRequest):

    Returns:
        Response[Organization]
    """

    return sync_detailed(
        workspace=workspace,
        org=org,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    org: str,
    *,
    client: Client,
    json_body: UpdateOrganizationRequest,
) -> Response[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):
        json_body (UpdateOrganizationRequest):

    Returns:
        Response[Organization]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    org: str,
    *,
    client: Client,
    json_body: UpdateOrganizationRequest,
) -> Optional[Organization]:
    """Update an organization

    Args:
        workspace (str):
        org (str):
        json_body (UpdateOrganizationRequest):

    Returns:
        Response[Organization]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            client=client,
            json_body=json_body,
        )
    ).parsed
