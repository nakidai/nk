partial = __import__("functools").partial
repeat = __import__("itertools").repeat
starmap = __import__("itertools").starmap
function_builder = type(__import__("timeit").timeit)


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
                            '}.get(input("x/o? "), type({}.get(0)))()'
                        ),
                        repeat(())
                    ),
                ),
                False,
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
                side.switch()
            """
        ),
        repeat((), 5),
    )
)
