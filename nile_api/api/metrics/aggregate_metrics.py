from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.aggregation_request import AggregationRequest
from ...models.aggregation_response import AggregationResponse
from ...types import Response


def _get_kwargs(
    workspace: str,
    metric_name: str,
    *,
    client: Client,
    json_body: AggregationRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/metrics/{metric_name}/aggregate".format(
        client.base_url, workspace=workspace, metric_name=metric_name
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


def _parse_response(*, response: httpx.Response) -> Optional[AggregationResponse]:
    if response.status_code == 200:
        response_200 = AggregationResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AggregationResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    metric_name: str,
    *,
    client: Client,
    json_body: AggregationRequest,
) -> Response[AggregationResponse]:
    """Aggregation result for the metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[AggregationResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        metric_name=metric_name,
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
    metric_name: str,
    *,
    client: Client,
    json_body: AggregationRequest,
) -> Optional[AggregationResponse]:
    """Aggregation result for the metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[AggregationResponse]
    """

    return sync_detailed(
        workspace=workspace,
        metric_name=metric_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    metric_name: str,
    *,
    client: Client,
    json_body: AggregationRequest,
) -> Response[AggregationResponse]:
    """Aggregation result for the metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[AggregationResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        metric_name=metric_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    metric_name: str,
    *,
    client: Client,
    json_body: AggregationRequest,
) -> Optional[AggregationResponse]:
    """Aggregation result for the metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[AggregationResponse]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            metric_name=metric_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
