from colorama import Fore

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"{Fore.RED}Error: Contact not found. {str(e)}"
        except ValueError as e:
            return (f"{Fore.RED}Error: Invalid input. "
                    f"{str(e)}")
        except IndexError as e:
            return (f"{Fore.RED}Error: Missing required arguments. "
                    f"Please provide all necessary inputs. {str(e)}")
        except Exception as e:
            return f"{Fore.RED}An unexpected error occurred: {str(e)}"
    return inner