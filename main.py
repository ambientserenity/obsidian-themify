from Rule import Rule
import json

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

def convert_rules(rule_array, conversion_dict, output_filepath):
    with open(output_filepath, "w+") as f:
        f.truncate(0)
    for rule in rule_array:

        with open(output_filepath, "a+") as f:
            f.write(rule.selector_str + rule.declaration_str + "\n\n")

        try:
            if conversion_dict[rule.selector_str]:
                for new_selector in conversion_dict[rule.selector_str]:
                    with open(output_filepath, "a+") as f:
                        f.write(new_selector + rule.declaration_str)
        except KeyError:
            pass


if __name__ == '__main__':
    rules = file_to_rules("test.css")

    conversion_dict = json.load(open("dictionary.json"))

    convert_rules(rules, conversion_dict, "output.css")