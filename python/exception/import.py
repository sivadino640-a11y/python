try:
    import keyword
    print(keyword.kwlist)
except ImportError:
    print("Error")