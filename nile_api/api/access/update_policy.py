from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.policy import Policy
from ...models.update_policy_request import UpdatePolicyRequest
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    policy_id: str,
    *,
    client: Client,
    json_body: UpdatePolicyRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}/access/policies/{policyId}".format(
        client.base_url, workspace=workspace, org=org, policyId=policy_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Policy]:
    if response.status_code == 200:
        response_200 = Policy.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Policy]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    org: str,
    policy_id: str,
    *,
    client: Client,
    json_body: UpdatePolicyRequest,
) -> Response[Policy]:
    """Update an access policy

    Args:
        workspace (str):
        org (str):
        policy_id (str):
        json_body (UpdatePolicyRequest):

    Returns:
        Response[Policy]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        policy_id=policy_id,
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
    policy_id: str,
    *,
    client: Client,
    json_body: UpdatePolicyRequest,
) -> Optional[Policy]:
    """Update an access policy

    Args:
        workspace (str):
        org (str):
        policy_id (str):
        json_body (UpdatePolicyRequest):

    Returns:
        Response[Policy]
    """

    return sync_detailed(
        workspace=workspace,
        org=org,
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    org: str,
    policy_id: str,
    *,
    client: Client,
    json_body: UpdatePolicyRequest,
) -> Response[Policy]:
    """Update an access policy

    Args:
        workspace (str):
        org (str):
        policy_id (str):
        json_body (UpdatePolicyRequest):

    Returns:
        Response[Policy]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    org: str,
    policy_id: str,
    *,
    client: Client,
    json_body: UpdatePolicyRequest,
) -> Optional[Policy]:
    """Update an access policy

    Args:
        workspace (str):
        org (str):
        policy_id (str):
        json_body (UpdatePolicyRequest):

    Returns:
        Response[Policy]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
