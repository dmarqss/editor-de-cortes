# editor-de-cortes
um editor de podcast para fazer cortes

usa a biblioteca moviepy para editar o videos

video_base = arquivo do podcast
short_base = um video com a resolução e o aspecto que sera usado de base para o novo

tempo_inicio,tempo_fim = tempo do corte, deve ser colocado em forma de horas segundo e minutos(00:00:00)

inicio,final = variaveis que contem videos que serão inseridos no inico e no final de cada corte

tipo_video = short(1) para cortes de ate 1 minuto e ficam na vertical, normal(2) para cortes na horizontal, sem limite de tempo e com vidos adcionais de inico e fim (inicio, fim)

