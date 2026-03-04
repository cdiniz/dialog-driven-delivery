import sys
from pathlib import Path

MCP_SERVER_DIR = str(Path(__file__).resolve().parents[2] / "d3" / "mcp_server")

if MCP_SERVER_DIR not in sys.path:
    sys.path.insert(0, MCP_SERVER_DIR)
