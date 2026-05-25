def my_decorator(fx):
    def main(*args):
        print("Before calling the function")
        response = fx(*args)
        print("After calling the function")
        return response
    return main

@my_decorator
def fetch_data(url:str,path:str):
    return f"Fetching data from {url} and saving to {path} ..."

response=fetch_data("https://api.example.com/data","/tmp/data.json")
print(response)