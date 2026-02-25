import sys

from discovery import discover_nodes
from scoring import score_nodes
from selector import select_targets
from executor import apply_target


def main():
    # default mode
    mode = "auto"

    if len(sys.argv) > 1:
        mode = sys.argv[1]

    print(f"[audioroute] mode = {mode}")

    nodes = discover_nodes()
    scores = score_nodes(nodes)
    target = select_targets(scores, mode=mode)

    print(f"[audioroute] target = {target}")

    apply_target(target)


if __name__ == "__main__":
    main()
