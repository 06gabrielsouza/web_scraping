import os
import requests
from bs4 import BeautifulSoup
import zipfile
from urllib.parse import urljoin
import io

# Baixar PDF em Memoria
def baixar_pdf_em_memoria(url):
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        return io.BytesIO(resposta.content)
    else:
        print(f"Erro ao baixar o arquivo: {url}")
        return None

# Encontrar Links
def encontrar_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if ('Anexo I' in link.text or 'Anexo II' in link.text) and href.endswith('.pdf'):
            full_url = urljoin(url, href)
            links.append(full_url)
    
    return links

# Criar Zip
def criar_zip(links_pdf, nome_zip):
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for link in links_pdf:
            pdf_content = baixar_pdf_em_memoria(link)
            if pdf_content:
                nome_arquivo = os.path.basename(link)
                zipf.writestr(nome_arquivo, pdf_content.getvalue())
                print(f"Adicionado ao ZIP: {nome_arquivo}")

# Função Principal Main
def main():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    nome_zip = "anexos_ans.zip"

    print("Procurando links para os Anexos I e II...")
    links_pdf = encontrar_links(url)

    if not links_pdf:
        print("Nenhum PDF encontrado com os termos especificados.")
        return

    print("\nCriando arquivo ZIP...")
    criar_zip(links_pdf, nome_zip)

    print(f"\nProcesso concluído! ZIP criado em: {os.path.abspath(nome_zip)}")

if __name__ == "__main__":
    main()