# constants
MARKER_SIZE = 20  # points size when plotting
LINES_MARKER = "b-"       # lines shape and color when plotting


def get_vector_elements(cordi_vector: tuple) -> list:
    elements = ()
    for curr_cordi in cordi_vector:
        elements = elements + (curr_cordi,)
    return elements
