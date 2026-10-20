# Funcoes didaticas deste curso; nao sao comandos oficiais DryRun.
# Execute em Bash: source /caminho/kit/lab.sh
export DRYRUN_BASE='https://simple-api.dryrun.security/v1'
lab_branch() {
  test -z "$(git status --porcelain)" || {
    echo 'Salve as alteracoes antes de trocar de branch.'; return 1;
  }
  git switch main && git pull --ff-only && git switch -c "$1"
}
lab_pr() {
  git push -u origin HEAD || return
  gh pr create --base main --title "$1" --body \
    'Laboratorio DryRun. Nao mesclar codigo vulneravel.'
}
lab_evidence() {
  local n sha
  n=$(gh pr view --json number --jq .number) || return
  sha=$(gh pr view --json headRefOid --jq .headRefOid) || return
  mkdir -p .evidence
  gh api "repos/$GH_REPO/commits/$sha/check-runs" \
    > ".evidence/pr-$n-checks.json"
  gh api --paginate "repos/$GH_REPO/issues/$n/comments" \
    > ".evidence/pr-$n-comments.json"
  gh pr checks || true
}
lab_close() {
  gh pr close || return
  git switch main
}
dryget() {
  test -n "$DRYRUN_API_KEY" || { echo 'Falta DRYRUN_API_KEY'; return 1; }
  curl --fail-with-body --silent --show-error \
    -H "Authorization: Bearer $DRYRUN_API_KEY" \
    "$DRYRUN_BASE/$1"
}
