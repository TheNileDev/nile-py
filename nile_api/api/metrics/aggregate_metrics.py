from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.aggregation_request import AggregationRequest
from ...models.bucket import Bucket
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


def _parse_response(*, response: httpx.Response) -> Optional[List[Bucket]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Bucket.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise Exception(f"Unexpected status code: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[List[Bucket]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
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
) -> Response[List[Bucket]]:
    """Perform sum, min, max, avg, and percentile aggregations over a metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[List[Bucket]]
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
) -> Optional[List[Bucket]]:
    """Perform sum, min, max, avg, and percentile aggregations over a metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[List[Bucket]]
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
) -> Response[List[Bucket]]:
    """Perform sum, min, max, avg, and percentile aggregations over a metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[List[Bucket]]
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
) -> Optional[List[Bucket]]:
    """Perform sum, min, max, avg, and percentile aggregations over a metric

    Args:
        workspace (str):
        metric_name (str):
        json_body (AggregationRequest):

    Returns:
        Response[List[Bucket]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            metric_name=metric_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
