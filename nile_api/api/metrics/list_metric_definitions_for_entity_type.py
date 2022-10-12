from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.list_metric_definitions_response import ListMetricDefinitionsResponse
from ...types import Response


def _get_kwargs(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/metrics/entities/{entity_type}/metric_definitions".format(
        client.base_url, workspace=workspace, entity_type=entity_type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[ListMetricDefinitionsResponse]:
    if response.status_code == 200:
        response_200 = ListMetricDefinitionsResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[ListMetricDefinitionsResponse]:
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
) -> Response[ListMetricDefinitionsResponse]:
    """List metrics for an entity

    Args:
        workspace (str):
        entity_type (str):

    Returns:
        Response[ListMetricDefinitionsResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        entity_type=entity_type,
        client=client,
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
) -> Optional[ListMetricDefinitionsResponse]:
    """List metrics for an entity

    Args:
        workspace (str):
        entity_type (str):

    Returns:
        Response[ListMetricDefinitionsResponse]
    """

    return sync_detailed(
        workspace=workspace,
        entity_type=entity_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
) -> Response[ListMetricDefinitionsResponse]:
    """List metrics for an entity

    Args:
        workspace (str):
        entity_type (str):

    Returns:
        Response[ListMetricDefinitionsResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        entity_type=entity_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    entity_type: str,
    *,
    client: Client,
) -> Optional[ListMetricDefinitionsResponse]:
    """List metrics for an entity

    Args:
        workspace (str):
        entity_type (str):

    Returns:
        Response[ListMetricDefinitionsResponse]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            entity_type=entity_type,
            client=client,
        )
    ).parsed
