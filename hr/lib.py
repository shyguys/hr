def print_paragraph(
    length: int,
    outer: str,
    inner: str,
    title: str | None = None
) -> None:
    if title is None:
        begin, end = "BEGIN", "END"
    else:
        begin, end = f"BEGIN {title}", f"END {title}"
    print_titled(length, outer, inner, begin)
    print_titled(length, outer, inner, end)
    return None


def print_titled(length: int, outer: str, inner: str, title: str) -> None:
    spare_len = length - len(outer)*2 - len(title) - 4
    if spare_len < 2:
        raise ValueError(f"Length insufficient, {2-spare_len} more required.")
    rspare_len = spare_len // 2
    lspare_len = spare_len - rspare_len
    print(f"{outer} {inner*lspare_len} {title} {inner*rspare_len} {outer}")
    return None


def print_untitled(length: int, outer: str, inner: str) -> None:
    spare_len = length - len(outer)*2 - 2
    if spare_len < 1:
        raise ValueError(f"Length insufficient, {1-spare_len} more required.")
    print(f"{outer} {inner*spare_len} {outer}")
    return None
