import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.action import Action
from ..models.policy_type import PolicyType
from ..models.resource import Resource
from ..models.subject import Subject
from ..types import UNSET, Unset

T = TypeVar("T", bound="Policy")


@attr.s(auto_attribs=True)
class Policy:
    """
    Attributes:
        id (str):
        type (PolicyType):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
        seq (Union[Unset, int]):
        deleted (Union[Unset, datetime.datetime]):
        subject (Union[Unset, Subject]):   A subset of properties of a user to authorize against.

              You can specify concrete values for subject properties
              or use variables to match a subject property against a resource property.

              An access policy with no resource (which matches all resources)
              and the following subject would allow access to any resource with the same location as the subject:
              ```
              {
                "metadata": {
                  "location": ${resource.properties.location}
                }
              }
              ```
        resource (Union[Unset, Resource]): A subset of properties of any custom or built-in entity instance to authorize
            against.

            All properties on a resource are optional, and any combination of them can be specified when creating a policy.
            You can specify concrete values for resource and subject properties
            or use variables to match a subject property against a resource property.

            An access policy with the following resource would allow access to clusters with location matching the subject's
            region:
            ```
            {
              "type": "cluster",
              "properties": {
                "location": ${subject.metadata.location}
              }
            }
            ```


            Note that:
            * Only exact matching of properties is supported for now.
            * For built-in entity instances, only the Policy entity is currently supported.
            * Custom properties on a resource must be specified under the "properties" key.
             Example: {'id': 'inst_123', 'type': 'cluster', 'properties': {'region': 'us-west-2', 'status': 'running'}}.
        actions (Union[Unset, List[Action]]):
    """

    id: str
    type: PolicyType
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    seq: Union[Unset, int] = UNSET
    deleted: Union[Unset, datetime.datetime] = UNSET
    subject: Union[Unset, Subject] = UNSET
    resource: Union[Unset, Resource] = UNSET
    actions: Union[Unset, List[Action]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        seq = self.seq
        deleted: Union[Unset, str] = UNSET
        if not isinstance(self.deleted, Unset):
            deleted = self.deleted.isoformat()

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        actions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.value

                actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if seq is not UNSET:
            field_dict["seq"] = seq
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if subject is not UNSET:
            field_dict["subject"] = subject
        if resource is not UNSET:
            field_dict["resource"] = resource
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = PolicyType(d.pop("type"))

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        seq = d.pop("seq", UNSET)

        _deleted = d.pop("deleted", UNSET)
        deleted: Union[Unset, datetime.datetime]
        if isinstance(_deleted, Unset):
            deleted = UNSET
        else:
            deleted = isoparse(_deleted)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, Subject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = Subject.from_dict(_subject)

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, Resource]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = Resource.from_dict(_resource)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = Action(actions_item_data)

            actions.append(actions_item)

        policy = cls(
            id=id,
            type=type,
            created=created,
            updated=updated,
            seq=seq,
            deleted=deleted,
            subject=subject,
            resource=resource,
            actions=actions,
        )

        policy.additional_properties = d
        return policy

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
