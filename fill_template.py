"""
Given a template and values, fill out the template with the values.
Ex: template = "{name} uses {product}? I use {product} too!"
    values = {"name": "Jabba", "product": "Sublime Text"}
"""

template = "{name} uses {product}? I use {product} too!"
values = {"name": "Jabba", "product": "Sublime Text"}

def fill_template(template, values):
    filled_string = ""
    marker = 0
    while marker < len(template):
        if template[marker] != "{":
            filled_string += template[marker]
            marker += 1
        else:
            marker_end = marker + 1
            while template[marker_end] != "}":
                marker_end += 1
            filled_string += values[template[(marker+1):marker_end]]
            marker = marker_end + 1
    return filled_string


print fill_template(template, values)