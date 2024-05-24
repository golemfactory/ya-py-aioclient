import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.payment import Payment
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['timeout'] = timeout

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params['afterTimestamp'] = json_after_timestamp

    params['maxEvents'] = max_events

    params['appSessionId'] = app_session_id

    params['network'] = network

    params['driver'] = driver

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/payments',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['Payment']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Payment.from_dict(response_200_item_data)

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
) -> Response[Union[ErrorMessage, List['Payment']]]:
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
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['Payment']]]:
    """Get Payments.

     Payments can be treated as events and this method can be used to listen for new payments by long-
    polling.  If there are any payments the method will return them immediately. If there are none the
    method will wait until one appears or timeout passes. `afterTimestamp` parameter can be used in
    order to get just the 'new' payments. Setting the parameter value to the timestamp of the last
    processed payment ensures that no payments will go unnoticed. `network` and `driver` parameters can
    be used in order to filter payments.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['Payment']]]
    """

    kwargs = _get_kwargs(
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
        network=network,
        driver=driver,
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
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['Payment']]]:
    """Get Payments.

     Payments can be treated as events and this method can be used to listen for new payments by long-
    polling.  If there are any payments the method will return them immediately. If there are none the
    method will wait until one appears or timeout passes. `afterTimestamp` parameter can be used in
    order to get just the 'new' payments. Setting the parameter value to the timestamp of the last
    processed payment ensures that no payments will go unnoticed. `network` and `driver` parameters can
    be used in order to filter payments.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['Payment']]
    """

    return sync_detailed(
        client=client,
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
        network=network,
        driver=driver,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_events: Union[Unset, int] = 10,
    app_session_id: Union[Unset, str] = UNSET,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['Payment']]]:
    """Get Payments.

     Payments can be treated as events and this method can be used to listen for new payments by long-
    polling.  If there are any payments the method will return them immediately. If there are none the
    method will wait until one appears or timeout passes. `afterTimestamp` parameter can be used in
    order to get just the 'new' payments. Setting the parameter value to the timestamp of the last
    processed payment ensures that no payments will go unnoticed. `network` and `driver` parameters can
    be used in order to filter payments.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['Payment']]]
    """

    kwargs = _get_kwargs(
        timeout=timeout,
        after_timestamp=after_timestamp,
        max_events=max_events,
        app_session_id=app_session_id,
        network=network,
        driver=driver,
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
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['Payment']]]:
    """Get Payments.

     Payments can be treated as events and this method can be used to listen for new payments by long-
    polling.  If there are any payments the method will return them immediately. If there are none the
    method will wait until one appears or timeout passes. `afterTimestamp` parameter can be used in
    order to get just the 'new' payments. Setting the parameter value to the timestamp of the last
    processed payment ensures that no payments will go unnoticed. `network` and `driver` parameters can
    be used in order to filter payments.

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['Payment']]
    """

    return (
        await asyncio_detailed(
            client=client,
            timeout=timeout,
            after_timestamp=after_timestamp,
            max_events=max_events,
            app_session_id=app_session_id,
            network=network,
            driver=driver,
        )
    ).parsed
