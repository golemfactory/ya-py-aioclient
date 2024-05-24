from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.market_decoration import MarketDecoration
from golem_node_api_client.types import UNSET, Response


def _get_kwargs(
    *,
    allocation_ids: List[str],
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_allocation_ids = allocation_ids

    params['allocationIds'] = json_allocation_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/demandDecorations',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, MarketDecoration]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MarketDecoration.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
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
) -> Response[Union[ErrorMessage, MarketDecoration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    allocation_ids: List[str],
) -> Response[Union[ErrorMessage, MarketDecoration]]:
    """Obtain Demand elements specific to the given allocations, to be appended to a market Demand.

     Generate payment-related properties and constraints to be added to a demand published on the
    marketplace. As a parameter it accepts a list of IDs of allocations to be used to pay for invoices
    resulting from the decorated demand.

    Args:
        allocation_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, MarketDecoration]]
    """

    kwargs = _get_kwargs(
        allocation_ids=allocation_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    allocation_ids: List[str],
) -> Optional[Union[ErrorMessage, MarketDecoration]]:
    """Obtain Demand elements specific to the given allocations, to be appended to a market Demand.

     Generate payment-related properties and constraints to be added to a demand published on the
    marketplace. As a parameter it accepts a list of IDs of allocations to be used to pay for invoices
    resulting from the decorated demand.

    Args:
        allocation_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, MarketDecoration]
    """

    return sync_detailed(
        client=client,
        allocation_ids=allocation_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    allocation_ids: List[str],
) -> Response[Union[ErrorMessage, MarketDecoration]]:
    """Obtain Demand elements specific to the given allocations, to be appended to a market Demand.

     Generate payment-related properties and constraints to be added to a demand published on the
    marketplace. As a parameter it accepts a list of IDs of allocations to be used to pay for invoices
    resulting from the decorated demand.

    Args:
        allocation_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, MarketDecoration]]
    """

    kwargs = _get_kwargs(
        allocation_ids=allocation_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    allocation_ids: List[str],
) -> Optional[Union[ErrorMessage, MarketDecoration]]:
    """Obtain Demand elements specific to the given allocations, to be appended to a market Demand.

     Generate payment-related properties and constraints to be added to a demand published on the
    marketplace. As a parameter it accepts a list of IDs of allocations to be used to pay for invoices
    resulting from the decorated demand.

    Args:
        allocation_ids (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, MarketDecoration]
    """

    return (
        await asyncio_detailed(
            client=client,
            allocation_ids=allocation_ids,
        )
    ).parsed
