# Design e Arquitetura de Software 2

## Gabriel Lopes

## Aula 27/02/2025

### Trade-offs

Sempre há trade-offs ao escolher uma arquitetura, ou seja escolhas levando em consideração as capacidades e limitações das tecnologias.

- Consistência: Dados são enviados e recebidos corretamente em transações;
- Durabilidade: Manter os dados gravados;
- Espaço: Espaço de armazenamento disponível, ter mais não é sempre necessário;
- Escalabilidade: O quão bem o sistema lida com alta demanda. (capacidade operacional / custo)

(não se pode ter todos, é necessário priorizar alguns)

### Automação e melhorias de infraestrutura

CloudWatch detecta quedas no sistema, EC2 automaticamente configura e sobe um servidor idêntico.

IaC (Infrastructure as Code): Automatizar processos na infraestrutura usando código, eliminando processos manuais.

Tratar recursos como descartáveis: Recursos devem ser substituíveis, evitar que recursos como servidores sejam complexos ou não automatizados a ponto de serem insubstituíveis.

## Aula 06/03/2025

- Acoplamento: Dependência entre servidores da aplicação, um caso em que a queda do BD significa a queda da aplicação é um exemplo de alto acoplamento. Elastic Load Balancing (ELB) é um método para diminuir acoplamento;

- Projetar serviços, não servidores;

- Evitar pontos únicos de falha por meio de replicação de BD;

- Otimização de custo: Apenas usar recursos do tipo e tamanho necessário;

- Cache: Armazenar dados frequentemente acessados em caches regionais para evitar acessos desnecessários ao BD principal;

- Segurança: princípio do privilégio mínimo - cada usuário só tem acesso ao que precisa;

- Seleção de regiões: Usar data centers nos lugares onde dados são mais requisitados (mais usuarios);

- Local zone: AZs menores para aonde não há demanda o bastante para AZs normal;

- Wavelength zone: Servidor que roda em conjunto com 5g para minimizar latência.

### Escolher a opção de banco correta

- Escalabilidade horizontal: Ter réplicas do banco de dados, ler e escrever no primário, apenas ler nas réplicas. 

- BD relacional: Tem escalabilidade vertical, feito para performace extrema. Não feito para ser dinâmico;

## Aula 10/03/2025

- Edge location (data center / server mais próximo do consumidor) busca dados do regional edge cache, que busca da origem;

### Securing Access

- Modelo compartilhado de servidor divide a responsabilidade entre provedor e usuário. A segurança da parte física é responsabilidade do servidor, a segurança na nuvem é do cliente;

- S3 (simple storage service) Saas, mais responsabilidades nas mãos do provedor. Criptografia transparente, padrão básico da AWS;

- Ter provedor de identidade forte: é necessário ter uma forma mais segura de armazendar usuário e senha que no BD. Usar software como keycloak ou outro epecializado em segurança;

- Proteção de dados em trânsito e em descanso;

- Aplicar segurança em todas as camadas;

- Manter as pessoas longe dos dados (não dar acesso direto ao BD);

- Ter rastreabilidade (registrar todas ações dos usuários);

- Se preparar para eventos de falha de segurança;

- Automatizar práticas de segurança;

- Autenticação de dois ou três fatores: o que eu sei (usuário e senha), sou (biometria) e tenho (chave de segurança);

- Permissão: definir exatamente o que cada tipo de usuário pode acessar. Não dar mais acesso que o necessário (princípio do privilégio mínimo);

- Usar criptografia: proteger dados em trânsito por meio de protocolos de criptografia;

- IAM (Identity and Access Management);
