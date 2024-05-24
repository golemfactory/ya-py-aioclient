from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    network_id: str,
    ip: str,
    port: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/net-api/v2/vpn/net/{network_id}/tcp/{ip}/{port}'.format(
            network_id=network_id,
            ip=ip,
            port=port,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorMessage]]:
    if response.status_code == HTTPStatus.SWITCHING_PROTOCOLS:
        response_101 = cast(Any, None)
        return response_101
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
) -> Response[Union[Any, ErrorMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    network_id: str,
    ip: str,
    port: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorMessage]]:
    """
    Args:
        network_id (str):
        ip (str):
        port (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        ip=ip,
        port=port,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    network_id: str,
    ip: str,
    port: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorMessage]]:
    """
    Args:
        network_id (str):
        ip (str):
        port (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        network_id=network_id,
        ip=ip,
        port=port,
        client=client,
    ).parsed


async def asyncio_detailed(
    network_id: str,
    ip: str,
    port: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorMessage]]:
    """
    Args:
        network_id (str):
        ip (str):
        port (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        network_id=network_id,
        ip=ip,
        port=port,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    network_id: str,
    ip: str,
    port: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorMessage]]:
    """
    Args:
        network_id (str):
        ip (str):
        port (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            network_id=network_id,
            ip=ip,
            port=port,
            client=client,
        )
    ).parsed
