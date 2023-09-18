class LengthError(Exception):
    def __init__(self, more_required: int, *args: object) -> None:
        super().__init__(*args)
        self.more_required = more_required

    def __str__(self) -> str:
        return f"length insufficient, {self.more_required} more required"


def print_as_paragraph(length: int, outer: str, inner: str, title: str | None = None) -> None:
    if title is None:
        begin, end = "BEGIN", "END"
    else:
        begin, end = f"BEGIN {title}", f"END {title}"
    print_titled(length, outer, inner, begin)
    print_titled(length, outer, inner, end)
    return None


def print_titled(length: int, outer: str, inner: str, title: str) -> None:
    spare_length = length - len(outer)*2 - len(title) - 4
    if spare_length < 2:
        raise LengthError(2-spare_length)
    right_spare_length = spare_length // 2
    left_spare_length = spare_length - right_spare_length
    print(f"{outer} {inner*left_spare_length} {title} {inner*right_spare_length} {outer}")
    return None


def print_untitled(length: int, outer: str, inner: str) -> None:
    spare_len = length - len(outer)*2 - 2
    if spare_len < 1:
        raise LengthError(1-spare_len)
    print(f"{outer} {inner*spare_len} {outer}")
    return None
