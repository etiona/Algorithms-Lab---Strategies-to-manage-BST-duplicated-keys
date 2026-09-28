import subprocess
import sys


def run(script_name):
    print(f"\n===== Esecuzione di {script_name} =====\n")

    result = subprocess.run(
        [sys.executable, script_name]
    )

    if result.returncode != 0:
        print(f"Errore durante l'esecuzione di {script_name}")
        sys.exit(result.returncode)


def main():

    run("benchmark.py")
    run("plots.py")
    run("plots_height.py")

    print("\n===================================")
    print("Benchmark completato.")
    print("Grafici generati con successo.")
    print("===================================")


if __name__ == "__main__":
    main()