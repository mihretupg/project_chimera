# Project Chimera: Tooling Strategy

## Developer Tools (MCP)

These tools support development, debugging, and local experimentation for Project Chimera. All tools expose MCP endpoints to allow agents or IDEs to access resources programmatically.

| Tool Name        | MCP Server             | Purpose                                           | Notes |
|-----------------|----------------------|-------------------------------------------------|------|
| git-mcp          | mcp-server-git       | Version control: commit, branch, diff, push/pull | Connects repo actions via MCP protocol |
| filesystem-mcp   | mcp-server-fs        | File operations: read, write, list directory    | Enables agent-assisted file editing |
| logging-mcp      | mcp-server-log       | Real-time logging and analytics                 | Helps monitor swarm execution |
| redis-mcp        | mcp-server-redis     | Task queue inspection and management            | Connects Planner/Worker/Queue |
| api-mcp          | mcp-server-http      | Test REST APIs, GET/POST requests               | Useful for integration testing |
