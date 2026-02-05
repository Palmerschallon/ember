```python
import importlib
import sys
import os
import logging
from types import ModuleType
from typing import List, Optional, Union

class ModuleReloader:
    """
    A robust and flexible module reloading utility with advanced error handling and logging.

    Features:
    - Safely reload individual modules or entire packages
    - Optional dependency tracking
    - Configurable logging
    - Error resilience
    - Support for nested/complex module structures

    Examples:
    >>> reloader = ModuleReloader()
    >>> reloader.reload('my_module')  # Reload specific module
    >>> reloader.reload_package('my_package')  # Reload entire package
    """

    def __init__(self, log_level: int = logging.INFO):
        """
        Initialize ModuleReloader with configurable logging.

        Args:
            log_level (int): Logging verbosity level. Defaults to logging.INFO.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _is_valid_module(self, module: Union[str, ModuleType]) -> bool:
        """
        Validate if the provided module is legitimate and reloadable.

        Args:
            module: Module name or module object to validate

        Returns:
            bool: Whether module is valid for reloading
        """
        try:
            module_obj = module if isinstance(module, ModuleType) else sys.modules.get(module)
            return module_obj is not None and hasattr(module_obj, '__file__')
        except Exception as e:
            self.logger.warning(f"Module validation failed: {e}")
            return False

    def reload(self, module: Union[str, ModuleType], track_dependencies: bool = False) -> bool:
        """
        Reload a specific module with optional dependency tracking.

        Args:
            module: Module name or module object to reload
            track_dependencies: Whether to attempt reloading dependent modules

        Returns:
            bool: Success status of reload operation
        """
        try:
            if not self._is_valid_module(module):
                self.logger.error(f"Cannot reload invalid module: {module}")
                return False

            module_name = module if isinstance(module, str) else module.__name__
            
            self.logger.info(f"Reloading module: {module_name}")
            reloaded_module = importlib.reload(sys.modules[module_name])

            if track_dependencies:
                self._reload_dependencies(module_name)

            return True

        except Exception as e:
            self.logger.error(f"Reload failed for {module}: {e}")
            return False

    def _reload_dependencies(self, module_name: str) -> None:
        """
        Recursively attempt to reload modules that import the target module.

        Args:
            module_name: Name of the module to find dependencies for
        """
        for name, mod in list(sys.modules.items()):
            try:
                if mod and hasattr(mod, '__file__') and module_name in getattr(mod, '__imports__', []):
                    self.logger.info(f"Reloading dependent module: {name}")
                    importlib.reload(mod)
            except Exception as e:
                self.logger.warning(f"Dependency reload failed for {name}: {e}")

    def reload_package(self, package: str, recursive: bool = True) -> List[str]:
        """
        Reload an entire package, with optional recursive submodule reloading.

        Args:
            package: Name of package to reload
            recursive: Whether to reload all submodules

        Returns:
            List of successfully reloaded module names
        """
        try:
            package_path = sys.modules[package].__path__[0]
            reloaded_modules = []

            for root, _, files in os.walk(package_path):
                for file in files:
                    if file.endswith('.py') and not file.startswith('__'):
                        module_name = os.path.join(root, file).replace(package_path, '').replace('/', '.')[1:-3]
                        full_module_name = f"{package}.{module_name}"

                        if self.reload(full_module_name):
                            reloaded_modules.append(full_module_name)

            return reloaded_modules

        except Exception as e:
            self.logger.error(f"Package reload failed: {e}")
            return []

def main():
    """Demonstration of ModuleReloader capabilities"""
    reloader = ModuleReloader(log_level=logging.DEBUG)
    
    # Example usage
    reloader.reload('os')  # Reload system module
    reloader.reload_package('typing')  # Reload package

if __name__ == "__main__":
    main()
```