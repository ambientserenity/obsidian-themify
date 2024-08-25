from Rule import Rule
def increment_delim_count(c):
    if c == "{":
        return 1
    elif c == "}":
        return -1

    return 0

def file_to_rules(filepath):
    with open(filepath) as f:
        txt = f.read()
        output = []
        selector_str = ""
        declaration_str = ""

        i = 0
        delim_count = 0
        while i < len(txt):

            delim_count += increment_delim_count(txt[i])
            if delim_count < 0:
                raise RuntimeError("Invalid CSS: orphaned braces")

            while delim_count == 0:
                selector_str += txt[i]

                if txt[i] == ";":
                    selector_str = ""

                delim_count += increment_delim_count(txt[i])

                i += 1

            selector_str = selector_str[:-1].strip()

            while delim_count > 0:
                declaration_str += txt[i]

                delim_count += increment_delim_count(txt[i])

                i += 1
            declaration_str = "{" + declaration_str
            declaration_str = declaration_str.strip()
            output.append(Rule(selector_str, declaration_str))
            selector_str = ""
            declaration_str = ""

        return output