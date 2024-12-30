from pypresence import Presence
import time
import signal
import sys

# Configuração do Rich Presence
def set_state_rpc():
    try:
        client_id = '1323029661826941092'  # ID da aplicação
        rpc = Presence(client_id)
        rpc.connect()

        # Configurar Rich Presence
        rpc.update(
            state="Virtual Programming Prodigy",  # Texto no status
            details="Fzd - Cpx do Alemão",  # Detalhes adicionais
            large_image="https://i.pinimg.com/originals/09/c8/f5/09c8f5e342f0c55f2909cc6d09ca0919.gif",  # URL da imagem grande
            large_text="Haha Network System",  # Texto adicional da imagem grande
            start=time.time(),  # Marca de início
            buttons=[
                {"label": "SNS", "url": "https://www.instagram.com/sonderboy7/"}  # Botão com URL
            ]
        )

        def clear_state_rpc(signal_received, frame):
            print("Encerrando Rich Presence...")
            rpc.clear()
            rpc.close()
            sys.exit(0)

        # Configuração para sair com segurança
        signal.signal(signal.SIGINT, clear_state_rpc)
        signal.signal(signal.SIGTERM, clear_state_rpc)

        print("Rich Presence configurado. Pressione Ctrl+C para sair.")
        while True:
            time.sleep(15)  # Manter o Rich Presence ativo

    except Exception as error:
        print("Erro ao configurar o Rich Presence:", error)

if __name__ == "__main__":
    set_state_rpc()
