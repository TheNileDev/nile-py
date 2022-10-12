from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.instance_event import InstanceEvent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    type: str,
    *,
    client: Client,
    seq: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/events/{type}".format(
        client.base_url, workspace=workspace, type=type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["seq"] = seq

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[InstanceEvent]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InstanceEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[InstanceEvent]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    type: str,
    *,
    client: Client,
    seq: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
) -> Response[List[InstanceEvent]]:
    """Get instance events

    Args:
        workspace (str):
        type (str):
        seq (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.

    Returns:
        Response[List[InstanceEvent]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        type=type,
        client=client,
        seq=seq,
        limit=limit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    type: str,
    *,
    client: Client,
    seq: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
) -> Optional[List[InstanceEvent]]:
    """Get instance events

    Args:
        workspace (str):
        type (str):
        seq (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.

    Returns:
        Response[List[InstanceEvent]]
    """

    return sync_detailed(
        workspace=workspace,
        type=type,
        client=client,
        seq=seq,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    type: str,
    *,
    client: Client,
    seq: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
) -> Response[List[InstanceEvent]]:
    """Get instance events

    Args:
        workspace (str):
        type (str):
        seq (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.

    Returns:
        Response[List[InstanceEvent]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        type=type,
        client=client,
        seq=seq,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    type: str,
    *,
    client: Client,
    seq: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 20,
) -> Optional[List[InstanceEvent]]:
    """Get instance events

    Args:
        workspace (str):
        type (str):
        seq (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 20.

    Returns:
        Response[List[InstanceEvent]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            type=type,
            client=client,
            seq=seq,
            limit=limit,
        )
    ).parsed
