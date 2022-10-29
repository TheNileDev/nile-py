def test_it_imports():
    import nile_api

    nile_api


def test_toplevel_contents():
    import nile_api

    keys = [key for key in dir(nile_api) if not key.startswith("_")]
    print(keys)
    assert set(keys) == set(["AuthenticatedClient", "Client", "client"])


def test_packages():
    import importlib
    import pkgutil

    import nile_api.api

    subpkgs = [
        pkg.name for pkg in pkgutil.walk_packages(nile_api.api.__path__)
    ]
    assert set(subpkgs) == set(
        [
            "access",
            "developers",
            "entities",
            "metrics",
            "organizations",
            "users",
            "workspaces",
        ]
    )

    for subpkg in subpkgs:
        mod = importlib.import_module("nile_api.api." + subpkg)
        pub_funs = [f.name for f in pkgutil.walk_packages(mod.__path__)]
        print(pub_funs)

        match subpkg:
            case "workspaces":
                assert set(pub_funs) == {
                    "create_access_token",
                    "create_workspace",
                    "delete_access_token",
                    "get_access_token",
                    "get_workspace_open_api",
                    "list_access_tokens",
                    "list_workspaces",
                    "update_access_token",
                }
            case "organizations":
                assert set(pub_funs) == {
                    "accept_invite",
                    "add_user_to_org",
                    "create_organization",
                    "delete_organization",
                    "get_organization",
                    "list_invites",
                    "list_organizations",
                    "list_users_in_org",
                    "remove_user_from_org",
                    "update_organization",
                    "update_user_in_org",
                }
            case "entities":
                assert set(pub_funs) == {
                    "create_entity",
                    "create_instance",
                    "delete_instance",
                    "get_entity",
                    "get_instance",
                    "get_open_api",
                    "instance_events",
                    "list_entities",
                    "list_instances",
                    "list_instances_in_workspace",
                    "update_entity",
                    "update_instance",
                }
            case "developers":
                assert set(pub_funs) == {
                    "create_developer",
                    "developer_google_o_auth_callback",
                    "login_developer",
                    "start_developer_google_o_auth",
                    "validate_developer",
                }
            case "users":
                assert set(pub_funs) == {
                    "create_user",
                    "delete_user",
                    "get_user",
                    "list_users",
                    "login_user",
                    "me",
                    "token",
                    "update_user",
                    "validate_user",
                }
            case "access":
                assert set(pub_funs) == {
                    "create_policy",
                    "delete_policy",
                    "get_policy",
                    "list_policies",
                    "update_policy",
                }
            case "metrics":
                assert set(pub_funs) == {
                    "aggregate_metrics",
                    "filter_metrics",
                    "filter_metrics_for_entity_type",
                    "list_metric_definitions",
                    "list_metric_definitions_for_entity_type",
                    "produce_batch_of_metrics",
                }

    # Note: JS lib has tests for connect, login and setting workspaces
    # This is because in the JS lib these methods set value of workspaces and token in all Nile classes
    # The Python lib doesn't do this, instead developers need to pass in the workspace and client in each method
    # Therefore there are no tests for this non-existing functionality
