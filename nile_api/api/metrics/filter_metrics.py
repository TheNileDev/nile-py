import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.filter_ import Filter
from ...models.metric import Metric
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    *,
    client: Client,
    json_body: Filter,
    from_timestamp: Union[Unset, None, datetime.datetime] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/metrics/filter".format(
        client.base_url, workspace=workspace
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_from_timestamp: Union[Unset, None, str] = UNSET
    if not isinstance(from_timestamp, Unset):
        json_from_timestamp = from_timestamp.isoformat() if from_timestamp else None

    params["from_timestamp"] = json_from_timestamp

    params["duration"] = duration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
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
    *,
    client: Client,
    json_body: Filter,
    from_timestamp: Union[Unset, None, datetime.datetime] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
) -> Response[List[Metric]]:
    """List of metrics matching the filter

    Args:
        workspace (str):
        from_timestamp (Union[Unset, None, datetime.datetime]): The ISO-8601 formatted timestamp
            used to begin searching for matching metrics, i.e., 2018-11-13T20:20:39+00:00. If not
            provided the range will start from the epoch. Results returned are inclusive of this
            timestamp.
        duration (Union[Unset, None, int]): The duration (seconds) added to from_timestamp to
            limit the time range of the query. i.e., the query will be restricting to metric.timestamp
            >= from_timestamp AND metric.timestamp < from_timestamp + duration.  If not provided or
            the duration is <=0 then the end timestamp is set to now
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        json_body=json_body,
        from_timestamp=from_timestamp,
        duration=duration,
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
    json_body: Filter,
    from_timestamp: Union[Unset, None, datetime.datetime] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
) -> Optional[List[Metric]]:
    """List of metrics matching the filter

    Args:
        workspace (str):
        from_timestamp (Union[Unset, None, datetime.datetime]): The ISO-8601 formatted timestamp
            used to begin searching for matching metrics, i.e., 2018-11-13T20:20:39+00:00. If not
            provided the range will start from the epoch. Results returned are inclusive of this
            timestamp.
        duration (Union[Unset, None, int]): The duration (seconds) added to from_timestamp to
            limit the time range of the query. i.e., the query will be restricting to metric.timestamp
            >= from_timestamp AND metric.timestamp < from_timestamp + duration.  If not provided or
            the duration is <=0 then the end timestamp is set to now
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        json_body=json_body,
        from_timestamp=from_timestamp,
        duration=duration,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: Client,
    json_body: Filter,
    from_timestamp: Union[Unset, None, datetime.datetime] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
) -> Response[List[Metric]]:
    """List of metrics matching the filter

    Args:
        workspace (str):
        from_timestamp (Union[Unset, None, datetime.datetime]): The ISO-8601 formatted timestamp
            used to begin searching for matching metrics, i.e., 2018-11-13T20:20:39+00:00. If not
            provided the range will start from the epoch. Results returned are inclusive of this
            timestamp.
        duration (Union[Unset, None, int]): The duration (seconds) added to from_timestamp to
            limit the time range of the query. i.e., the query will be restricting to metric.timestamp
            >= from_timestamp AND metric.timestamp < from_timestamp + duration.  If not provided or
            the duration is <=0 then the end timestamp is set to now
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        client=client,
        json_body=json_body,
        from_timestamp=from_timestamp,
        duration=duration,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    *,
    client: Client,
    json_body: Filter,
    from_timestamp: Union[Unset, None, datetime.datetime] = UNSET,
    duration: Union[Unset, None, int] = UNSET,
) -> Optional[List[Metric]]:
    """List of metrics matching the filter

    Args:
        workspace (str):
        from_timestamp (Union[Unset, None, datetime.datetime]): The ISO-8601 formatted timestamp
            used to begin searching for matching metrics, i.e., 2018-11-13T20:20:39+00:00. If not
            provided the range will start from the epoch. Results returned are inclusive of this
            timestamp.
        duration (Union[Unset, None, int]): The duration (seconds) added to from_timestamp to
            limit the time range of the query. i.e., the query will be restricting to metric.timestamp
            >= from_timestamp AND metric.timestamp < from_timestamp + duration.  If not provided or
            the duration is <=0 then the end timestamp is set to now
        json_body (Filter):

    Returns:
        Response[List[Metric]]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            json_body=json_body,
            from_timestamp=from_timestamp,
            duration=duration,
        )
    ).parsed
