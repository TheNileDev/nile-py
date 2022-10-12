from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.login_info import LoginInfo
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
    json_body: LoginInfo,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/auth/login".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, Token]]:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Token]]:
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
    json_body: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a user

     Login a user to Nile. This operation returns a JWT token. Most Nile operations require
    authentication and expect this token in the 'Authorization: Bearer <token>' header

    Args:
        workspace (str):
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
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
    json_body: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a user

     Login a user to Nile. This operation returns a JWT token. Most Nile operations require
    authentication and expect this token in the 'Authorization: Bearer <token>' header

    Args:
        workspace (str):
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
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
    json_body: LoginInfo,
) -> Response[Union[Error, Token]]:
    """Log in a user

     Login a user to Nile. This operation returns a JWT token. Most Nile operations require
    authentication and expect this token in the 'Authorization: Bearer <token>' header

    Args:
        workspace (str):
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
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
    json_body: LoginInfo,
) -> Optional[Union[Error, Token]]:
    """Log in a user

     Login a user to Nile. This operation returns a JWT token. Most Nile operations require
    authentication and expect this token in the 'Authorization: Bearer <token>' header

    Args:
        workspace (str):
        json_body (LoginInfo):

    Returns:
        Response[Union[Error, Token]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
