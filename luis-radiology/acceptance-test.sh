#!/bin/bash
# Acceptance test for the luis-pacs PACS workstation setup.
#
# Run from the Mac mini. Proves the full chain end to end: the node is on the
# tailnet, it is TAGGED (not user-owned), the SSH service answers, and the
# rgfsvc account can log in. Read-only -- runs `hostname` and `whoami` on the
# far end and nothing else.
#
# Usage: ./acceptance-test.sh [hostname]   (default: luis-pacs)

set -uo pipefail

TS=/Applications/Tailscale.app/Contents/MacOS/Tailscale
HOST="${1:-luis-pacs}"
USER_ACCT=rgfsvc
pass=0; fail=0

ok()   { echo "  PASS  $1"; pass=$((pass+1)); }
bad()  { echo "  FAIL  $1"; fail=$((fail+1)); }

echo "=== Acceptance test: ${HOST} ==="
echo

# 1. Node is on the tailnet
echo "[1] Node present on tailnet"
if line=$("$TS" status 2>/dev/null | grep -i "[[:space:]]${HOST}[[:space:]]"); then
  ok "found: ${line}"
  ip=$(awk '{print $1}' <<<"$line")
else
  bad "${HOST} not in 'tailscale status' -- did Step 2 run?"
  echo; echo "=== ${pass} passed, ${fail} failed ==="; exit 1
fi

# 2. Node is TAGGED, not user-owned. This is the security control from Step 3.
echo "[2] Node is tagged (not user-owned)"
owner=$(awk '{print $3}' <<<"$line")
if [[ "$owner" == tag:* ]]; then
  ok "owner is ${owner}"
else
  bad "owner is '${owner}', expected tag:pacs -- node is USER-OWNED, remove and rejoin"
fi

# 3. SSH port reachable
echo "[3] SSH port 22 reachable"
if nc -z -G 8 "$ip" 22 2>/dev/null; then
  ok "port 22 open at ${ip}"
else
  bad "port 22 closed -- shields still up (Step 4b), or sshd not started (Step 5a)"
fi

# 4. The actual acceptance test
echo "[4] SSH login as ${USER_ACCT}"
out=$(ssh -o BatchMode=no -o ConnectTimeout=15 -o StrictHostKeyChecking=accept-new \
        "${USER_ACCT}@${HOST}" "hostname && whoami" 2>&1)
rc=$?
if [[ $rc -eq 0 && -n "$out" ]]; then
  ok "remote returned:"
  sed 's/^/        /' <<<"$out"
else
  bad "ssh exited ${rc}:"
  sed 's/^/        /' <<<"$out"
fi

echo
echo "=== ${pass} passed, ${fail} failed ==="
[[ $fail -eq 0 ]] && echo "ACCEPTANCE TEST PASSED -- durable remote access confirmed."
exit $fail
