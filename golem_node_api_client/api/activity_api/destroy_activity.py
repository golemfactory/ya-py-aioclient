from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    activity_id: str,
    *,
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['timeout'] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'delete',
        'url': '/activity-api/v1/activity/{activity_id}'.format(
            activity_id=activity_id,
        ),
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
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
    activity_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """Destroys given Activity.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        activity_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """Destroys given Activity.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        activity_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
