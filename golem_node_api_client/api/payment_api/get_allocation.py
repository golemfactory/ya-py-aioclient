from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.allocation import Allocation
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    allocation_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/allocations/{allocation_id}'.format(
            allocation_id=allocation_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Allocation, ErrorMessage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Allocation.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
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
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Allocation, ErrorMessage]]:
    """Get Allocation.

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Allocation, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        allocation_id=allocation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Allocation, ErrorMessage]]:
    """Get Allocation.

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Allocation, ErrorMessage]
    """

    return sync_detailed(
        allocation_id=allocation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Allocation, ErrorMessage]]:
    """Get Allocation.

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Allocation, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        allocation_id=allocation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Allocation, ErrorMessage]]:
    """Get Allocation.

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Allocation, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            allocation_id=allocation_id,
            client=client,
        )
    ).parsed
