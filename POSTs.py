import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def main():
    try:
        with urlopen("https://jsonplaceholder.typicode.com/posts", timeout=10) as response:
            posts = json.load(response)

        for number, post in enumerate(posts[:5], start=1):
            print(f"{number}. {post['title']}")
            print(post["body"])
            print()
    except HTTPError as error:
        print(f"JSONPlaceholder вернул ошибку HTTP {error.code}.")
        return 1
    except (URLError, TimeoutError):
        print("Не удалось подключиться к JSONPlaceholder.")
        return 1
    except (ValueError, KeyError, TypeError):
        print("JSONPlaceholder вернул данные в неожиданном формате.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
