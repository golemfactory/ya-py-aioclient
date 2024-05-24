from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.driver_status_property import DriverStatusProperty
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    *,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['network'] = network

    params['driver'] = driver

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/payments/status',
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['DriverStatusProperty']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DriverStatusProperty.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
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
) -> Response[Union[ErrorMessage, List['DriverStatusProperty']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['DriverStatusProperty']]]:
    """Get status of the payment driver

     This only relates to the erc20 driver, not erc20legacy. The returned list contains individual status
    properties, which can be used to identify problems like missing funds or misconfigured max fee per
    gas on a per-chain (network) basis.

    Args:
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['DriverStatusProperty']]]
    """

    kwargs = _get_kwargs(
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
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['DriverStatusProperty']]]:
    """Get status of the payment driver

     This only relates to the erc20 driver, not erc20legacy. The returned list contains individual status
    properties, which can be used to identify problems like missing funds or misconfigured max fee per
    gas on a per-chain (network) basis.

    Args:
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['DriverStatusProperty']]
    """

    return sync_detailed(
        client=client,
        network=network,
        driver=driver,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorMessage, List['DriverStatusProperty']]]:
    """Get status of the payment driver

     This only relates to the erc20 driver, not erc20legacy. The returned list contains individual status
    properties, which can be used to identify problems like missing funds or misconfigured max fee per
    gas on a per-chain (network) basis.

    Args:
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['DriverStatusProperty']]]
    """

    kwargs = _get_kwargs(
        network=network,
        driver=driver,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    network: Union[Unset, str] = UNSET,
    driver: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorMessage, List['DriverStatusProperty']]]:
    """Get status of the payment driver

     This only relates to the erc20 driver, not erc20legacy. The returned list contains individual status
    properties, which can be used to identify problems like missing funds or misconfigured max fee per
    gas on a per-chain (network) basis.

    Args:
        network (Union[Unset, str]):
        driver (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['DriverStatusProperty']]
    """

    return (
        await asyncio_detailed(
            client=client,
            network=network,
            driver=driver,
        )
    ).parsed
