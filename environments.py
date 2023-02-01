def environmentsVariables(variableName:str) -> str:
    import os
    from dotenv import load
    load()
    return os.getenv(variableName)


