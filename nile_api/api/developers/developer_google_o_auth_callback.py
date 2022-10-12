from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.developer_google_o_auth_response import DeveloperGoogleOAuthResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    code: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/auth/oauth/google/callback".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["code"] = code

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, DeveloperGoogleOAuthResponse]]:
    if response.status_code == 200:
        response_200 = DeveloperGoogleOAuthResponse.from_dict(response.json())

        return response_200
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, DeveloperGoogleOAuthResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    code: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DeveloperGoogleOAuthResponse]]:
    """Developer Google OAuth flow callback

     This endpoint is called automatically by Google after the user authenticates successfully.
    It's here for documentation purposes only, and it shouldn't be called directly.

    Args:
        code (Union[Unset, None, str]):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, DeveloperGoogleOAuthResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        code=code,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    code: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DeveloperGoogleOAuthResponse]]:
    """Developer Google OAuth flow callback

     This endpoint is called automatically by Google after the user authenticates successfully.
    It's here for documentation purposes only, and it shouldn't be called directly.

    Args:
        code (Union[Unset, None, str]):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, DeveloperGoogleOAuthResponse]]
    """

    return sync_detailed(
        client=client,
        code=code,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    code: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, DeveloperGoogleOAuthResponse]]:
    """Developer Google OAuth flow callback

     This endpoint is called automatically by Google after the user authenticates successfully.
    It's here for documentation purposes only, and it shouldn't be called directly.

    Args:
        code (Union[Unset, None, str]):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, DeveloperGoogleOAuthResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        code=code,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    code: Union[Unset, None, str] = UNSET,
    state: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, DeveloperGoogleOAuthResponse]]:
    """Developer Google OAuth flow callback

     This endpoint is called automatically by Google after the user authenticates successfully.
    It's here for documentation purposes only, and it shouldn't be called directly.

    Args:
        code (Union[Unset, None, str]):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, DeveloperGoogleOAuthResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            state=state,
        )
    ).parsed
