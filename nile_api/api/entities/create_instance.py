from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.error import Error
from ...models.instance import Instance
from ...models.json_schema_instance import JsonSchemaInstance
from ...types import Response


def _get_kwargs(
    workspace: str,
    org: str,
    type: str,
    *,
    client: Client,
    json_body: JsonSchemaInstance,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspace}/orgs/{org}/instances/{type}".format(
        client.base_url, workspace=workspace, org=org, type=type
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


def _parse_response(*, response: httpx.Response) -> Optional[Instance]:
    if response.status_code == 201:
        response_201 = Instance.from_dict(response.json())

        return response_201

    # Nile has a known format for 40X errors, so regardless of the spec, lets return a Nile error
    # Note that the type hint may or may not include Error type
    if response.status_code >= 400 and response.status_code < 500:
        return Error.from_dict(response.json())

    # If it isn't 20X and isn't 40X, we don't know what to do.
    # This is a hard-coded version of https://github.com/openapi-generators/openapi-python-client/pull/593
    raise RuntimeError(f"Unexpected status code: {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Instance]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    org: str,
    type: str,
    *,
    client: Client,
    json_body: JsonSchemaInstance,
) -> Response[Instance]:
    """Create a new instance

    Args:
        workspace (str):
        org (str):
        type (str):
        json_body (JsonSchemaInstance): An *instance* of a JSON Schema Example: {'id': 'lkc-123',
            'memory': 4096, 'cpus': 4}.

    Returns:
        Response[Instance]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        type=type,
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
    org: str,
    type: str,
    *,
    client: Client,
    json_body: JsonSchemaInstance,
) -> Optional[Instance]:
    """Create a new instance

    Args:
        workspace (str):
        org (str):
        type (str):
        json_body (JsonSchemaInstance): An *instance* of a JSON Schema Example: {'id': 'lkc-123',
            'memory': 4096, 'cpus': 4}.

    Returns:
        Response[Instance]
    """

    return sync_detailed(
        workspace=workspace,
        org=org,
        type=type,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    org: str,
    type: str,
    *,
    client: Client,
    json_body: JsonSchemaInstance,
) -> Response[Instance]:
    """Create a new instance

    Args:
        workspace (str):
        org (str):
        type (str):
        json_body (JsonSchemaInstance): An *instance* of a JSON Schema Example: {'id': 'lkc-123',
            'memory': 4096, 'cpus': 4}.

    Returns:
        Response[Instance]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        org=org,
        type=type,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    org: str,
    type: str,
    *,
    client: Client,
    json_body: JsonSchemaInstance,
) -> Optional[Instance]:
    """Create a new instance

    Args:
        workspace (str):
        org (str):
        type (str):
        json_body (JsonSchemaInstance): An *instance* of a JSON Schema Example: {'id': 'lkc-123',
            'memory': 4096, 'cpus': 4}.

    Returns:
        Response[Instance]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            org=org,
            type=type,
            client=client,
            json_body=json_body,
        )
    ).parsed
