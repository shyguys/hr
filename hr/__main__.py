import argparse

from hr import lib


class CustomFormatter(argparse.RawTextHelpFormatter):
    def _format_action_invocation(self, action) -> str:
        """Only show metavar for long options."""
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default_metavar = self._get_default_metavar_for_optional(action)
        formatted_args = self._format_args(action, default_metavar)
        return ', '.join(action.option_strings) + ' ' + formatted_args


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
    parser.add_argument(
        "title",
        help="title to insert in center",
        nargs="?",
    )
    parser.add_argument(
        "-l", "--length",
        help="total character length (default: 80)",
        metavar="INT",
        type=int,
        default=80
    )
    parser.add_argument(
        "-o", "--outer",
        help="outer character(s) (default: #)",
        metavar="STR",
        default="#"
    )
    parser.add_argument(
        "-i", "--inner",
        help="inner character (default: -)",
        metavar="CHAR",
        type=lambda c: c[0],
        default="-"
    )
    parser.add_argument(
        "-p", "--as-paragraph",
        help="as paragraph, BEGIN and END",
        action="store_true"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.as_paragraph:
        lib.print_paragraph(args.length, args.outer, args.inner, args.title)
        return None
    if args.title:
        lib.print_titled(args.length, args.outer, args.inner, args.title)
        return None
    lib.print_untitled(args.length, args.outer, args.inner)
    return None


if __name__ == "__main__":
    main()
