class Message:

    @static
    def message(self, type: str, message: str) -> void:
        method_name = '_' + str(type)
        method = getattr(self, method_name, lambda: "Invalid message type")

        return method(message)


    def __error(self):
        termcolor.cprint(str(error), 'red')
        sys.exit(1)

    def __warning(self):
        termcolor.cprint(str(error), 'yellow')

    def __success(self):
        termcolor.cprint(str(error), 'green')

    def __info(self):
        termcolor.cprint(str(error), 'grey')

    def __generic(self):
        termcolor.cprint(str(error))



#
#
#     def msg_msg(self, type):
#         case
#         "${1:-}" in
#         --e | --error)
#         icon = "${COMMITLINT_ICON_ERROR}"
#         color = "${COMMITLINT_COLOR_RED}" \
#         ;;
#         --w | --warning)
#         icon = "${COMMITLINT_ICON_WARNING}"
#         color = "${COMMITLINT_COLOR_YELLOW}" \
#         ;;
#         --s | --success)
#         icon = "${COMMITLINT_ICON_SUCCESS}"
#         color = "${COMMITLINT_COLOR_GREEN}" \
#         ;;
#         --i | --info)
#         icon = "${COMMITLINT_ICON_INFO}"
#         color = "${COMMITLINT_COLOR_GREY}" \
#         ;;
#         --g | --generic)
#         icon = "${COMMITLINT_ICON_HOURGLASS}"
#         color = "" \
#         ;;
#         --h | --help)
#         echo
#         "HELP${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--e|--error${COMMITLINT_TB}Print error message${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--w|--warning${COMMITLINT_TB}Print warning message${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--s|--success${COMMITLINT_TB}Print success message${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--i|--info${COMMITLINT_TB}Print info message${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--g|--generic${COMMITLINT_TB}Print generic message${COMMITLINT_BR}" \
#         "${COMMITLINT_SP4}--h|--help${COMMITLINT_TB2}Print this help${COMMITLINT_BR}"
#         return
#         ;;
#         * )
#         echo
#         "${COMMITLINT_SP4}${COMMITLINT_SP}${1:-}"
#         return
#         ;;
#
#     esac
#
#     if ["${2:-}" != ""];then
#     echo - e
#     "${color:-}${icon:-}${COMMITLINT_SP4}${2:-}${COMMITLINT_FONT_RESTORE}"
#
#
# fi
