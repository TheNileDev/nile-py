from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.update_user_request import UpdateUserRequest
from ...models.user import User
from ...types import Response


def _get_kwargs(
    workspace: str,
    id: str,
    *,
    client: Client,
    json_body: UpdateUserRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/users/{id}".format(
        client.base_url, workspace=workspace, id=id
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


def _parse_response(*, response: httpx.Response) -> Optional[User]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[User]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
    json_body: UpdateUserRequest,
) -> Response[User]:
    """Update a user

    Args:
        workspace (str):
        id (str):
        json_body (UpdateUserRequest):

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
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
    id: str,
    *,
    client: Client,
    json_body: UpdateUserRequest,
) -> Optional[User]:
    """Update a user

    Args:
        workspace (str):
        id (str):
        json_body (UpdateUserRequest):

    Returns:
        Response[User]
    """

    return sync_detailed(
        workspace=workspace,
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
    json_body: UpdateUserRequest,
) -> Response[User]:
    """Update a user

    Args:
        workspace (str):
        id (str):
        json_body (UpdateUserRequest):

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    id: str,
    *,
    client: Client,
    json_body: UpdateUserRequest,
) -> Optional[User]:
    """Update a user

    Args:
        workspace (str):
        id (str):
        json_body (UpdateUserRequest):

    Returns:
        Response[User]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
