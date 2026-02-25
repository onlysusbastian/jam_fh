import subprocess


def run_cmd(cmd):
    print(f"[exec] {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def apply_target(target):
    current_sink, current_source = get_current_defaults()

    if current_sink == target.sink_name and current_source == target.source_name:
        print("[audioroute] already active — skipping")
        return

    if target.sink_id is not None:
        run_cmd(["wpctl", "set-default", str(target.sink_id)])

    if target.source_id is not None:
        run_cmd(["wpctl", "set-default", str(target.source_id)])

import json

def get_current_defaults():
    result = subprocess.run(
        ["pw-dump"],
        capture_output=True,
        text=True,
        check=True
    )

    data = json.loads(result.stdout)

    sink = None
    source = None

    for obj in data:
        if obj.get("type") != "PipeWire:Interface:Metadata":
            continue

        for item in obj.get("metadata", []):
            key = item.get("key")

            if key == "default.audio.sink":
                sink = item["value"]["name"]

            if key == "default.audio.source":
                source = item["value"]["name"]

    return sink, source
