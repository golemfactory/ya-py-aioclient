from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_activity_request import CreateActivityRequest
from ...models.create_activity_result import CreateActivityResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union["CreateActivityRequest", str],
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/activity-api/v1/activity",
        "params": params,
    }

    _body: Union[Dict[str, Any], str]
    if isinstance(body, CreateActivityRequest):
        _body = body.to_dict()
    else:
        _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["CreateActivityResult", str]]]:
    if response.status_code == HTTPStatus.CREATED:

        def _parse_response_201(data: object) -> Union["CreateActivityResult", str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1 = CreateActivityResult.from_dict(data)

                return response_201_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CreateActivityResult", str], data)

        response_201 = _parse_response_201(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
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
) -> Response[Union[Any, Union["CreateActivityResult", str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["CreateActivityRequest", str],
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[Any, Union["CreateActivityResult", str]]]:
    """Creates new Activity based on given Agreement.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Union['CreateActivityRequest', str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['CreateActivityResult', str]]]
    """

    kwargs = _get_kwargs(
        body=body,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union["CreateActivityRequest", str],
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[Any, Union["CreateActivityResult", str]]]:
    """Creates new Activity based on given Agreement.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Union['CreateActivityRequest', str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['CreateActivityResult', str]]
    """

    return sync_detailed(
        client=client,
        body=body,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["CreateActivityRequest", str],
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[Any, Union["CreateActivityResult", str]]]:
    """Creates new Activity based on given Agreement.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Union['CreateActivityRequest', str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['CreateActivityResult', str]]]
    """

    kwargs = _get_kwargs(
        body=body,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union["CreateActivityRequest", str],
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[Any, Union["CreateActivityResult", str]]]:
    """Creates new Activity based on given Agreement.

     **Note:** This call shall get routed as a provider event (see ProviderEvent structure).

    Args:
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Union['CreateActivityRequest', str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['CreateActivityResult', str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            timeout=timeout,
        )
    ).parsed
