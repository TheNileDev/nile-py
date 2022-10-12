from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.action import Action
from ..models.resource import Resource
from ..models.subject import Subject
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePolicyRequest")


@attr.s(auto_attribs=True)
class UpdatePolicyRequest:
    """
    Attributes:
        actions (List[Action]): The actions to be allowed on the resource if an access policy matches a
            request.

            At least one action must be provided and executable actions
            (i.e: `read`, `write`) cannot be combined with non-executable actions
            (i.e: `deny`).

            If multiple access policies match a request, policies
            with a `deny` action take precedence over policies with a `read`
            action. You can define `deny` access policies to make exceptions in
            your policies that allow access.
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
    """

    actions: List[Action]
    subject: Union[Unset, Subject] = UNSET
    resource: Union[Unset, Resource] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.value

            actions.append(actions_item)

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = Action(actions_item_data)

            actions.append(actions_item)

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

        update_policy_request = cls(
            actions=actions,
            subject=subject,
            resource=resource,
        )

        update_policy_request.additional_properties = d
        return update_policy_request

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
