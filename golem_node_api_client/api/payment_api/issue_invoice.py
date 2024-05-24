from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.invoice import Invoice
from golem_node_api_client.types import Response


def _get_kwargs(
    *,
    body: Invoice,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/payment-api/v1/invoices',
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, Invoice]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Invoice.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorMessage, Invoice]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Invoice,
) -> Response[Union[ErrorMessage, Invoice]]:
    """Issue an Invoice.

    Args:
        body (Invoice): An Invoice is an artifact issued by the Provider to the Requestor, in the
            context of a specific Agreement. It indicates the total Amount owed by the Requestor in
            this Agreement. No further Debit Notes shall be issued after the Invoice is issued. The
            issue of Invoice signals the Termination of the Agreement (if it hasn't been terminated
            already). No Activity execution is allowed after the Invoice is issued.

            **NOTE:** An invoice can be issued even before any Activity is started in the context of
            an Agreement (eg. in one off, 'fire-and-forget' payment regime).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, Invoice]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Invoice,
) -> Optional[Union[ErrorMessage, Invoice]]:
    """Issue an Invoice.

    Args:
        body (Invoice): An Invoice is an artifact issued by the Provider to the Requestor, in the
            context of a specific Agreement. It indicates the total Amount owed by the Requestor in
            this Agreement. No further Debit Notes shall be issued after the Invoice is issued. The
            issue of Invoice signals the Termination of the Agreement (if it hasn't been terminated
            already). No Activity execution is allowed after the Invoice is issued.

            **NOTE:** An invoice can be issued even before any Activity is started in the context of
            an Agreement (eg. in one off, 'fire-and-forget' payment regime).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, Invoice]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Invoice,
) -> Response[Union[ErrorMessage, Invoice]]:
    """Issue an Invoice.

    Args:
        body (Invoice): An Invoice is an artifact issued by the Provider to the Requestor, in the
            context of a specific Agreement. It indicates the total Amount owed by the Requestor in
            this Agreement. No further Debit Notes shall be issued after the Invoice is issued. The
            issue of Invoice signals the Termination of the Agreement (if it hasn't been terminated
            already). No Activity execution is allowed after the Invoice is issued.

            **NOTE:** An invoice can be issued even before any Activity is started in the context of
            an Agreement (eg. in one off, 'fire-and-forget' payment regime).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, Invoice]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Invoice,
) -> Optional[Union[ErrorMessage, Invoice]]:
    """Issue an Invoice.

    Args:
        body (Invoice): An Invoice is an artifact issued by the Provider to the Requestor, in the
            context of a specific Agreement. It indicates the total Amount owed by the Requestor in
            this Agreement. No further Debit Notes shall be issued after the Invoice is issued. The
            issue of Invoice signals the Termination of the Agreement (if it hasn't been terminated
            already). No Activity execution is allowed after the Invoice is issued.

            **NOTE:** An invoice can be issued even before any Activity is started in the context of
            an Agreement (eg. in one off, 'fire-and-forget' payment regime).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, Invoice]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
