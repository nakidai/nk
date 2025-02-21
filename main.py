partial = __import__("functools").partial
repeat = __import__("itertools").repeat
starmap = __import__("itertools").starmap
res = {}.get(0)
any(
    starmap(
        partial(eval, """
{
    "": partial(exec, "exit(0)"),
    "x": partial(eval, "bool(res := 'x')"),
    "o": partial(eval, "bool(res := 'o')"),
}.get(input("x/o? "), type({}.get(0)))()
"""),
        repeat(())
    ),
)
print(res)
