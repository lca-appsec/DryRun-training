# Course helpers. Source this file from the generated session.sh.
export DRYRUN_BASE='https://simple-api.dryrun.security/v1'
lab_branch() {
  test -n "$GH_REPO" || { echo 'Load session.sh first.'; return 1; }
  test -z "$(git status --porcelain)" || {
    echo 'STOP: local changes exist. Run git status and finish them.'; return 1;
  }
  git switch main && git pull --ff-only && git switch -c "$1"
}
lab_pr() {
  test "$(git branch --show-current)" != main || {
    echo 'STOP: create an exercise branch first.'; return 1;
  }
  git push -u origin HEAD || return
  gh pr create --base main --title "$1" --body \
    'DryRun student exercise. Do not merge vulnerable code.'
}
lab_evidence() {
  local n sha
  n=$(gh pr view --json number --jq .number) || return
  sha=$(gh pr view --json headRefOid --jq .headRefOid) || return
  mkdir -p .evidence
  printf 'PR %s; remote SHA %s\n' "$n" "$sha"
  git rev-parse HEAD
  gh api "repos/$GH_REPO/commits/$sha/check-runs" \
    > ".evidence/pr-$n-checks.json" || return
  gh api --paginate "repos/$GH_REPO/issues/$n/comments" \
    > ".evidence/pr-$n-comments.json" || return
  gh pr checks
  echo 'Read the check results above; failure can be an expected finding.'
}
lab_close() {
  test -z "$(git status --porcelain)" || {
    echo 'STOP: local changes exist. Finish/review them first.'; return 1;
  }
  gh pr close || return
  git switch main
}
dryget() {
  test -n "$DRYRUN_API_KEY" || {
    echo 'STOP: load DRYRUN_API_KEY in this terminal.' >&2; return 1;
  }
  curl --fail-with-body --silent --show-error \
    -H "Authorization: Bearer $DRYRUN_API_KEY" "$DRYRUN_BASE/$1"
}
