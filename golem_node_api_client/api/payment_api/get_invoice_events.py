import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.invoice_event import InvoiceEvent
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['timeout'] = timeout

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params['afterTimestamp'] = json_after_timestamp

    params['maxEvents'] = max_events

    params['appSessionId'] = app_session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/invoiceEvents',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['InvoiceEvent']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InvoiceEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorMessage, List['InvoiceEvent']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['InvoiceEvent']]]:
    """Get Invoice events.

     Listen for Invoice-related events using long-polling. If there are any events the method will return
    them immediately. If there are none the method will wait until one appears or timeout passes.
    `afterTimestamp` parameter can be used in order to get just the 'new' events. Setting the parameter
    value to the timestamp of the last processed event ensures that no events will go unnoticed.

    **NOTE:** The events are persistent, ie. calling the API does not remove the event records from
    receiving queue.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['InvoiceEvent']]]
    """

    kwargs = _get_kwargs(
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['InvoiceEvent']]]:
    """Get Invoice events.

     Listen for Invoice-related events using long-polling. If there are any events the method will return
    them immediately. If there are none the method will wait until one appears or timeout passes.
    `afterTimestamp` parameter can be used in order to get just the 'new' events. Setting the parameter
    value to the timestamp of the last processed event ensures that no events will go unnoticed.

    **NOTE:** The events are persistent, ie. calling the API does not remove the event records from
    receiving queue.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['InvoiceEvent']]
    """

    return sync_detailed(
        client=client,
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['InvoiceEvent']]]:
    """Get Invoice events.

     Listen for Invoice-related events using long-polling. If there are any events the method will return
    them immediately. If there are none the method will wait until one appears or timeout passes.
    `afterTimestamp` parameter can be used in order to get just the 'new' events. Setting the parameter
    value to the timestamp of the last processed event ensures that no events will go unnoticed.

    **NOTE:** The events are persistent, ie. calling the API does not remove the event records from
    receiving queue.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['InvoiceEvent']]]
    """

    kwargs = _get_kwargs(
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['InvoiceEvent']]]:
    """Get Invoice events.

     Listen for Invoice-related events using long-polling. If there are any events the method will return
    them immediately. If there are none the method will wait until one appears or timeout passes.
    `afterTimestamp` parameter can be used in order to get just the 'new' events. Setting the parameter
    value to the timestamp of the last processed event ensures that no events will go unnoticed.

    **NOTE:** The events are persistent, ie. calling the API does not remove the event records from
    receiving queue.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['InvoiceEvent']]
    """

    return (
        await asyncio_detailed(
            client=client,
            timeout=timeout,
            after_timestamp=after_timestamp,
            max_events=max_events,
            app_session_id=app_session_id,
        )
    ).parsed
