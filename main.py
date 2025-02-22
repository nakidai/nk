partial = __import__("functools").partial
repeat = __import__("itertools").repeat
starmap = __import__("itertools").starmap

function_builder = type(__import__("timeit").timeit)
nothing = type({}.get(0))
true = bool(1)
false = bool(0)
none = nothing()


create_namespace = partial(
    function_builder,
    compile('', '', 'exec'),
    {}
)


Side = partial(eval, """
(
    self := create_namespace(),
    exec(
        '''if 1:
            self.choose = partial(
                next,
                filter(
                    bool,
                    starmap(
                        partial(
                            eval,
                            '{'
                            '    "": partial(exec, "exit(0)"),'
                            '    "x": partial(eval, "\\\\'x\\\\'"),'
                            '    "o": partial(eval, "\\\\'o\\\\'"),'
                            '}.get(input("x/o? "), nothing)()'
                        ),
                        repeat(())
                    ),
                ),
                false,
            )

            self.str = self.choose()

            self.switch = partial(
                exec,
                'self.str = {"x": "o", "o": "x"}.get(self.str)',
                locals={"self": self},
            )
        '''
    ),
    self,
)[-1]
""")


Board = partial(eval, """
(
    self := create_namespace(),
    exec(
        '''if 1:
            self.field = [
                ['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_'],
            ]

            self.str = partial(
                eval,
                "'\\\\\\\\n'.join(map(''.join, self.field))",
                locals={"self": self},
            )

            self.get_cell = partial(
                next,
                filter(
                    bool,
                    starmap(
                        partial(
                            eval,
                            '{'
                            '    false: partial(eval, "none"),'
                            '    true: partial(eval, "res"),'
                            '}.get('
                            '    range(1, 10).__contains__('
                            '       res := {'
                            '            false: partial(eval, "-1"),'
                            '            true: partial(eval, "int(inp)")'
                            '        }.get('
                            '            (inp := input("? ")).isdigit()'
                            '        )(locals={"inp": inp})'
                            '    )'
                            ')(locals={"res": res})'
                        ),
                        repeat(())
                    ),
                ),
                false
            )
        '''
    ),
    self,
)[-1]
""")


side = Side()
print("you've chosen", side.str)

board = Board()

any(
    starmap(
        partial(
            exec,
            """if 1:
                print(f"{side.str}\\n{board.str()}")

                cell = board.get_cell() - 1
                {
                    false: partial(exec, "board.field[cell // 3][cell % 3] = side.str"),
                    true: partial(exec, "print('uhh behavior in this situation is not implemented yet'); exit(1)"),
                }.get("xo".__contains__(board.field[cell // 3][cell % 3]))()

                side.switch()
            """
        ),
        repeat(()),
    )
)
