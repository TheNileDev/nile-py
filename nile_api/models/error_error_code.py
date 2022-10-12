from enum import Enum


class ErrorErrorCode(str, Enum):
    INTERNAL_ERROR = "internal_error"
    BAD_REQUEST = "bad_request"
    UNAUTHORIZED_CREDENTIALS = "unauthorized_credentials"
    USER_NOT_FOUND = "user_not_found"
    ORG_NOT_FOUND = "org_not_found"
    WORKSPACE_NOT_FOUND = "workspace_not_found"
    INVITE_NOT_FOUND = "invite_not_found"
    DUPLICATE_ORG_NAME = "duplicate_org_name"
    DUPLICATE_WORKSPACE_NAME = "duplicate_workspace_name"
    EMPTY_ORG_NAME = "empty_org_name"
    EMPTY_WORKSPACE_NAME = "empty_workspace_name"
    DUPLICATE_USER_EMAIL = "duplicate_user_email"
    USER_ALREADY_IN_ORG = "user_already_in_org"
    DUPLICATE_ENTITY_NAME = "duplicate_entity_name"
    ENTITY_NOT_FOUND = "entity_not_found"
    INSTANCE_NOT_FOUND = "instance_not_found"
    ACCESS_POLICY_NOT_FOUND = "access_policy_not_found"
    INVALID_ENTITY_SCHEMA = "invalid_entity_schema"
    INVALID_ID = "invalid_id"
    INVALID_ACTION = "invalid_action"
    EMPTY_ACTIONS = "empty_actions"
    INVALID_ACTION_COMBINATION = "invalid_action_combination"
    INVALID_POLICY_VARIABLE = "invalid_policy_variable"
    FORBIDDEN = "forbidden"
    METRIC_NOT_FOUND = "metric_not_found"

    def __str__(self) -> str:
        return str(self.value)
