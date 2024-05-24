import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.debit_note import DebitNote
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params['afterTimestamp'] = json_after_timestamp

    params['maxItems'] = max_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/debitNotes',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['DebitNote']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DebitNote.from_dict(response_200_item_data)

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
) -> Response[Union[ErrorMessage, List['DebitNote']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Union[ErrorMessage, List['DebitNote']]]:
    """Get Debit Notes known by this node (either issued by this Provider or received by this Requestor).

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['DebitNote']]]
    """

    kwargs = _get_kwargs(
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
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['DebitNote']]]:
    """Get Debit Notes known by this node (either issued by this Provider or received by this Requestor).

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['DebitNote']]
    """

    return sync_detailed(
        client=client,
        after_timestamp=after_timestamp,
        max_items=max_items,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Union[ErrorMessage, List['DebitNote']]]:
    """Get Debit Notes known by this node (either issued by this Provider or received by this Requestor).

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['DebitNote']]]
    """

    kwargs = _get_kwargs(
        after_timestamp=after_timestamp,
        max_items=max_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Optional[Union[ErrorMessage, List['DebitNote']]]:
    """Get Debit Notes known by this node (either issued by this Provider or received by this Requestor).

    Args:
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['DebitNote']]
    """

    return (
        await asyncio_detailed(
            client=client,
            after_timestamp=after_timestamp,
            max_items=max_items,
        )
    ).parsed
