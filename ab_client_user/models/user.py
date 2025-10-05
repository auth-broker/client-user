import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """User model.

    Attributes:
        updated_at (datetime.datetime):
        created_at (datetime.datetime):
        oidc_sub (str):
        oidc_iss (str):
        last_seen (Union[None, datetime.datetime]):
        is_active (Union[Unset, bool]):  Default: True.
        id (Union[Unset, UUID]):
        email (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        preferred_username (Union[None, Unset, str]):
    """

    updated_at: datetime.datetime
    created_at: datetime.datetime
    oidc_sub: str
    oidc_iss: str
    last_seen: Union[None, datetime.datetime]
    is_active: Union[Unset, bool] = True
    id: Union[Unset, UUID] = UNSET
    email: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    preferred_username: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        created_at = self.created_at.isoformat()

        oidc_sub = self.oidc_sub

        oidc_iss = self.oidc_iss

        last_seen: Union[None, str]
        if isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        is_active = self.is_active

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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
                "updated_at": updated_at,
                "created_at": created_at,
                "oidc_sub": oidc_sub,
                "oidc_iss": oidc_iss,
                "last_seen": last_seen,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if id is not UNSET:
            field_dict["id"] = id
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
        updated_at = isoparse(d.pop("updated_at"))

        created_at = isoparse(d.pop("created_at"))

        oidc_sub = d.pop("oidc_sub")

        oidc_iss = d.pop("oidc_iss")

        def _parse_last_seen(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = isoparse(data)

                return last_seen_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_seen = _parse_last_seen(d.pop("last_seen"))

        is_active = d.pop("is_active", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

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

        user = cls(
            updated_at=updated_at,
            created_at=created_at,
            oidc_sub=oidc_sub,
            oidc_iss=oidc_iss,
            last_seen=last_seen,
            is_active=is_active,
            id=id,
            email=email,
            display_name=display_name,
            preferred_username=preferred_username,
        )

        user.additional_properties = d
        return user

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
