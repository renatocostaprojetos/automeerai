from moviepy.editor import AudioFileClip
import uuid

def mp4_to_mp3(mp4_filename, mp3_filename):

    afc = AudioFileClip(mp4_filename)
    afc.write_audiofile(mp3_filename)
    afc.close()

if __name__=="__main__":
   
   mp4_filename= "C:/GitHub/automeerai/Video/entrevista de Boechat com Jô Soares curto.mp4"
   mp3_filename= "C:/GitHub/automeerai/Video/"+ uuid.uuid4().hex +".mp3"
   mp4_to_mp3(mp4_filename,mp3_filename)


