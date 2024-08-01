

class ScriptError(Exception):
    """Base class for exceptions in this module."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class InvalidAPIResponse(ScriptError):
    """Exception raised for invalid API responses."""
    
    def __init__(self, message):
        super().__init__(message)


class InvalidToken(ScriptError):
    """Exception raised for invalid tokens."""
    
    def __init__(self, message="Du må oppgi din X-CSRF-TOKEN. Se README.md for mer informasjon."):
        super().__init__(message)


class FunctionNotSpecified(ScriptError):
    """Exception raised for when no function is specified."""
    
    def __init__(self, message="Du må oppgi en funksjon å kjøre."):
        super().__init__(message)


class InvalidFunction(ScriptError):
    """Exception raised for invalid functions."""
    
    def __init__(self, message="Denne funksjonen er ikke støttet."):
        super().__init__(message)


class InvalidFileFormat(ScriptError):
    """Exception raised for invalid file formats."""
    
    def __init__(self, message="Denne filtypen er ikke støttet."):
        super().__init__(message)


class FileNotFound(ScriptError):
    """Exception raised for when a file is not found."""
    
    def __init__(self, message="Kunne ikke finne filen."):
        super().__init__(message)


class DirectoryNotFound(ScriptError):
    """Exception raised for when a directory is not found."""
    
    def __init__(self, message="Kunne ikke finne mappen."):
        super().__init__(message)