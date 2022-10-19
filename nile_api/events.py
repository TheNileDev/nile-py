"""
Support for the nile events API.

This file is not automatically generated from the OpenAPI spec.
"""

import asyncio

from nile_api.client import Client
from nile_api.api.entities import instance_events


async def on(
    *,
    client: Client,
    workspace: str,
    type: str,
    seq: int,
    refresh=5000,
):
    while True:
        events = await instance_events.asyncio(
            client=client,
            type=type,
            workspace=workspace,
            seq=seq,
        )
        for event in events:
            yield event
            seq = event.after.seq
        await asyncio.sleep(refresh)
