import sys

from .discovery import discover_nodes
from .scoring import score_nodes
from .selector import select_targets
from .executor import apply_target


def run(mode="auto", scope="both"):
    """
    Core routing function used by both CLI and UI
    """

    if scope not in ["sink", "source", "both"]:
        raise ValueError("scope must be sink, source, or both")

    print(f"[audioroute] mode = {mode}")

    nodes = discover_nodes()
    scores = score_nodes(nodes)
    target = select_targets(scores, mode=mode, scope=scope)

    print(f"[audioroute] target = {target}")

    apply_target(target)

    return target


def main():
    """
    CLI entrypoint
    """

    mode = "auto"
    scope = "both"

    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if len(sys.argv) > 2:
        scope = sys.argv[2]

    run(mode, scope)


if __name__ == "__main__":
    main()
