from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.exe_script_command_result import ExeScriptCommandResult
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    activity_id: str,
    batch_id: str,
    *,
    command_index: Union[Unset, float] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['commandIndex'] = command_index

    params['timeout'] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/activity-api/v1/activity/{activity_id}/exec/{batch_id}'.format(
            activity_id=activity_id,
            batch_id=batch_id,
        ),
        'params': params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExeScriptCommandResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorMessage.from_dict(response.json())

        return response_403
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
) -> Response[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    activity_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    command_index: Union[Unset, float] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    """Queries for ExeScript batch results.

     'This call shall collect ExeScriptCommand result objects received directly from ExeUnit (via the
    long polling pattern). **Note:** two formats of response are specified (as indicated by the Accept
    header):
      - application/json - standard JSON response, specified below, as code generators handle it
    properly.
      - text/event-stream - an EventSource implementation (as per https://www.w3.org/TR/eventsource/).
        This isn't explicitly specified as code generators generally are unable to handle this.
        The streaming events adhere to following format:

          event: runtime
          data: <RuntimeEvent structure>

        This streaming endpoint requires dedicated implementation. '

    Args:
        activity_id (str):
        batch_id (str):
        command_index (Union[Unset, float]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['ExeScriptCommandResult']]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        batch_id=batch_id,
        command_index=command_index,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    activity_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    command_index: Union[Unset, float] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    """Queries for ExeScript batch results.

     'This call shall collect ExeScriptCommand result objects received directly from ExeUnit (via the
    long polling pattern). **Note:** two formats of response are specified (as indicated by the Accept
    header):
      - application/json - standard JSON response, specified below, as code generators handle it
    properly.
      - text/event-stream - an EventSource implementation (as per https://www.w3.org/TR/eventsource/).
        This isn't explicitly specified as code generators generally are unable to handle this.
        The streaming events adhere to following format:

          event: runtime
          data: <RuntimeEvent structure>

        This streaming endpoint requires dedicated implementation. '

    Args:
        activity_id (str):
        batch_id (str):
        command_index (Union[Unset, float]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['ExeScriptCommandResult']]
    """

    return sync_detailed(
        activity_id=activity_id,
        batch_id=batch_id,
        client=client,
        command_index=command_index,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    command_index: Union[Unset, float] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    """Queries for ExeScript batch results.

     'This call shall collect ExeScriptCommand result objects received directly from ExeUnit (via the
    long polling pattern). **Note:** two formats of response are specified (as indicated by the Accept
    header):
      - application/json - standard JSON response, specified below, as code generators handle it
    properly.
      - text/event-stream - an EventSource implementation (as per https://www.w3.org/TR/eventsource/).
        This isn't explicitly specified as code generators generally are unable to handle this.
        The streaming events adhere to following format:

          event: runtime
          data: <RuntimeEvent structure>

        This streaming endpoint requires dedicated implementation. '

    Args:
        activity_id (str):
        batch_id (str):
        command_index (Union[Unset, float]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, List['ExeScriptCommandResult']]]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        batch_id=batch_id,
        command_index=command_index,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    activity_id: str,
    batch_id: str,
    *,
    client: AuthenticatedClient,
    command_index: Union[Unset, float] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[ErrorMessage, List['ExeScriptCommandResult']]]:
    """Queries for ExeScript batch results.

     'This call shall collect ExeScriptCommand result objects received directly from ExeUnit (via the
    long polling pattern). **Note:** two formats of response are specified (as indicated by the Accept
    header):
      - application/json - standard JSON response, specified below, as code generators handle it
    properly.
      - text/event-stream - an EventSource implementation (as per https://www.w3.org/TR/eventsource/).
        This isn't explicitly specified as code generators generally are unable to handle this.
        The streaming events adhere to following format:

          event: runtime
          data: <RuntimeEvent structure>

        This streaming endpoint requires dedicated implementation. '

    Args:
        activity_id (str):
        batch_id (str):
        command_index (Union[Unset, float]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, List['ExeScriptCommandResult']]
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            batch_id=batch_id,
            client=client,
            command_index=command_index,
            timeout=timeout,
        )
    ).parsed
