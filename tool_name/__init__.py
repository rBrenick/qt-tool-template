def main(*args, **kwargs):
    from . import tool_name_ui
    return tool_name_ui.main(*args, **kwargs)


def reload_modules():
    import sys
    if sys.version_info.major >= 3:
        from importlib import reload
    else:
        from imp import reload
    
    from . import tool_name_dcc_core
    from . import tool_name_system
    from . import tool_name_ui
    reload(tool_name_dcc_core)
    reload(tool_name_system)
    reload(tool_name_ui)
    

def startup():
    from maya import cmds
    cmds.optionVar(stringValue="")
