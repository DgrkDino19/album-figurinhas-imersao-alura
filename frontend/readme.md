# 🏆 Alura Album - Copa do Mundo Tech

Um álbum de figurinhas digital interativo e responsivo que celebra os maiores nomes e marcos da tecnologia. O projeto simula a experiência física de folhear um álbum real, integrando-se dinamicamente a uma API para expor e carregar as figurinhas.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é fornecer uma interface rica, dinâmica e visualmente deslumbrante que simula a experiência de colecionar figurinhas físicas de grandes personalidades da tecnologia (divididos em categorias como Inteligência Artificial, Python e Bancos de Dados). Ele demonstra conceitos modernos de desenvolvimento web como:
* Efeitos de transição 3D realistas baseados em física de páginas.
* Consumo assíncrono de APIs REST para carregamento dinâmico de mídia.
* Estilização moderna avançada com CSS Vanilla (variáveis, gradientes sofisticados, sombras dinâmicas e efeitos *glitch*).

---

## 🛠️ Tecnologias Utilizadas

* **HTML5**: Estruturação semântica de todo o livro e seus slots de figurinhas.
* **CSS3 (Vanilla)**: Design premium com variáveis CSS, suporte a temas escuros, transições suaves, efeitos de luz (*glow*) e efeitos tridimensionais.
* **JavaScript (ES6+)**: Controle de comportamento da página, manipulação do DOM e integrações assíncronas (Fetch API).
* **St.PageFlip**: Biblioteca Javascript especializada no efeito de folheamento realista de livros e revistas.

---

## 📂 Arquivos do Projeto e Funcionalidades

### 1. 📄 [index.html](index.html)
* **Objetivo:** Define o esqueleto e a estrutura física do álbum.
* **Funcionalidades:**
  * Define a estrutura de páginas esquerda/direita e a capa do álbum usando marcação semântica.
  * Estrutura a grade de slots de figurinhas (`.stickers-grid`) identificando cada figura pelo seu ID numérico (ex: `#01` para Alan Turing).
  * Cria botões interativos para avançar/retroceder páginas e habilitar/desabilitar efeitos sonoros.

### 2. 📄 [style.css](style.css)
* **Objetivo:** Aplica toda a identidade visual e atmosfera tecnológica do projeto.
* **Funcionalidades:**
  * Utiliza variáveis customizadas (`:root`) para controle ágil do tema escuro cibernético.
  * Implementa o layout de perspectiva 3D (`perspective: 1500px`) indispensável para o efeito de rotação do álbum.
  * Modela efeitos dinâmicos, incluindo o efeito *glitch* de texto na capa, sombras centrais que simulam a profundidade da dobra do livro e reações interativas ao passar o mouse (*hover*).
  * Garante responsividade para diferentes tamanhos de tela.

### 3. 📄 [app.js](app.js)
* **Objetivo:** Orquestra a interatividade e a sincronização de dados.
* **Funcionalidades:**
  * **Consumo de API:** Realiza requisições HTTP do tipo `GET` na rota `/figurinhas` de um servidor backend local (porta `8000`), preenchendo automaticamente os slots vazios correspondentes com as imagens recebidas.
  * **Efeito de Folha:** Inicializa e configura a biblioteca `PageFlip`, gerenciando ações customizadas de arrastar com o mouse ou deslizar em telas sensíveis ao toque (*touch events*).
  * **Interação de Som:** Controla a reprodução dos áudios ao virar páginas ou alternar o estado do reprodutor (mudo/ativo).

---

## 🚀 Como Executar o Projeto

1. **Frontend:**
   * Basta abrir o arquivo `index.html` diretamente em seu navegador (de preferência usando uma extensão de servidor local como *Live Server* no VS Code).

2. **Backend (Figurinhas Dinâmicas):**
   * O frontend tenta se conectar a um servidor local rodando em `http://localhost:8000`.
   * Certifique-se de iniciar a API no diretório correspondente usando:
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
   * Caso a API não esteja ativa, os slots permanecerão no modo cinza padrão mostrando apenas a descrição do profissional.
