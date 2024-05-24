import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.allocation import Allocation
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Allocation,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params['afterTimestamp'] = json_after_timestamp

    params['maxItems'] = max_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/payment-api/v1/allocations',
        'params': params,
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Allocation, ErrorMessage]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Allocation.from_dict(response.json())

        return response_201
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
) -> Response[Union[Allocation, ErrorMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Allocation,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Union[Allocation, ErrorMessage]]:
    """Create Allocation.

     Allocate funds to make sure they are not spent elsewhere.

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.
        body (Allocation): An Allocation is a designated sum of money reserved for the purpose of
            making some particular payments. Allocations are currently purely virtual objects. They
            exist only in Requestor's database. An Allocation is connected to a payment account
            (wallet) specified by `address` and `paymentPlatform` field. If these fields are not
            present the default payment platform is used and the address is assumed to be identical to
            the Requestor's Node ID.

            **NOTE:** `timeout` and `makeDeposit` field are currently ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Allocation, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        body=body,
        after_timestamp=after_timestamp,
        max_items=max_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Allocation,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Optional[Union[Allocation, ErrorMessage]]:
    """Create Allocation.

     Allocate funds to make sure they are not spent elsewhere.

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.
        body (Allocation): An Allocation is a designated sum of money reserved for the purpose of
            making some particular payments. Allocations are currently purely virtual objects. They
            exist only in Requestor's database. An Allocation is connected to a payment account
            (wallet) specified by `address` and `paymentPlatform` field. If these fields are not
            present the default payment platform is used and the address is assumed to be identical to
            the Requestor's Node ID.

            **NOTE:** `timeout` and `makeDeposit` field are currently ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Allocation, ErrorMessage]
    """

    return sync_detailed(
        client=client,
        body=body,
        after_timestamp=after_timestamp,
        max_items=max_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Allocation,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Union[Allocation, ErrorMessage]]:
    """Create Allocation.

     Allocate funds to make sure they are not spent elsewhere.

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.
        body (Allocation): An Allocation is a designated sum of money reserved for the purpose of
            making some particular payments. Allocations are currently purely virtual objects. They
            exist only in Requestor's database. An Allocation is connected to a payment account
            (wallet) specified by `address` and `paymentPlatform` field. If these fields are not
            present the default payment platform is used and the address is assumed to be identical to
            the Requestor's Node ID.

            **NOTE:** `timeout` and `makeDeposit` field are currently ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Allocation, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        body=body,
        after_timestamp=after_timestamp,
        max_items=max_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Allocation,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Optional[Union[Allocation, ErrorMessage]]:
    """Create Allocation.

     Allocate funds to make sure they are not spent elsewhere.

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.
        body (Allocation): An Allocation is a designated sum of money reserved for the purpose of
            making some particular payments. Allocations are currently purely virtual objects. They
            exist only in Requestor's database. An Allocation is connected to a payment account
            (wallet) specified by `address` and `paymentPlatform` field. If these fields are not
            present the default payment platform is used and the address is assumed to be identical to
            the Requestor's Node ID.

            **NOTE:** `timeout` and `makeDeposit` field are currently ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Allocation, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            after_timestamp=after_timestamp,
            max_items=max_items,
        )
    ).parsed
