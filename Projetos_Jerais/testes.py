# Códigos ANSI
FUNDO_AMARELO = "\033[43m"
TEXTO_PRETO = "\033[30m"
LIMPA_LINHA = "\033[K"
RESET = "\033[0m"

# Destacando a linha toda
print(f"{FUNDO_AMARELO}{TEXTO_PRETO}Esta linha está totalmente destacada!{LIMPA_LINHA}{RESET}")
print("Esta é uma linha normal abaixo.")
