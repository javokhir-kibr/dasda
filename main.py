"""
Project Aurora — Application Entrypoint & Server Launcher.
Compatible with standard Web Hosting (Render, Railway, Fly.io, Heroku, Docker)
and native Windows / Linux execution.
"""
import os
import sys
import time
import argparse
import threading
import webbrowser
import uvicorn

# Re-export FastAPI app for ASGI web publishers (e.g., "uvicorn main:app")
from aurora.api import app
from aurora.config import PORT, HOST

def open_browser_delayed(url: str, delay: float = 1.2):
    """Opens the local browser in a background thread after server starts."""
    def _target():
        time.sleep(delay)
        print(f"\n[Browser] Launching browser to {url} ...")
        try:
            webbrowser.open_new_tab(url)
        except Exception as e:
            print(f"[Browser] Note: Could not auto-launch browser ({e}). Open {url} manually.")
    
    t = threading.Thread(target=_target, daemon=True)
    t.start()


def main():
    parser = argparse.ArgumentParser(description="Project Aurora: Autonomous Agritech Vision Engine")
    parser.add_argument("--host", type=str, default=None, help=f"Host address to bind (default: {HOST})")
    parser.add_argument("--port", type=int, default=None, help=f"Port number to bind (default: {PORT})")
    parser.add_argument("--reload", action="store_true", help="Enable uvicorn hot reloading for development")
    parser.add_argument("--open-browser", action="store_true", help="Automatically launch default web browser")
    parser.add_argument("--no-browser", action="store_true", help="Prevent auto-launching web browser")
    
    args = parser.parse_args()

    # Environment variables take precedence if CLI flags not explicitly passed
    target_host = args.host or os.getenv("HOST") or HOST
    
    # Handle PORT dynamic variable passed by web hosting platforms (Render, Heroku, Cloud Run, etc.)
    env_port = os.getenv("PORT")
    target_port = args.port or (int(env_port) if env_port else PORT)

    is_windows = sys.platform.startswith("win")
    
    # Determine if browser should be opened
    should_open_browser = False
    if args.open_browser:
        should_open_browser = True
    elif not args.no_browser and is_windows and not os.getenv("PORT") and not os.getenv("CI") and not os.getenv("DOCKER"):
        # By default on Windows desktop interactive mode, open browser
        should_open_browser = True

    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    display_host = "localhost" if target_host in ("0.0.0.0", "127.0.0.1", "") else target_host
    local_url = f"http://{display_host}:{target_port}"

    print("=" * 62)
    print("      PROJECT AURORA -- AUTONOMOUS AGRITECH VISION ENGINE   ")
    print("=" * 62)
    print(f" * Platform Mode:  {'Windows Local Mode' if is_windows else 'Production Web / Linux Mode'}")
    print(f" * Local URL:      {local_url}")
    print(f" * Network Host:   {target_host}:{target_port}")
    print(f" * Hot Reload:     {'Enabled' if args.reload else 'Disabled'}")
    print(f" * Web Publishing: Ready (Render / Railway / Docker / Cloud Run)")
    print("=" * 62 + "\n")

    if should_open_browser:
        open_browser_delayed(local_url)

    try:
        uvicorn.run(
            "main:app",
            host=target_host,
            port=target_port,
            reload=args.reload
        )
    except KeyboardInterrupt:
        print("\n[Project Aurora] Server stopped gracefully by user.")


if __name__ == "__main__":
    main()
