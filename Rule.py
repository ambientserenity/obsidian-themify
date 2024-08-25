class Rule():
    def __init__(self, selector, declarations):
        self.selector = selector
        self.declaration = declarations

    def __repr__(self):
        return "Rule with selector=" + self.selector + " and declaration=" + self.declaration