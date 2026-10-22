# MCP onboarding for Copilot CLI

No secrets belong in these files or in `maq-project.toon`. Authenticate interactively; never paste tokens. The TOON contains platform identifiers only; workflow policy is baked into the skills.

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
- Azure DevOps workflow skills are resolved directly from the `microsoft/azure-devops-skills` APM dependency; rediscover the available skill/tool schemas instead of assuming server-version-specific arguments.

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

- The signed-in identity has access to the DEV workspaces in `fabric.devWorkspaceIds` in `maq-project.toon` only as far as policy allows. Validate workspace identity and environment; lists must not overlap.
- The execution surface honors fixed limits: stated purpose, at most 250 returned rows, and a 60-second timeout/budget where supported. If timeout enforcement is unavailable, report the limitation and narrow the scan.
- FabricIQ discovery covers semantic models and reports only. For other workloads, use the directly installed Fabric companion skill identified in `capability-matrix.json`; if no supported skill/tool binding exists, report the operation as `blocked` or `manual-only` rather than improvising.
