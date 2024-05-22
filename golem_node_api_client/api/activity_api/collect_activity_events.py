import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['appSessionId'] = app_session_id

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params['afterTimestamp'] = json_after_timestamp

    params['timeout'] = timeout

    params['maxEvents'] = max_events

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/activity-api/v1/events',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Response[Any]:
    """Fetch Requestor command events.

    Args:
        app_session_id (Union[Unset, str]):
        after_timestamp (Union[Unset, datetime.datetime]):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_session_id=app_session_id,
        after_timestamp=after_timestamp,
        timeout=timeout,
        max_events=max_events,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Response[Any]:
    """Fetch Requestor command events.

    Args:
        app_session_id (Union[Unset, str]):
        after_timestamp (Union[Unset, datetime.datetime]):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_session_id=app_session_id,
        after_timestamp=after_timestamp,
        timeout=timeout,
        max_events=max_events,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
