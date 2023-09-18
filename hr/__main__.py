import argparse
import logging
import sys

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
        "-p", "--as-paragraph",
        help="print two horizontal rules, BEGIN and END",
        action="store_true"
    )
    style_properties = parser.add_argument_group("style proprties")
    style_properties.add_argument(
        "-i", "--inner",
        help="inner character (default: -)",
        metavar="STR",
        type=lambda s: s.strip()[0],
        default="-"
    )
    style_properties.add_argument(
        "-l", "--length",
        help="total character length (default: 80)",
        metavar="INT",
        type=int,
        default=80
    )
    style_properties.add_argument(
        "-o", "--outer",
        help="outer character(s) (default: #)",
        metavar="STR",
        type=lambda s: s.strip(),
        default="#"
    )
    return parser.parse_args()


def configure_logging() -> None:
    logging.basicConfig(format="[%(levelname)s] %(message)s")
    return None


def main() -> None:
    args = parse_args()
    configure_logging()
    try:
        if args.as_paragraph:
            lib.print_as_paragraph(args.length, args.outer, args.inner, args.title)
        elif args.title:
            lib.print_titled(args.length, args.outer, args.inner, args.title)
        else:
            lib.print_untitled(args.length, args.outer, args.inner)
    except lib.LengthError as e:
        logging.error(str(e))
        sys.exit(1)
    return None


if __name__ == "__main__":
    main()
