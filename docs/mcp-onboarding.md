# MCP onboarding for Copilot CLI

No secrets belong in these files or in `maq-project.json`. Authenticate interactively; never paste tokens.

Tool names vary by server version. After connecting, rediscover tool schemas and do not assume argument shapes.

## Azure DevOps MCP (`@azure-devops/mcp`)

Used for work items, PRs, iterations, and search.

Add to your Copilot CLI MCP configuration (for example `~/.copilot/mcp-config.json`):

```json
{
  "mcpServers": {
    "azure-devops": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "<your-ado-organization-name>"],
      "tools": ["*"]
    }
  }
}
```

- The organization name is the segment after `dev.azure.com/` in `ado.organizationUrl`.
- Sign in through the browser prompt on first use with the account that has project access.
- Verify: list projects, then read one work item in the configured project.
- Writes remain subject to preview, approval, and revision checks in the safety rules.

## Fabric and FabricIQ MCP

Used for semantic model and report discovery, bounded DAX (`FabricIQ-*`), and bounded SQL endpoint reads (`fabric-sqlendpoint-execute_query`).

1. Obtain the MCP server endpoint or install instructions from your Fabric administrator or the official Microsoft Fabric MCP documentation.
2. Add each server to your Copilot CLI MCP configuration using the vendor-provided command or URL, for example:

```json
{
  "mcpServers": {
    "FabricIQ": { "type": "http", "url": "<fabriciq-mcp-endpoint>" },
    "fabric-sqlendpoint": { "type": "http", "url": "<sql-endpoint-mcp-endpoint>" }
  }
}
```

3. Authenticate with your Entra ID account when prompted.
4. Verify: resolve a known DEV semantic model and run a small, bounded read.

## Checks before use

- The signed-in identity has access to the DEV workspaces in `maq-project.json` only as far as policy allows.
- Query limits (`fabric.queryLimits`) are honored by the execution surface; if the tool cannot enforce a timeout, report the limitation.
- FabricIQ discovery covers semantic models and reports only; other workloads use the `maq-fabric-*` adapters and their companion skills.
