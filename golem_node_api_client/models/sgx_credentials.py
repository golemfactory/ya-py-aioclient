from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

T = TypeVar('T', bound='SgxCredentials')


@dataclass
class SgxCredentials:
    """
    Attributes:
        enclave_pub_key (str):
        requestor_pub_key (str):
        payload_hash (str):
        ias_report (str):
        ias_sig (str):
    """

    enclave_pub_key: str
    requestor_pub_key: str
    payload_hash: str
    ias_report: str
    ias_sig: str
    additional_properties: Dict[str, Any] = field(init=False, default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enclave_pub_key = self.enclave_pub_key

        requestor_pub_key = self.requestor_pub_key

        payload_hash = self.payload_hash

        ias_report = self.ias_report

        ias_sig = self.ias_sig

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'enclavePubKey': enclave_pub_key,
                'requestorPubKey': requestor_pub_key,
                'payloadHash': payload_hash,
                'iasReport': ias_report,
                'iasSig': ias_sig,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enclave_pub_key = d.pop('enclavePubKey')

        requestor_pub_key = d.pop('requestorPubKey')

        payload_hash = d.pop('payloadHash')

        ias_report = d.pop('iasReport')

        ias_sig = d.pop('iasSig')

        sgx_credentials = cls(
            enclave_pub_key=enclave_pub_key,
            requestor_pub_key=requestor_pub_key,
            payload_hash=payload_hash,
            ias_report=ias_report,
            ias_sig=ias_sig,
        )

        sgx_credentials.additional_properties = d
        return sgx_credentials

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
