import os
import importlib
import sys

def load_plugins():
    plugins = {}
    
    
    plugin_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "plugins")

    
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  
            full_module_path = f"plugins.{module_name}"  
            module = importlib.import_module(full_module_path)

            if hasattr(module, "run") and hasattr(module, "name"):
                plugins[module.name] = module.run

    return plugins

