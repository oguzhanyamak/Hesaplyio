import importlib
import pkgutil
from typing import Dict, List
import app.calculators.definitions as definitions

class CalculatorRegistry:
    def __init__(self):
        self._calculators: Dict[str, dict] = {}
        self._load_all()

    def _load_all(self):
        import os
        base_path = os.path.dirname(__file__)
        def_path = os.path.join(base_path, "definitions")
        
        for root, dirs, files in os.walk(def_path):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    # Calculate module path robustly for both Windows and Linux
                    rel_path = os.path.relpath(os.path.join(root, file), def_path)
                    normalized_path = rel_path.replace("\\", ".").replace("/", ".").replace(".py", "")
                    module_name = f"app.calculators.definitions.{normalized_path}"
                    try:
                        # Use importlib.reload for robustness during StatReload
                        module = importlib.import_module(module_name)
                        importlib.reload(module) 
                        for attr_name in dir(module):
                            if attr_name.endswith("_CONFIG"):
                                config = getattr(module, attr_name)
                                if isinstance(config, dict) and "slug" in config:
                                    slug = config["slug"]
                                    category = config.get("category", "")
                                    
                                    # Central status check
                                    is_enabled = True
                                    try:
                                        from .calculator_settings import CALCULATOR_STATUS, CATEGORY_STATUS
                                        # 1. Check Slug Level
                                        if CALCULATOR_STATUS.get(slug) is False:
                                            is_enabled = False
                                        # 2. Check Category Level
                                        if category and CATEGORY_STATUS.get(category) is False:
                                            is_enabled = False
                                    except ImportError:
                                        pass
                                    
                                    # 3. Check Individual File Flag (e.g. "enabled": False)
                                    if config.get("enabled", True) is False:
                                        is_enabled = False
                                    
                                    if not is_enabled:
                                        continue
                                    
                                    # Ensure required structure for template compatibility
                                    if "seo" not in config:
                                        config["seo"] = {
                                            "meta_title": config.get("title", ""),
                                            "meta_description": config.get("description", ""),
                                            "meta_keywords": [],
                                            "schema_type": "SoftwareApplication"
                                        }
                                    if "faq" not in config:
                                        config["faq"] = []
                                        
                                    self._calculators[slug] = config
                    except Exception as e:
                        print(f"Error loading {module_name}: {e}")
        print("LOADED CALCULATORS COUNT:", len(self._calculators))
        print("LOADED SLUGS:", list(self._calculators.keys()))

    def get_by_slug(self, slug: str) -> dict:
        return self._calculators.get(slug)
        
    def get_all(self) -> List[dict]:
        return list(self._calculators.values())

registry = CalculatorRegistry()
