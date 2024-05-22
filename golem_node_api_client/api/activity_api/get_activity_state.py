from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_state import ActivityState
from ...types import Response


def _get_kwargs(
    activity_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/activity-api/v1/activity/{activity_id}/state".format(
            activity_id=activity_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActivityState, Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActivityState.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ActivityState, Any]]:
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
) -> Response[Union[ActivityState, Any]]:
    """Get state of specified Activity.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityState, Any]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ActivityState, Any]]:
    """Get state of specified Activity.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityState, Any]
    """

    return sync_detailed(
        activity_id=activity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ActivityState, Any]]:
    """Get state of specified Activity.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityState, Any]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ActivityState, Any]]:
    """Get state of specified Activity.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityState, Any]
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
        )
    ).parsed
