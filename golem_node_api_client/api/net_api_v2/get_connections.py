from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.types import Response


def _get_kwargs(
    network_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/net-api/v2/vpn/net/{network_id}/tcp'.format(
            network_id=network_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    network_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """GetConnections - Fetches Requestor's TCP connections in a Network.

    Args:
        network_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    network_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """GetConnections - Fetches Requestor's TCP connections in a Network.

    Args:
        network_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
