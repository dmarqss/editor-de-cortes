from moviepy.editor import *

while True:
    video_base =  'D:/mais q1/script/podcast/' + input('diretorio do video: ') + '.mp4'

    tempo_inicio = (input('tempo do corte inicial (00:00:00): '))
    tempo_inicio = tempo_inicio.split(':')
    tempo_inicio = int(tempo_inicio[0]) * 3600 + int(tempo_inicio[1]) * 60 + int(tempo_inicio[2])

    tempo_fim = (input('tempo do corte final (00:00:00): '))
    tempo_fim = tempo_fim.split(':')
    tempo_fim = int(tempo_fim[0]) * 3600 + int(tempo_fim[1]) * 60 + int(tempo_fim[2])

    nome_final = input('nome final do aquivo: ')
    tipo_video = int(input('formato SHORT(1) | NORMAL(2) '))

    inicio = VideoFileClip("D:/mais q1/script/videos/inicio_q1.mp4").set_fps(24).resize(height =720)
    
    final = VideoFileClip("D:/mais q1/script/videos/final_q1.mp4").set_fps(24)


    
    if tipo_video == 2:
        corte = VideoFileClip(video_base).subclip(tempo_inicio,tempo_fim).fadein(2).fadeout(2).set_fps(24)

        video_pronto = concatenate_videoclips([inicio,corte,final], method="compose")
        video_pronto.write_videofile('D:/mais q1/script/cortes/' + nome_final + ".mp4", threads = 8, fps=24)

        print(f'corte {nome_final}.mp4 feito com sucesso')

    elif tipo_video == 1:
        corte = VideoFileClip(video_base).subclip(tempo_inicio,tempo_fim).set_fps(24)

        nome_final = 'SHORT-' + nome_final
        short_base = VideoFileClip('D:/mais q1/script/videos/short.mp4').set_duration(corte.duration).without_audio()
        corte = corte.set_position((0,647)).resize(0.9)

        juntar = CompositeVideoClip([short_base, corte],)
        juntar.write_videofile('D:/mais q1/script/cortes/' + nome_final + ".mp4", threads = 8, fps=24)
        print(f'short {nome_final}.mp4 feito com sucesso')

    fim = input('deseja continuar? s/n: ')
    if fim == 'n':
        break
    else:
        print('\n' * 60)

