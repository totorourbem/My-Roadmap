// Você alguma vez já jogou algum jogo que te desse mais de uma escolha e, dependendo do que você escolhesse, o destino do personagem seria totalmente diferente?
// Hoje você vai desenvolver um exemplo assim com Javascript!
// Eu quero que você trabalhe com estruturas de controle de fluxo. Esse jeito complicado de falar só quer dizer que, assim como nos jogos, a história que você montar precisa se adaptar às respostas dadas por quem está jogando.
// Para isso, você vai precisar de algumas estruturas capazes de alterar o fluxo da aplicação, como for, while, if e else. Todas essas conseguem cumprir esse objetivo, dada uma certa condição.
// O if e o else, que eu já te mostrei nos últimos dias, são capazes de criar ramificações dentro da aplicação para que seja tomada uma ou outra ação, dependendo da condição fornecida.
// Os loops (como for e while) são capazes de fazer uma tarefa repetitiva se transformar em poucas linhas de código, independente de quantas vezes você precisar repetir aquela tarefa.
// Seu desafio de hoje é criar os destinos possíveis de um jogo, em que o usuário consiga escolher:

// 1. Se quer seguir para área de Front-End ou seguir para a área de Back-End.
// 2. Caso esteja na área de Front-End, se quer aprender React ou aprender Vue. Caso esteja na área de Back-End, poderá aprender C# ou aprender Java.
// 3. Depois, independente das escolhas anteriores, o usuário poderá escolher entre seguir se especializando na área escolhida ou seguir se desenvolvendo para se tornar Fullstack. Você deve exibir na tela uma mensagem específica para cada escolha.
// 4. Por fim, pergunte quais são as tecnologias nas quais a pessoa gostaria de se especializar ou de conhecer. Aqui, a pessoa pode responder N tecnologias, uma de cada vez. Então, enquanto ela continuar respondendo ok para a pergunta: “Tem mais alguma tecnologia que você gostaria de aprender?”, continue apresentando para ela o Prompt, para que ela complete o nome da tecnologia em questão. E, logo depois, apresente uma mensagem comentando algo sobre a linguagem inserida.

// O importante é que a pessoa que estiver jogando possa sempre escolher qual decisão tomar para conseguir aprender e se desenvolver na área de programação.
// Além disso, também é essencial que, ao final do jogo, ela possa inserir quantas tecnologias quiser na lista de aprendizado.

let jogador = prompt(`Ola! Seja benvindo ao Desafio de carreiras tecnológicas!
    Primeira,mente, preciso saber, qual o seu nome?`);

let escolhas = [];

while (true) {
    
    alert(`Seja benvindo, ${jogador}! Espero que se divirta por alguns instantes.`);

    let opcao1 = parseInt(prompt(`${jogador}! Em nossa primeira etapa, precisamos decidir o seu destino!
        Mais informações sobre os caminhos:
        - Back-end:   1
        - Front-end:   2
        - FullStack:   3
        - Sair:   4`));

    if (opcao1 ===   1 || opcao1 ===   2 || opcao1 ===   3) {
        escolhas.push({ caminho: opcao1, tecnologia: null });
    } else if (opcao1 ===   4) {
        break; // Saída do loop
    } else {
        alert(`${jogador}, preciso que você escolha uma opção válida, de   1 a   4!`);
    }

    if (escolhas.length >   0 && escolhas[escolhas.length -   1].caminho !==   4) {
        let opcao2 = parseInt(prompt(`Chegou a hora de escolher:
            - Continuar escolhendo:   1
            - Corrigir escolha anterior:   2
            - Terminar o jogo:   3`));

        if (opcao2 ===   1) {
            continue; // Volta para o início do loop
        } else if (opcao2 ===   2) {
            escolhas.pop(); // Remove a última escolha
        } else if (opcao2 ===   3) {
            break; // Saída do loop
        } else {
            alert(`${jogador}, preciso que você escolha uma opção válida, de   1 a   3!`);
        }
    }
}

// Percorre as escolhas para obter as tecnologias escolhidas
for (let i =   0; i < escolhas.length; i++) {
    if (escolhas[i].caminho ===   1) { // Back-end
        escolhas[i].tecnologia = parseInt(prompt(`Agora, qual tecnologia você gostaria de aprender ou saber mais? Digite o número correspondente.\n- C# ("C Sharp"):   1\n- Java:   2\n- Outra tecnologia:   3`));
    } else if (escolhas[i].caminho ===   2) { // Front-end
        escolhas[i].tecnologia = parseInt(prompt(`Agora, qual tecnologia você gostaria de aprender ou saber mais? Digite o número correspondente.\n- React:   1\n- Vue:   2\n- Outra tecnologia:   3`));
    } else if (escolhas[i].caminho ===   3) { // FullStack
        escolhas[i].tecnologia = parseInt(prompt(`Agora, qual tecnologia você gostaria de aprender ou saber mais? Digite o número correspondente.\n- React ou Vue:   1\n- C# ou Java:   2\n- Outra tecnologia:   3`));
    }
}

// Exibe o resumo das escolhas do jogador
alert(`Resumo das escolhas de ${jogador}:`);
for (let i =   0; i < escolhas.length; i++) {
    let caminho = '';
    let tecnologia = '';
    switch (escolhas[i].caminho) {
        case   1:
            caminho = 'Caminho do Back-end';
            break;
        case   2:
            caminho = 'Caminho do Front-end';
            break;
        case   3:
            caminho = 'Caminho FullStack';
            break;
    }
    switch (escolhas[i].tecnologia) {
        case   1:
            tecnologia = 'C# ("C Sharp")';
            break;
        case   2:
            tecnologia = 'Java';
            break;
        case   3:
            tecnologia = 'React';
            break;
        case   4:
            tecnologia = 'Vue';
            break;    
    }
    alert(`Escolha ${i +   1}: ${caminho}${tecnologia ? ` com a tecnologia ${tecnologia}` : ''}`);
}

alert(`Fim de jogo! Obrigado por jogar, ${jogador}. Tenha um   ótimo dia!`);