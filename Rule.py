class Rule():
    def __init__(self, selector_str, declaration_str):
        self.selector_str = selector_str
        self.declaration_str = declaration_str

    def __repr__(self):
        return "Rule with selector=" + self.selector_str + " and declaration=" + self.declaration_str
