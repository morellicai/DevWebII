import list as ls
import blacklist as bl
from remover import remover_palavras
remover_palavras(ls.lista_palavras, bl.blacklist)
print(ls.lista_palavras)