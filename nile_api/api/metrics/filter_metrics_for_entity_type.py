from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.filter_ import Filter
from ...models.metric import Metric
from ...types import Response


def _get_kwargs(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
    json_body: Filter,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/metrics/entities/{entity_type}/filter".format(
        client.base_url, workspace=workspace, entity_type=entity_type
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


def _parse_response(*, response: httpx.Response) -> Optional[List[Metric]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Metric.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Metric]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
    json_body: Filter,
) -> Response[List[Metric]]:
    """List metrics for the entity matching the filter

    Args:
        workspace (str):
        entity_type (str):
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        entity_type=entity_type,
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
    entity_type: str,
    *,
    client: Client,
    json_body: Filter,
) -> Optional[List[Metric]]:
    """List metrics for the entity matching the filter

    Args:
        workspace (str):
        entity_type (str):
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    return sync_detailed(
        workspace=workspace,
        entity_type=entity_type,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
    json_body: Filter,
) -> Response[List[Metric]]:
    """List metrics for the entity matching the filter

    Args:
        workspace (str):
        entity_type (str):
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        entity_type=entity_type,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
    json_body: Filter,
) -> Optional[List[Metric]]:
    """List metrics for the entity matching the filter

    Args:
        workspace (str):
        entity_type (str):
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            entity_type=entity_type,
            client=client,
            json_body=json_body,
        )
    ).parsed
