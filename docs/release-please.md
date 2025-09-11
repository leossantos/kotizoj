## Versionamento Automático

Este projeto utiliza o [release-please](https://github.com/googleapis/release-please) para versionamento automático baseado em [Conventional Commits](https://conventionalcommits.org/).

### Como funciona

1. **Commits convencionais**: Use mensagens de commit seguindo o padrão Conventional Commits:
   - `feat:` para novas funcionalidades
   - `fix:` para correções de bugs
   - `perf:` para melhorias de performance
   - `docs:` para documentação
   - `style:` para formatação
   - `refactor:` para refatoração
   - `test:` para testes
   - `chore:` para tarefas de manutenção

2. **Versionamento automático**:
   - `feat:` incrementa a versão minor (0.1.0 → 0.2.0)
   - `fix:` incrementa a versão patch (0.1.0 → 0.1.1)
   - `feat!:` ou `fix!:` com `!` incrementa a versão major (0.1.0 → 1.0.0)

3. **Changelog automático**: O arquivo `CHANGELOG.md` é atualizado automaticamente com as mudanças

4. **Releases**: Pull requests são criados automaticamente com as mudanças de versão

### Exemplos de commits

```bash
# Nova funcionalidade (versão minor)
git commit -m "feat: add support for crypto currency tracking"

# Correção de bug (versão patch)
git commit -m "fix: resolve calculation error in portfolio value"

# Breaking change (versão major)
git commit -m "feat!: change API interface for asset creation"

# Documentação (não afeta versão)
git commit -m "docs: update README with installation instructions"
```

### Configuração

O release-please está configurado através dos seguintes arquivos:
- `release-please-config.json`: Configuração principal
- `.github/workflows/release-please.yml`: Workflow do GitHub Actions
- `CHANGELOG.md`: Changelog automático
- `pyproject.toml`: Versão do projeto Python