from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.create_user_request import CreateUserRequest
from ...models.user import User
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
    json_body: CreateUserRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/users".format(client.base_url, workspace=workspace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[User]:
    if response.status_code == 201:
        response_201 = User.from_dict(response.json())

        return response_201
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
    *,
    client: Client,
    json_body: CreateUserRequest,
) -> Response[User]:
    """Create a user

    Args:
        workspace (str):
        json_body (CreateUserRequest):

    Returns:
        Response[User]
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
    client: Client,
    json_body: CreateUserRequest,
) -> Optional[User]:
    """Create a user

    Args:
        workspace (str):
        json_body (CreateUserRequest):

    Returns:
        Response[User]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
    json_body: CreateUserRequest,
) -> Response[User]:
    """Create a user

    Args:
        workspace (str):
        json_body (CreateUserRequest):

    Returns:
        Response[User]
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
    client: Client,
    json_body: CreateUserRequest,
) -> Optional[User]:
    """Create a user

    Args:
        workspace (str):
        json_body (CreateUserRequest):

    Returns:
        Response[User]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
