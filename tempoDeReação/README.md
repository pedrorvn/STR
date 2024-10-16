# Tempo de reação com o jogo das bolinhas

## Objetivo

O **Jogo das Bolinhas** é um jogo simples desenvolvido em Python utilizando a biblioteca Pygame. O objetivo principal é testar o tempo de reação do jogador ao clicar em bolinhas que aparecem aleatoriamente na tela. Este jogo serve como um exemplo prático das funções de temporização e eventos, agregando atividades práticas desenvolvidas para a disciplina de **Sistemas em Tempo Real**.

## Como Funciona

1. **Geração de Bolinhas**: Bolinhas de cores diferentes (vermelha, verde, azul e amarela) aparecem aleatoriamente na tela. O jogador deve pressionar a tecla correspondente à cor da bolinha.
2. **Tempo de Reação**: O tempo que leva para o jogador pressionar a tecla após a bolinha aparecer é medido em milissegundos. O jogo acumula esse tempo para calcular a média após o término de 10 tentativas.
3. **Pontuação**: O número de bolinhas acertadas é contabilizado e exibido ao final do jogo, junto com o tempo médio de reação.

## Como Jogar

1. **Inicie o Jogo**: Execute o script Python `tempoReacao.py` para iniciar o jogo.
2. **Identifique a Cor da Bolinha**: Observe a cor da bolinha que aparece na tela.
3. **Pressione a Tecla Correspondente**: Aperte a tecla que corresponde à cor da bolinha:
   - `r` para vermelho
   - `g` para verde
   - `b` para azul
   - `y` para amarelo
4. **Continue Jogando**: O jogo continuará até que o jogador acerte 10 bolinhas.
5. **Veja os Resultados**: Após 10 acertos, o tempo médio de reação e a pontuação de acertos serão exibidos no console.

## Requisitos

Para executar o jogo, você precisa ter o Python e a biblioteca Pygame instalados. Você pode instalar o Pygame usando o seguinte comando:

```bash
pip install pygame
```

## Execução

Para iniciar o jogo, use o seguinte comando no terminal:
```bash
python tempoReacao.py
```
## Conclusão
Este jogo é uma ótima maneira de entender como as funções de temporização podem ser aplicadas em sistemas de tempo real e em jogos. 
