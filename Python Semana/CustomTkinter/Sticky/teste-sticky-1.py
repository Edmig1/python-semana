from modulo import *
janela = criarjanela('Janela','600x600',1)

frame = criar_frame(janela, 400,100,0,0)
frame.grid(sticky="N", columnspan=12)
aba = criar_aba(janela,200,200,6,6,'Pedro','Julio')
janela.mainloop()