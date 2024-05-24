from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.rejection import Rejection
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    body: Rejection,
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params['timeout'] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/payment-api/v1/invoices/{invoice_id}/reject'.format(
            invoice_id=invoice_id,
        ),
        'params': params,
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
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
        response_504 = ErrorMessage.from_dict(response.json())

        return response_504
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
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    body: Rejection,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[Any, ErrorMessage]]:
    """Reject received Invoice.

     **WARNING:** Operation not implemented.

    Send Invoice Rejected message to Invoice Issuer. Notification of rejection is signalling that
    Requestor does not accept Invoice (for some reason).

    This is a blocking operation. It will not return until the Requestor has acknowledged rejecting the
    Invoice or timeout has passed.

    **NOTE:** A Rejected Invoice can be Accepted subsequently (e.g. as a result of some arbitrage).

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Rejection): Message sent when Requestor rejects a Debit Note or Invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    body: Rejection,
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[Any, ErrorMessage]]:
    """Reject received Invoice.

     **WARNING:** Operation not implemented.

    Send Invoice Rejected message to Invoice Issuer. Notification of rejection is signalling that
    Requestor does not accept Invoice (for some reason).

    This is a blocking operation. It will not return until the Requestor has acknowledged rejecting the
    Invoice or timeout has passed.

    **NOTE:** A Rejected Invoice can be Accepted subsequently (e.g. as a result of some arbitrage).

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Rejection): Message sent when Requestor rejects a Debit Note or Invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        body=body,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    body: Rejection,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Union[Any, ErrorMessage]]:
    """Reject received Invoice.

     **WARNING:** Operation not implemented.

    Send Invoice Rejected message to Invoice Issuer. Notification of rejection is signalling that
    Requestor does not accept Invoice (for some reason).

    This is a blocking operation. It will not return until the Requestor has acknowledged rejecting the
    Invoice or timeout has passed.

    **NOTE:** A Rejected Invoice can be Accepted subsequently (e.g. as a result of some arbitrage).

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Rejection): Message sent when Requestor rejects a Debit Note or Invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    body: Rejection,
    timeout: Union[Unset, float] = 5.0,
) -> Optional[Union[Any, ErrorMessage]]:
    """Reject received Invoice.

     **WARNING:** Operation not implemented.

    Send Invoice Rejected message to Invoice Issuer. Notification of rejection is signalling that
    Requestor does not accept Invoice (for some reason).

    This is a blocking operation. It will not return until the Requestor has acknowledged rejecting the
    Invoice or timeout has passed.

    **NOTE:** A Rejected Invoice can be Accepted subsequently (e.g. as a result of some arbitrage).

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.
        body (Rejection): Message sent when Requestor rejects a Debit Note or Invoice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
            timeout=timeout,
        )
    ).parsed
