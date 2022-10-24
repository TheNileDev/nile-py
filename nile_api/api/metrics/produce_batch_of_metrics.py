from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error import Error
from ...models.metric import Metric
from ...types import Response


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
    json_body: List[Metric],
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/metrics".format(
        client.base_url, workspace=workspace
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

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
) -> Optional[Union[Any, Error]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Error]]:
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
    json_body: List[Metric],
) -> Response[Union[Any, Error]]:
    """Produce a Batch of Metrics

    Args:
        workspace (str):
        json_body (List[Metric]):

    Returns:
        Response[Union[Any, Error]]
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
    json_body: List[Metric],
) -> Optional[Union[Any, Error]]:
    """Produce a Batch of Metrics

    Args:
        workspace (str):
        json_body (List[Metric]):

    Returns:
        Response[Union[Any, Error]]
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
    json_body: List[Metric],
) -> Response[Union[Any, Error]]:
    """Produce a Batch of Metrics

    Args:
        workspace (str):
        json_body (List[Metric]):

    Returns:
        Response[Union[Any, Error]]
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
    json_body: List[Metric],
) -> Optional[Union[Any, Error]]:
    """Produce a Batch of Metrics

    Args:
        workspace (str):
        json_body (List[Metric]):

    Returns:
        Response[Union[Any, Error]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
        )
    ).parsed
