class DynamicAttribute:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __getattr__(self, attribute):
        if attribute.startswith('fallback_'):
            name = attribute.replace('fallback_',"")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"{self.__class__.__name__} has no attribute {attribute}")

if __name__ == "__main__":
    dyn = DynamicAttribute(123)
    print(dyn.attribute)
    print(dyn.__dict__)
    print(dyn.fallback_firas)
    dyn.__dict__['fallback_firas'] = 42
    print(dyn.fallback_firas)
    print(getattr(dyn, "attribute"))
    print(getattr(dyn, "something", "default"))