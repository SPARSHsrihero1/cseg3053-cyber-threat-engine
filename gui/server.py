#!/usr/bin/env python3
"""
Cybersecurity Log Threat Detection Engine - SOC Web GUI Server
Pure Python standard library (Zero pip dependencies required).
"""

import http.server
import socketserver
import os
import sys
import json
import subprocess
import urllib.parse
import webbrowser

PORT = 8080
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUI_DIR = os.path.join(BASE_DIR, "gui")
BIN_ENGINE = os.path.join(BASE_DIR, "bin", "soc_engine.exe" if os.name == 'nt' else "soc_engine")
BIN_TESTS = os.path.join(BASE_DIR, "bin", "test_all.exe" if os.name == 'nt' else "test_all")
DATA_JSON = os.path.join(BASE_DIR, "data", "benchmark_results.json")
DATA_CSV = os.path.join(BASE_DIR, "data", "benchmark_results.csv")

class SOCHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=GUI_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == "/api/status":
            self.send_json_response({
                "status": "online",
                "engine_binary_exists": os.path.exists(BIN_ENGINE),
                "test_binary_exists": os.path.exists(BIN_TESTS),
                "base_dir": BASE_DIR,
                "os": os.name
            })
        elif path == "/api/benchmarks":
            if os.path.exists(DATA_JSON):
                with open(DATA_JSON, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        self.send_json_response({"success": True, "benchmarks": data})
                    except Exception as e:
                        self.send_json_response({"success": False, "error": str(e)}, 500)
            else:
                self.send_json_response({"success": False, "benchmarks": []})
        elif path == "/api/run":
            arg = query.get("target", ["--run-all-demos"])[0]
            valid_args = ["--run-all-demos", "--scenario1", "--scenario2", "--scenario3", "--unit2", "--unit3", "--unit4", "--unit5", "--unit6", "tests"]

            if arg == "tests":
                cmd = [BIN_TESTS]
            else:
                if arg not in valid_args:
                    arg = "--run-all-demos"
                cmd = [BIN_ENGINE, arg]

            try:
                proc = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, timeout=15)
                # Read latest benchmark if updated
                benchmarks = []
                if os.path.exists(DATA_JSON):
                    with open(DATA_JSON, "r", encoding="utf-8") as f:
                        try:
                            benchmarks = json.load(f)
                        except Exception:
                            pass

                self.send_json_response({
                    "success": proc.returncode == 0,
                    "returncode": proc.returncode,
                    "stdout": proc.stdout,
                    "stderr": proc.stderr,
                    "benchmarks": benchmarks
                })
            except Exception as e:
                self.send_json_response({"success": False, "error": str(e)}, 500)
        else:
            super().do_GET()

    def send_json_response(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

def run_server():
    os.chdir(BASE_DIR)
    # Ensure binary exists or compile if missing
    if not os.path.exists(BIN_ENGINE) or not os.path.exists(BIN_TESTS):
        print("[*] Binaries not found, compiling via GCC...")
        srcs = [
            "src/core/metrics.c", "src/core/data_generator.c",
            "src/unit2_divide_conquer.c", "src/unit3_greedy.c",
            "src/unit4_dp.c", "src/unit5_backtracking_bb.c",
            "src/unit6_flow_string_crt.c"
        ]
        os.makedirs(os.path.join(BASE_DIR, "bin"), exist_ok=True)
        subprocess.run(["gcc", "-std=c17", "-Wall", "-Wextra", "-O2", "-Iinclude"] + srcs + ["src/main.c", "-o", BIN_ENGINE], check=True)
        subprocess.run(["gcc", "-std=c17", "-Wall", "-Wextra", "-O2", "-Iinclude"] + srcs + ["tests/test_all.c", "-o", BIN_TESTS], check=True)

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), SOCHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n========================================================")
        print(f" CSEG3053 CYBERSECURITY THREAT ENGINE - SOC GUI CONSOLE")
        print(f"========================================================")
        print(f" Server active at : {url}")
        print(f" GUI root dir     : {GUI_DIR}")
        print(f" Press Ctrl+C to terminate.")
        print(f"========================================================\n")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down SOC GUI server.")

if __name__ == "__main__":
    run_server()
