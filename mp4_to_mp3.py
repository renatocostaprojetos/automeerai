# Importa o módulo necessário do moviepy para manipulação de áudio e vídeo
from moviepy.editor import AudioFileClip

# Importa o módulo uuid para gerar identificadores únicos
import uuid

# Define uma função chamada 'mp4_to_mp3' que converte um arquivo MP4 em formato MP3
def mp4_to_mp3(mp4, mp3):
    try:
        # Cria um objeto de áudio a partir do arquivo MP4 utilizando a classe AudioFileClip
        filetoconvert = AudioFileClip(mp4)

        # Grava o áudio extraído do arquivo MP4 em formato MP3
        filetoconvert.write_audiofile(mp3)

        # Fecha o objeto de áudio para liberar recursos do sistema
        filetoconvert.close()

    except FileNotFoundError:
        # Esta exceção é capturada caso o arquivo MP4 não seja encontrado
        print(f"Erro: O arquivo MP4 '{mp4}' não foi encontrado.")

    except Exception as e:
        # Captura qualquer outra exceção e imprime a mensagem de erro
        print(f"Ocorreu um erro durante a conversão: {e}")





# Verifica se o script está sendo executado como o programa principal
if __name__ == "__main__":
    # Define o caminho do arquivo MP4 local que será convertido
    mp4_local_filename = "entrevista de Boechat com Jô Soares_curta.mp4"

    # Gera um nome de arquivo único para o arquivo MP3 usando uuid para evitar colisões de nome
    mp3_local_filename = f"{uuid.uuid4().hex}.mp3"

    # Chama a função para converter o arquivo MP4 em MP3
    mp4_to_mp3(mp4_local_filename, mp3_local_filename)



