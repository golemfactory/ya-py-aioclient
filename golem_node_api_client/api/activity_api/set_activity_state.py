from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.activity_state import ActivityState
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    activity_id: str,
    *,
    body: ActivityState,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        'method': 'put',
        'url': '/activity-api/v1/activity/{activity_id}/state'.format(
            activity_id=activity_id,
        ),
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorMessage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
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
) -> Response[Union[Any, ErrorMessage]]:
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
    body: ActivityState,
) -> Response[Union[Any, ErrorMessage]]:
    """Set state of specified Activity.

    Args:
        activity_id (str):
        body (ActivityState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient,
    body: ActivityState,
) -> Optional[Union[Any, ErrorMessage]]:
    """Set state of specified Activity.

    Args:
        activity_id (str):
        body (ActivityState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        activity_id=activity_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient,
    body: ActivityState,
) -> Response[Union[Any, ErrorMessage]]:
    """Set state of specified Activity.

    Args:
        activity_id (str):
        body (ActivityState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient,
    body: ActivityState,
) -> Optional[Union[Any, ErrorMessage]]:
    """Set state of specified Activity.

    Args:
        activity_id (str):
        body (ActivityState):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
            body=body,
        )
    ).parsed
