from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.create_access_token_request import CreateAccessTokenRequest
from ...models.create_access_token_response import CreateAccessTokenResponse
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
    json_body: CreateAccessTokenRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/access_tokens".format(
        client.base_url, workspace=workspace
    )

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[CreateAccessTokenResponse]:
    if response.status_code == 201:
        response_201 = CreateAccessTokenResponse.from_dict(response.json())

        return response_201

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise Exception(f"Unexpected status code: {response.status_code}")


def _build_response(
    *, response: httpx.Response
) -> Response[CreateAccessTokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: Client,
    json_body: CreateAccessTokenRequest,
) -> Response[CreateAccessTokenResponse]:
    """Create an access token

     Create a workspace token. Workspace tokens have authorization to perform most actions within a
    workspace.

    Args:
        workspace (str):
        json_body (CreateAccessTokenRequest):

    Returns:
        Response[CreateAccessTokenResponse]
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
    json_body: CreateAccessTokenRequest,
) -> Optional[CreateAccessTokenResponse]:
    """Create an access token

     Create a workspace token. Workspace tokens have authorization to perform most actions within a
    workspace.

    Args:
        workspace (str):
        json_body (CreateAccessTokenRequest):

    Returns:
        Response[CreateAccessTokenResponse]
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
    json_body: CreateAccessTokenRequest,
) -> Response[CreateAccessTokenResponse]:
    """Create an access token

     Create a workspace token. Workspace tokens have authorization to perform most actions within a
    workspace.

    Args:
        workspace (str):
        json_body (CreateAccessTokenRequest):

    Returns:
        Response[CreateAccessTokenResponse]
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
    json_body: CreateAccessTokenRequest,
) -> Optional[CreateAccessTokenResponse]:
    """Create an access token

     Create a workspace token. Workspace tokens have authorization to perform most actions within a
    workspace.

    Args:
        workspace (str):
        json_body (CreateAccessTokenRequest):

    Returns:
        Response[CreateAccessTokenResponse]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
