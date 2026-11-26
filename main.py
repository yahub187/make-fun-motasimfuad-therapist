import os

ENTRY_FILENAME = "entry.txt"
ENTRY_TEXT = "Diagnosis: you apologize to furniture when you bump into it. Prognosis: excellent manners, untreated self-worth."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
