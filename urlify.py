def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")