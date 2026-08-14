try:
    import abcmodule
    print(abcmodule)
except ModuleNotFoundError:
    print("module not found")
