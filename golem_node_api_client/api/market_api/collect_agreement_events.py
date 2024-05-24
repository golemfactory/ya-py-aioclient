import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.agreement_event import AgreementEvent
from golem_node_api_client.models.error_message import ErrorMessage
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
        'url': '/market-api/v1/agreementEvents',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['AgreementEvent']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AgreementEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorMessage, List['AgreementEvent']]]:
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
) -> Response[Union[ErrorMessage, List['AgreementEvent']]]:
    """CollectAgreementEvents - Collects events related to an Agreement.

     This is a blocking operation. It will not return until there is at least one new event. All events
    are appearing on both sides equally.

    Returns Agreement related events:
    * `AgreementApprovedEvent` - Indicates that the Agreement has been approved
      by the Provider.
      - The Provider is now ready to accept a request to start an Activity
        as described in the negotiated agreement.
      - The Providers’s corresponding `approveAgreement` call returns `Approved`
        after this event is emitted.

    * `AgreementRejectedEvent` - Indicates that the Provider has called
      `rejectAgreement`, which effectively stops the Agreement handshake.
      The Requestor may attempt to return to the Negotiation phase by sending
      a new Proposal.

    * `AgreementCancelledEvent` - Indicates that the Requestor has called
      `cancelAgreement`, which effectively stops the Agreement handshake.

    * `AgreementTerminatedEvent` - Indicates that the Agreement has been
      terminated by specified party (contains signature).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['AgreementEvent']]]
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
) -> Optional[Union[ErrorMessage, List['AgreementEvent']]]:
    """CollectAgreementEvents - Collects events related to an Agreement.

     This is a blocking operation. It will not return until there is at least one new event. All events
    are appearing on both sides equally.

    Returns Agreement related events:
    * `AgreementApprovedEvent` - Indicates that the Agreement has been approved
      by the Provider.
      - The Provider is now ready to accept a request to start an Activity
        as described in the negotiated agreement.
      - The Providers’s corresponding `approveAgreement` call returns `Approved`
        after this event is emitted.

    * `AgreementRejectedEvent` - Indicates that the Provider has called
      `rejectAgreement`, which effectively stops the Agreement handshake.
      The Requestor may attempt to return to the Negotiation phase by sending
      a new Proposal.

    * `AgreementCancelledEvent` - Indicates that the Requestor has called
      `cancelAgreement`, which effectively stops the Agreement handshake.

    * `AgreementTerminatedEvent` - Indicates that the Agreement has been
      terminated by specified party (contains signature).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['AgreementEvent']]
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
) -> Response[Union[ErrorMessage, List['AgreementEvent']]]:
    """CollectAgreementEvents - Collects events related to an Agreement.

     This is a blocking operation. It will not return until there is at least one new event. All events
    are appearing on both sides equally.

    Returns Agreement related events:
    * `AgreementApprovedEvent` - Indicates that the Agreement has been approved
      by the Provider.
      - The Provider is now ready to accept a request to start an Activity
        as described in the negotiated agreement.
      - The Providers’s corresponding `approveAgreement` call returns `Approved`
        after this event is emitted.

    * `AgreementRejectedEvent` - Indicates that the Provider has called
      `rejectAgreement`, which effectively stops the Agreement handshake.
      The Requestor may attempt to return to the Negotiation phase by sending
      a new Proposal.

    * `AgreementCancelledEvent` - Indicates that the Requestor has called
      `cancelAgreement`, which effectively stops the Agreement handshake.

    * `AgreementTerminatedEvent` - Indicates that the Agreement has been
      terminated by specified party (contains signature).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['AgreementEvent']]]
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
) -> Optional[Union[ErrorMessage, List['AgreementEvent']]]:
    """CollectAgreementEvents - Collects events related to an Agreement.

     This is a blocking operation. It will not return until there is at least one new event. All events
    are appearing on both sides equally.

    Returns Agreement related events:
    * `AgreementApprovedEvent` - Indicates that the Agreement has been approved
      by the Provider.
      - The Provider is now ready to accept a request to start an Activity
        as described in the negotiated agreement.
      - The Providers’s corresponding `approveAgreement` call returns `Approved`
        after this event is emitted.

    * `AgreementRejectedEvent` - Indicates that the Provider has called
      `rejectAgreement`, which effectively stops the Agreement handshake.
      The Requestor may attempt to return to the Negotiation phase by sending
      a new Proposal.

    * `AgreementCancelledEvent` - Indicates that the Requestor has called
      `cancelAgreement`, which effectively stops the Agreement handshake.

    * `AgreementTerminatedEvent` - Indicates that the Agreement has been
      terminated by specified party (contains signature).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        after_timestamp (Union[Unset, datetime.datetime]):
        max_events (Union[Unset, int]):  Default: 10.
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['AgreementEvent']]
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
