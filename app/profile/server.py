"""
Сервер-заглушка для локального просмотра страницы профиля.

Запуск из этой папки:
    python server.py

Откройте в браузере: http://127.0.0.1:5000/

Корень раздачи — папка app/, чтобы работали ссылки
на страницы обучения и карты в templates/.
"""

from __future__ import annotations

import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5000
APP_DIR = Path(__file__).resolve().parent.parent


class ProfileHandler(SimpleHTTPRequestHandler):
    """Раздаёт файлы из app/; / открывает профиль."""

    def do_GET(self) -> None:  # noqa: N802
        if self.path in ("/", "/index.html", "/profile", "/profile/"):
            self.path = "/profile/profile.html"
        super().do_GET()

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        print(f"[{self.log_date_time_string()}] {args[0]}")


def main() -> None:
    handler = partial(ProfileHandler, directory=str(APP_DIR))
    server = ThreadingHTTPServer((HOST, PORT), handler)
    url = f"http://{HOST}:{PORT}/"

    print(f"Папка: {APP_DIR}")
    print(f"Профиль: {url}")
    print("Остановка: Ctrl+C")

    try:
        webbrowser.open(url)
    except Exception:
        pass

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
