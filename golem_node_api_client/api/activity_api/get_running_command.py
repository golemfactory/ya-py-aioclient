from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.exe_script_command_state import ExeScriptCommandState
from golem_node_api_client.types import Response


def _get_kwargs(
    activity_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/activity-api/v1/activity/{activity_id}/command'.format(
            activity_id=activity_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandState']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExeScriptCommandState.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[ErrorMessage, List['ExeScriptCommandState']]]:
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
) -> Response[Union[ErrorMessage, List['ExeScriptCommandState']]]:
    """Get running commands for a specified Activity.

     **Note:** This call shall get routed directly to ExeUnit.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['ExeScriptCommandState']]]
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
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandState']]]:
    """Get running commands for a specified Activity.

     **Note:** This call shall get routed directly to ExeUnit.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['ExeScriptCommandState']]
    """

    return sync_detailed(
        activity_id=activity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorMessage, List['ExeScriptCommandState']]]:
    """Get running commands for a specified Activity.

     **Note:** This call shall get routed directly to ExeUnit.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['ExeScriptCommandState']]]
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
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandState']]]:
    """Get running commands for a specified Activity.

     **Note:** This call shall get routed directly to ExeUnit.

    Args:
        activity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['ExeScriptCommandState']]
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
        )
    ).parsed
