import os
import sys

active_dcc_is_maya = "maya" in os.path.basename(sys.executable)

if active_dcc_is_maya:
    from . import tool_name_dcc_maya as dcc_module
    dcc = dcc_module.ToolNameMaya()
else:
    from . import tool_name_dcc_core as dcc_module
    dcc = dcc_module.ToolNameCoreInterface()
