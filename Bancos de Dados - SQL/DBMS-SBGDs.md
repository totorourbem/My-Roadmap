# Fundamentos dos Bancos de dados

## DBMS/SBGDs (Database management systems/sistemas gerenciadores de bancos de dados)
 
### O Que é um DBMS?
Um Sistema de Gerenciamento de Banco de Dados (DBMS) é um software de proposito geral, projetado para armazenar, recuperar e manipular grandes conjuntos de dados. Este sistema é fundamental em aplicações que requerem o gerenciamento eficiente de grandes volumes de informação. Os DBMS relacionais, em particular, baseiam-se em um modelo que organiza os dados em tabelas com linhas e colunas, oferecendo uma abordagem intuitiva e flexível para o gerenciamento de dados, de maneira modular..

![advantages of dbms](https://scientips.com/wp-content/uploads/2020/07/yess.png)

### A Importância dos DBMS
Os DBMS oferecem várias vantagens em comparação com o armazenamento tradicional de dados em arquivos do sistema operacional. Estes incluem:

- **Eficiência no Acesso aos Dados:** Técnicas sofisticadas para armazenamento e recuperação eficiente dos dados.
- **Integridade e Segurança:** Capacidade de impor restrições de integridade e controlar o acesso aos dados, garantindo que apenas usuários autorizados possam acessar informações específicas.
- **Administração Centralizada dos Dados:** Facilita a organização dos dados, reduzindo redundâncias e melhorando a qualidade da informação.

![dbms](https://lh5.googleusercontent.com/jlooEUFrB1WkSrvTQRDPYCiYdqUxMfFUm4wSb6JEKWmii508hz10AkEiNHkDS1x8-nhzcnnCxhuD11EzJ8xvrj74kTv041JqRcv6IrkEIwhe4-02EJKwwQU-NNQrDFG-q3OtaQ1_)

### Evolução Histórica dos DBMS

A Evolução Histórica dos Sistemas de Gerenciamento de Banco de Dados (DBMS) remonta aos primórdios da computação, na década de 1960. Desde então, esses sistemas têm passado por diversas transformações, acompanhando as demandas e necessidades do mercado.
Inicialmente, os sistemas de gerenciamento de banco de dados tinham como objetivo principal otimizar e reduzir os custos das operações de armazenamento e recuperação de dados. Nessa época, a IBM foi uma das pioneiras nesse campo, desenvolvendo soluções para lidar com grandes volumes de dados.
Modelos de banco de dados são fundamentais para o armazenamento de informações em empresas e organizações. Dentre os modelos existentes a essa época, temos o hierárquico e em redes. 
#### O modelo Hierárquico
O modelo hierárquico, voltado ao registro/instância, foi muito utilizado nas décadas de 60 e 70. Nele, as informações eram armazenadas em árvores, de maneira não estruturada, tendo como base o registro em si. Dentre as linguagens utilizadas nesse modelo, destacam-se Cobol, BDDBase, FoxPro e Clipper.
O IMS (Information Management System) é um exemplo de sistema que utiliza o modelo hierárquico. Nele, os registros são organizados em uma estrutura de árvore com raiz, na qual cada nó é um conjunto de dados e links para outros nós.
#### O modelo em redes
Já o modelo em redes é mais complexo e exige um conhecimento mais aprofundado da estrutura física do banco de dados. Ele é baseado na associação de diversos nós e relacionamentos não definidos entre eles. Foi criado em 1964 pela CoDASiL.
Esse modelo é utilizado em situações nas quais há relacionamentos N:M entre os registros. Além disso, ele permite a criação de relações não hierárquicas entre os nós, o que torna sua estrutura mais flexível e adaptável às necessidades da organização.
No entanto, a complexidade desse modelo pode tornar sua implementação mais difícil e custosa. É necessário um planejamento cuidadoso para garantir que a estrutura do banco de dados seja adequada às necessidades da empresa.
#### O início dos SGBDs/DBMS
Com o passar do tempo, surgiu a necessidade de estruturar os dados de forma mais eficiente, evitando falhas humanas e permitindo um acesso mais rápido e preciso às informações. Foi nesse contexto que surgiram os primeiros Sistemas de Gerenciamento de Banco de Dados Relacionais (SGBDR), baseados no modelo proposto por Ted Codd.
O surgimento do modelo relacional em 1970, criado por Ted Codd, marcou um grande avanço na área de banco de dados. Esse modelo é baseado em álgebra relacional e é altamente generalista, proporcionando um alto nível de transparência para o usuário. Uma das principais características desse modelo é a alta abstração das tabelas, que são representadas de forma simples e intuitiva. Além disso, na década de 70 foram desenvolvidos a linguagem SQL e a teoria dos conjuntos, que contribuíram para a evolução do modelo relacional.
As relações TAD foram criadas para armazenamento com transparência e união de dados de diversos tipos. Esse modelo possui dois usuários: o usuário e o administrador. O administrador é responsável por definir as regras e tabelas do banco de dados, além de comandos traduzidos pelo processador LDD. Essas regras fornecem a diretiva dentro dos contextos, tabelas e dados.
A Linguagem de Definição de Dados (LDD) é uma linguagem específica para a tradução de dados para SQL. Já o usuário utiliza linguagem de definição, altera e extrai informações. As transações são o agrupamento das queries para execução, storage (HD) e buffer TRAM.
O SGBD (Sistema Gerenciador de Banco de Dados) tem como função controlar o storage e buffer, que é o armazenamento do HD para a RAM e a movimentação entre as memórias. É importante destacar que o SGBD é fundamental para garantir a integridade dos dados e a segurança do sistema.
O modelo relacional revolucionou a forma como os dados são representados e acessados. Em vez de utilizar estruturas hierárquicas ou em rede, como era comum até então, o modelo relacional utiliza tabelas para armazenar os dados, estabelecendo relações entre elas por meio de chaves. Isso permitiu uma maior flexibilidade na manipulação e recuperação dos dados, além de facilitar a integração entre diferentes sistemas.
A linguagem SQL (Structured Query Language) foi desenvolvida nessa época para facilitar a interação com os bancos de dados relacionais. Ela se baseia em conceitos da teoria dos conjuntos e permite a realização de consultas complexas de forma simples e intuitiva. Com o SQL, os usuários podem extrair informações específicas do banco de dados, realizar atualizações nos dados e definir regras para garantir a integridade dos mesmos.
Os SGBD se tornaram cada vez mais populares ao longo dos anos, com o surgimento de sistemas como o Sistema R da IBM e o Oracle. Esses sistemas ofereciam recursos avançados de gerenciamento de transações, segurança e escalabilidade, consolidando o modelo relacional como o padrão da indústria.
A partir dos anos 90, com o avanço da programação orientada a objetos, surgiram os chamados bancos de dados orientados a objetos. Esses sistemas combinavam as vantagens do modelo relacional com os conceitos da programação orientada a objetos, permitindo o armazenamento de objetos complexos diretamente no banco de dados.
No início dos anos 2000, com o crescimento exponencial da quantidade de dados gerados pelas empresas e a necessidade de processá-los em tempo real, surgiram os bancos de dados NoSQL. Esses sistemas foram projetados para lidar com grandes volumes de dados não estruturados, como os gerados por redes sociais, sensores e dispositivos móveis. Diferentemente dos bancos de dados relacionais, os bancos de dados NoSQL não utilizam o modelo relacional tradicional, permitindo uma maior flexibilidade na estruturação e manipulação dos dados.
Atualmente, existem diversos Sistemas de Gerenciamento de Banco de Dados disponíveis no mercado. Alguns dos mais populares são o OracleDB, conhecido por sua performance e robustez; o MySQL, um banco de dados open source mantido pela Oracle, que é leve, integrável e versátil; o Microsoft SQL Server, que é integrado ao PowerBi e ao Office/Windows e oferece recursos mais sofisticados; e o PostgreSQL, um banco de dados robusto e híbrido, que é amplamente utilizado em conjunto com linguagens como PHP e Python. Além desses, também temos o MariaDB, uma variante do MySQL licenciada que oferece buscas mais otimizadas.
Em resumo, os Sistemas de Gerenciamento de Banco de Dados passaram por uma evolução significativa ao longo dos anos, acompanhando as demandas do mercado e as necessidades das empresas. Desde os modelos hierárquicos e em rede até os bancos de dados NoSQL, esses sistemas continuam desempenhando um papel fundamental na organização e recuperação das informações, garantindo a integridade e disponibilidade dos dados para os usuários.

![history of dbms](https://www.researchgate.net/publication/356934804/figure/fig1/AS:1099553134649344@1639165304753/Evolution-of-database-systems.ppm)
