"""Menu principal do Projeto 6 - DTMF."""

from emissor import executar_emissor
from receptor import executar_receptor


def main() -> None:
    while True:
        print("\n=== PROJETO 6 - DTMF ===")
        print("1 - Emissor")
        print("2 - Receptor")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            executar_emissor()
        elif opcao == "2":
            executar_receptor()
        elif opcao == "0":
            print("Programa encerrado.")
            return
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
