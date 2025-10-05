from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertByOIDCRequest")


@_attrs_define
class UpsertByOIDCRequest:
    """Request model for creating or updating a user based on OIDC information.

    Attributes:
        oidc_sub (str): The subject (unique user identifier) provided by the OIDC provider.
        oidc_iss (str): The issuer URL or identifier of the OIDC provider.
        email (Union[None, Unset, str]): User’s email address from the identity provider, if available.
        display_name (Union[None, Unset, str]): Human-readable name shown in the UI.
        preferred_username (Union[None, Unset, str]): Username the user prefers to be known by (may differ from email).
    """

    oidc_sub: str
    oidc_iss: str
    email: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    preferred_username: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oidc_sub = self.oidc_sub

        oidc_iss = self.oidc_iss

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        preferred_username: Union[None, Unset, str]
        if isinstance(self.preferred_username, Unset):
            preferred_username = UNSET
        else:
            preferred_username = self.preferred_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "oidc_sub": oidc_sub,
                "oidc_iss": oidc_iss,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if preferred_username is not UNSET:
            field_dict["preferred_username"] = preferred_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oidc_sub = d.pop("oidc_sub")

        oidc_iss = d.pop("oidc_iss")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_preferred_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_username = _parse_preferred_username(d.pop("preferred_username", UNSET))

        upsert_by_oidc_request = cls(
            oidc_sub=oidc_sub,
            oidc_iss=oidc_iss,
            email=email,
            display_name=display_name,
            preferred_username=preferred_username,
        )

        upsert_by_oidc_request.additional_properties = d
        return upsert_by_oidc_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
