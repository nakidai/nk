partial = __import__("functools").partial
repeat = __import__("itertools").repeat
starmap = __import__("itertools").starmap
res = next(
    filter(
        bool,
        starmap(
            partial(
                eval,
                '{'
                '    "": partial(exec, "exit(0)"),'
                '    "x": partial(eval, "\'x\'"),'
                '    "o": partial(eval, "\'o\'"),'
                '}.get(input("x/o? "), type({}.get(0)))()'
            ),
            repeat(())
        ),
    ),
    False,
)
print(res)
