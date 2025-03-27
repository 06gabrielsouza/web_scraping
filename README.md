# **Web Scraper para Anexos da ANS**

## **📝 Descrição**
Script Python que:
- Acessa o site da ANS ([link](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos))
- Baixa automaticamente os Anexos I e II em PDF
- Gera um arquivo `anexos_ans.zip` localmente
- **Tudo em memória** (sem arquivos temporários)

## **⚡ Como Usar**

1. **Instale as dependências** (execute no terminal):
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Baixe o script**:
   - Copie o código do `ans_scraper.py`

3. **Execute** (no terminal/prompt de comando):
   ```bash
   python ans_scraper.py
   ```

4. **Resultado**:
   ```
   Procurando links para os Anexos I e II
   Adicionado ao ZIP: anexo-i.pdf
   Adicionado ao ZIP: anexo-ii.pdf
   
   Processo concluído! ZIP criado em: C:\caminho\atual\anexos_ans.zip
   ```

## **🔄 Atualizações Futuras**
1. Se o site mudar:
   - Atualize os critérios de busca na função `encontrar_links()`
   ```python
   if ('Novo Nome Anexo 1' in link.text or 'Novo Nome Anexo 2' in link.text) and href.endswith('.pdf'):
   ```

## **📂 Estrutura do Projeto**
```
ans_scraper.py          # Script principal
anexos_ans.zip          # Arquivo gerado (após execução)
```

## **❓ Problemas Comuns**
- **Links não encontrados**: O site pode ter atualizado seu layout
- **Erros de conexão**: Verifique sua internet ou aumente o timeout:
  ```python
  resposta = requests.get(url, timeout=15)
    # em baixar_pdf_em_memoria()
  ```
.