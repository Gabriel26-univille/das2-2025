# Design e Arquitetura de Software 2

## Gabriel Lopes

## Aula 27/02

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

## Aula 06/03

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

## Aula 10/03

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

- Autenticação: Sempre usar autenticação de dois ou três fatores. O que eu sei (usuário e senha), sou (biometria) e tenho (chave de segurança);

- Permissão: definir exatamente o que cada tipo de usuário pode acessar. Não dar mais acesso que o necessário (princípio do privilégio mínimo);

- Usar criptografia: proteger dados em trânsito por meio de protocolos de criptografia;

- IAM (Identity and Access Management): responsável por usuários, funções, políticas, grupos e usuários...

## Aula 13/03

- AWS access key não expira (long-term credential), tornando necessário um sistema para gera novas keys de tempo em tempo;

- Não usar usuário root para tarefas que outros usuários podem fazer. Habilitar MTA imediatamente no root;

- Roles (funções) permitem trocar permissões dos usuários ("assumir um novo papel") a key de um role dura um tempo limitado;

- Acesso pela console (acesso programático): aws cli, aws sdk, aws api rest. Integração da aplicação com a AWS, Chave de acesso do role permite que o usuário faça ações fora de suas permições habituais;

## Aula 17/03

- RBAC: role base access control - método de administrar acesso de usuários ao sistema baseado no seu papel na organização;

- Policies são usadas para definir exatamente as permissões de cada usuário. Policies de identidade definem permissões baseado em cada usuário. Policies de recurso definem permissões por meio de documentos - permissão granular.

- Todas tem efeito, ação e recurso. Nsário especificar usuário (principal) no caso de policy de recurso.

- Tipos de armazenamento:

- por blocos: ebs (elastic block storage) dados armazenados em blocos de tamanhos fixos, suportam edições no meio dos arquivos;

- por arquivos: efs (elastic file system) FXs (file share), dados são armazenados em uma estrutura hierarquica, várias máquinas trocando arquivos por meio de uma máquina mais alta na estrutura;

- por objetos: s3, dados são armazenados como objetos baseados em atributos e metadados;

- S3: armazena uma quantidade ilimitada de dados não estruturados, mas apenas 5tb por objeto ou arquivo. Arquivos maiores são fracionados. Não é possível rodar BDs no S3. Todo objeto tem uma chave única. Todos os objetos tem uma url pública, mas são bloqueados por padrão;

- Não existem pastas no s3, essa divisão é feita por um prefixo no url;

## Aula 20/03

- S3 tem durabilidade e disponibilidade de 99,99%;

- usos do S3: sites estáticos, picos de demanda, recuperação de desastres, armazenamento de dados para análise;

- storage gateway: servidor que serve como buffer, dados gravados nele são mandados para o s3;

- Multipart upload: arquivos grandes são armazenados no S3 por meio de paralelização, o arquivo é fatiado em partes de tamanhos iguais e são reunídos depois;

- Direct connect: usa cloudfront edge locations para criar caminhos mais curtos para acessar o S3 (diminuir latência por não entrar na internet pública);

- transfer family: permite enviar e receber do s3 sem ter que alterar o protocolo de transferência de arquivos do seu software;

- storage classes: forma como o S3 guarda a informação, define o preço e disponibilidade;

- Classes quentes (acesso imediato ao objeteto armazenado): 

- Standard: caro para armazenar, barato para baixar;

- Standard-IA (infrequent access): mais barato para armazenar, mais caro para baixar. Para arquivos pouco acessados;

- One zone-IA: faz apenas uma cópia do objeto ao invés de 3, tornando armazenamento mais barato;

- Intelligent-tiering: Arquivos são monitorados no s3 e são movidos para a classe mais apropriada;

- Classes frias (objetos precisam ser recuperados):

- tem períodos mínimos para manter arquivos. custos extras são aplicados se baixar antes desse tempo;

- Glacier deep archive: armazenamento offline, arquivos podem demorar de 12 a 48 horas para serem recuperados. Mais barato para armazenar;

- Glacier flexible retrieval: mais rápido para baixar e mais caro que o deep archive;

- Glacier instant retrieval: arquivo disponível instantaneamente, mas precisa passar por rehidratação para ser usado;

- Outposts: Leva servidores da AWS fisicamente para dentro da sua empresa. Nuvem privada como se fosse uma região da sua empresa. Amplamente usado pelo governo brasileiro.

## Aula 24/03

- S3 Lifecycle: Conjunto de regras para transacionar entre classes ou expirar arquivos;

- S3 versioning: Deve ser habilitado, não desabilitável. Pode ser pausado. Mantém a chave do objeto e cria uma version id diferente por versão. Apagar um objeto cria uma versãoque marca o objeto como apagado. Portanto apagar essa versão restaura o objeto. OBS: não é possível editar arquivos no S3.

- CORS (cross-origin resource sharing): Forma de proteção para sites. Permissão para que um site acesse o conteúdo de outro;

- Por padrão todo bucket é criptografado e privado;

- No S3 se paga pelos gigas armazenados e por acessos aos arquivos;

## Aula 03/04

- EC2: Elastic compute Cloud, permite criar e hospedar sistemas de software com capacidade computacional redimencionável;

- Serve para qualquer coisa que necessite de um servidor;

- AMI, uma "foto" do servidor, permitindo criar cópias idênticas do servidor original. Serve para recuperação e repetição;

- EBS: Armazenamento persistente na EC2, diferente da instance store no host, que só armazena arquivos temporariamente;

- quanto menos gerenciado, mais controle:

- (menos gerenciado) Vms, Containers, VPS, PaaS, Serverless (mais gerenciado);

- Compute optimizer: IA que recomenda recursos de computação da AWS mais eficientes para workloads, tem versão gratuita e paga;

- File share: usar FSx para Windows, EFS para Linux;
