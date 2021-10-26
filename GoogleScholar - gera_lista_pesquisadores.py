import dsd

# proximo_href = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=direito+OR+label%3Adireito+OR+label%3Adireito_constitucional+OR+label%3Afilosofia_do_direito+OR+label%3Adireito_tributario+OR+label%3Adireito_publico+OR+label%3Adireito_penal'

proximo_href = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=direito+OR+label%3Adireito+OR+label%3Adireito_constitucional+OR+label%3Afilosofia_do_direito+OR+label%3Adireito_tributario+OR+label%3Adireito_publico+OR+label%3Adireito_penal&after_author=S_aWANX___8J&astart=0'
html = dsd.get(proximo_href)

lista_paginas = []
lista_total = []
total_citacoes = '2'
bottom = False

# dsd.limpar_arquivo('pesquisadores.txt')
# dsd.write_csv_header('pesquisadores.txt', 'nome, user, href, affiliation, labels, total_citacoes, citacoes_total, citacoes_desde_2016, i10_total, i10_desde_2016, hindex_total, hindex_desde_2016')
dsd.limpar_arquivo('labels.txt')
labels_total = []
parar = False
contagem = 0
    
for n in range (2000):
    lista_paginas.append(proximo_href)
    
    pesquisadores = dsd.extrair(html,'class="gsc_1usr"','')
    pesquisadores_split = pesquisadores.split('id="gsc_authors_bottom_pag" class="gs_scl">')
    bottom = pesquisadores_split[1]
    pesquisadores = pesquisadores_split[0]

        
    lista_pesquisadores = pesquisadores.split('class="gsc_1usr"')

    if parar == True:
        break
    
    for item in lista_pesquisadores:
        contagem = contagem+1
    
        pesquisador = item.split('<div')
        
        nome = dsd.extrair(pesquisador[1],'alt="','"')
        
        if nome == 'Andrye Alves Rios' and n > 1:
            parar = True
            break
        
        href = 'https://scholar.google.com' + dsd.extrair(pesquisador[1],'href="','"')
        href = href.replace('amp;','')
        
        user = dsd.extrair(href,'user=','')
    
        affiliation = dsd.extrair(pesquisador[3],'class="gs_ai_aff">','</div>')
        affiliation = affiliation.replace("<span class='gs_hlt'>", '')
        affiliation = affiliation.replace("</span>", '')
        
        total_citacoes = dsd.extrair(pesquisador[5],'Cited by ','<')
        print (str(contagem) + '  ' + nome + '  ' + total_citacoes)
        
        pesquisador[6] = dsd.extrair(pesquisador[6],'label:','')
        
        label = pesquisador[6].split('label:')
        
        labels = []
        
        for a in range(len(label)):
            label[a] = label[a].replace('</span>','')
            label[a] = label[a].replace("<span class='gs_hlt'>",'')
            
            label[a] = dsd.extrair(label[a],'>','<')
            
            labels.append(label[a])
            labels_total.append(label[a].upper())
            dsd.write_csv_row('labels.txt',[label[a].upper()])
            
        indices = dsd.get(href)
        citacoes = dsd.extrair(indices,'Citations</a></td><td class="gsc_rsb_std">','</td></tr><tr><td class="gsc_rsb_sc1">')
        citacoes = citacoes.split('</td><td class="gsc_rsb_std">')
            
        citacoes_total = citacoes[0]
        citacoes_desde_2016 = citacoes[1]
        
        hindex = dsd.extrair(indices,'">h-index</a></td><td class="gsc_rsb_std">','</td></tr><tr><td class="gsc_rsb_sc1">')
        hindex = hindex.split('</td><td class="gsc_rsb_std">')
        hindex_total = hindex[0]
        hindex_desde_2016 = hindex[1]
        
        i10 = dsd.extrair(indices,'">i10-index</a></td><td class="gsc_rsb_std">','</td></tr></tbody>')
        i10 = i10.split('</td><td class="gsc_rsb_std">')
        i10_total = i10[0]
        i10_desde_2016 = i10[1]
        

    
        dados = [nome, user, href, affiliation, labels, total_citacoes, citacoes_total, citacoes_desde_2016, i10_total,i10_desde_2016, hindex_total, hindex_desde_2016]
        
        dsd.write_csv_row('pesquisadores.txt',dados)

        

        

    proximo = dsd.extrair(bottom,'after_author\\x3d','\\')
    proximoext = dsd.extrair(bottom,'start\\x3d',"'")
    proximo_href = 'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=direito+OR+label%3Adireito+OR+label%3Adireito_constitucional+OR+label%3Afilosofia_do_direito+OR+label%3Adireito_tributario+OR+label%3Adireito_publico+OR+label%3Adireito_penal&after_author=' + proximo + '&astart=' + proximoext

    html = dsd.get(proximo_href)

    
labels_total.sort()



    


