from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.event import Event
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    subscription_id: str,
    *,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['timeout'] = timeout

    params['maxEvents'] = max_events

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/market-api/v1/offers/{subscription_id}/events'.format(
            subscription_id=subscription_id,
        ),
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['Event']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Event.from_dict(response_200_item_data)

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
) -> Response[Union[ErrorMessage, List['Event']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Response[Union[ErrorMessage, List['Event']]]:
    r"""CollectDemands - Reads Market responses to published Offer.

     This is a blocking operation. It will not return until there is at least one new event.
    Returns Proposal related events:
    * `ProposalEvent` - Indicates that there is new Demand Proposal for this Offer.
    * `ProposalRejectedEvent` - Indicates that the Requestor has rejected
      our previous Proposal related to this Offer. This effectively ends a
      Negotiation chain - it explicitly indicates that the sender will not
      create another counter-Proposal.

    * `AgreementEvent` - Indicates that the Requestor is accepting our
      previous Proposal and ask for our approval of the Agreement.

    * `PropertyQueryEvent` - not supported yet.

    **Note**: When `collectDemands` is waiting, simultaneous call to `unsubscribeOffer` on the same
    `subscriptionId` should result in \"Subscription does not exist\" error returned from
    `collectDemands`.

    **Note**: Specification requires this endpoint to support list of specific Proposal Ids to listen
    for messages related only to specific Proposals. This is not covered yet.

    Args:
        subscription_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['Event']]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        timeout=timeout,
        max_events=max_events,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['Event']]]:
    r"""CollectDemands - Reads Market responses to published Offer.

     This is a blocking operation. It will not return until there is at least one new event.
    Returns Proposal related events:
    * `ProposalEvent` - Indicates that there is new Demand Proposal for this Offer.
    * `ProposalRejectedEvent` - Indicates that the Requestor has rejected
      our previous Proposal related to this Offer. This effectively ends a
      Negotiation chain - it explicitly indicates that the sender will not
      create another counter-Proposal.

    * `AgreementEvent` - Indicates that the Requestor is accepting our
      previous Proposal and ask for our approval of the Agreement.

    * `PropertyQueryEvent` - not supported yet.

    **Note**: When `collectDemands` is waiting, simultaneous call to `unsubscribeOffer` on the same
    `subscriptionId` should result in \"Subscription does not exist\" error returned from
    `collectDemands`.

    **Note**: Specification requires this endpoint to support list of specific Proposal Ids to listen
    for messages related only to specific Proposals. This is not covered yet.

    Args:
        subscription_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['Event']]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        timeout=timeout,
        max_events=max_events,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Response[Union[ErrorMessage, List['Event']]]:
    r"""CollectDemands - Reads Market responses to published Offer.

     This is a blocking operation. It will not return until there is at least one new event.
    Returns Proposal related events:
    * `ProposalEvent` - Indicates that there is new Demand Proposal for this Offer.
    * `ProposalRejectedEvent` - Indicates that the Requestor has rejected
      our previous Proposal related to this Offer. This effectively ends a
      Negotiation chain - it explicitly indicates that the sender will not
      create another counter-Proposal.

    * `AgreementEvent` - Indicates that the Requestor is accepting our
      previous Proposal and ask for our approval of the Agreement.

    * `PropertyQueryEvent` - not supported yet.

    **Note**: When `collectDemands` is waiting, simultaneous call to `unsubscribeOffer` on the same
    `subscriptionId` should result in \"Subscription does not exist\" error returned from
    `collectDemands`.

    **Note**: Specification requires this endpoint to support list of specific Proposal Ids to listen
    for messages related only to specific Proposals. This is not covered yet.

    Args:
        subscription_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['Event']]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        timeout=timeout,
        max_events=max_events,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
    max_events: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['Event']]]:
    r"""CollectDemands - Reads Market responses to published Offer.

     This is a blocking operation. It will not return until there is at least one new event.
    Returns Proposal related events:
    * `ProposalEvent` - Indicates that there is new Demand Proposal for this Offer.
    * `ProposalRejectedEvent` - Indicates that the Requestor has rejected
      our previous Proposal related to this Offer. This effectively ends a
      Negotiation chain - it explicitly indicates that the sender will not
      create another counter-Proposal.

    * `AgreementEvent` - Indicates that the Requestor is accepting our
      previous Proposal and ask for our approval of the Agreement.

    * `PropertyQueryEvent` - not supported yet.

    **Note**: When `collectDemands` is waiting, simultaneous call to `unsubscribeOffer` on the same
    `subscriptionId` should result in \"Subscription does not exist\" error returned from
    `collectDemands`.

    **Note**: Specification requires this endpoint to support list of specific Proposal Ids to listen
    for messages related only to specific Proposals. This is not covered yet.

    Args:
        subscription_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        max_events (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['Event']]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            timeout=timeout,
            max_events=max_events,
        )
    ).parsed
