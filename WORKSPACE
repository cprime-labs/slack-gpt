#--------------------------------------------------------------------------------------------------------------
# Workspace configuration
#--------------------------------------------------------------------------------------------------------------
workspace(name = "slack-gpt")

#--------------------------------------------------------------------------------------------------------------
# Global configuration
#--------------------------------------------------------------------------------------------------------------

load("@//.bazel/workspace:workspace_global.bzl", "workspace_global")

workspace_global()

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()

#--------------------------------------------------------------------------------------------------------------
# Python configuration
#--------------------------------------------------------------------------------------------------------------
load("@//.bazel/workspace:workspace_python.bzl", "workspace_python")

workspace_python()
