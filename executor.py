import subprocess


def run_cmd(cmd):
    print(f"[exec] {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def apply_target(target):
    # Apply sink default
    if target.sink_id is not None:
        run_cmd(["wpctl", "set-default", str(target.sink_id)])

    # Apply source default
    if target.source_id is not None:
        run_cmd(["wpctl", "set-default", str(target.source_id)])


