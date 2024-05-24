import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.provider_event import ProviderEvent
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
) -> Optional[Union[ErrorMessage, List['ProviderEvent']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorMessage, List['ProviderEvent']]]:
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
) -> Response[Union[ErrorMessage, List['ProviderEvent']]]:
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
        Response[Union[ErrorMessage, List['ProviderEvent']]]
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


def sync(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['ProviderEvent']]]:
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
        Union[ErrorMessage, List['ProviderEvent']]
    """

    return sync_detailed(
        client=client,
        app_session_id=app_session_id,
        after_timestamp=after_timestamp,
        timeout=timeout,
        max_events=max_events,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Response[Union[ErrorMessage, List['ProviderEvent']]]:
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
        Response[Union[ErrorMessage, List['ProviderEvent']]]
    """

    kwargs = _get_kwargs(
        app_session_id=app_session_id,
        after_timestamp=after_timestamp,
        timeout=timeout,
        max_events=max_events,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['ProviderEvent']]]:
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
        Union[ErrorMessage, List['ProviderEvent']]
    """

    return (
        await asyncio_detailed(
            client=client,
            app_session_id=app_session_id,
            after_timestamp=after_timestamp,
            timeout=timeout,
            max_events=max_events,
        )
    ).parsed
