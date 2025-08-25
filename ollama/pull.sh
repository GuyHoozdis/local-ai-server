#!/usr/bin/env bash
# ##############################################################################
# Pull or update a model from Ollama's model repository.
#
# Usage:
#   $ pull [model ...]
#
# Arguments:
#   model-name - The name(s) of the model(s) to pull or update.
#
# Environment Variables:
#   DRY_RUN - If set to "true", the script will only simulate actions without making changes (default: false).
#
# Examples:
#   Pull a single model that does not exist locally:
#    $ ./ollama/pull.sh gpt-oss
#
#   Pull multiple models, some of which may already exist locally:
#    $ ./ollama/pull.sh gpt-oss llama2 mistral
#
#   Simulate pulling a model without making changes:
#    $ DRY_RUN=true ./ollama/pull.sh gpt-oss
# ##############################################################################

set -Eoeu pipefail

declare -r GREEN='\033[0;32m'
declare -r RED='\033[0;31m'
declare -r YELLOW='\033[0;33m'
declare -r NC='\033[0m'
declare -r SCRIPTPATH=$( cd $(dirname ${BASH_SOURCE[0]}) > /dev/null; pwd -P )
declare -r DRY_RUN=${DRY_RUN:-false}

# Trap handler for script cleanup
function cleanup() {
  trap - SIGINT SIGTERM EXIT
  # Add cleanup logic here if necessary.
}

function stderr() {
  local msg="${1-}"
  echo >&2 -e "${msg}"
}


function info() {
  local msg="${1-}"
  stderr "[${GREEN}INFO${NC}] ${msg}"
}


function warn() {
  local msg="${1-}"
  stderr "[${YELLOW}WARN${NC}] ${msg}"
}


function error() {
  local msg="${1-}"
  stderr "[${RED}ERROR${NC}] ${msg}"
}


function fatal() {
  local msg="${1-}"
  local exit_code="${2-1}"
  error "${msg}"
  exit ${exit_code}
}


function is_dry_run() {
  [[ "${DRY_RUN}" == "true" ]] || [[ "${DRY_RUN}" == "1" ]]
}

function ollama_pull() {
  local model="${1-}"
  local exit_code=0
  if [[ -z "${model}" ]]; then
    fatal "Model name is required for ollama_pull function."
  fi

  info "Pulling model '${model}'..."
  if is_dry_run; then
    warn "[DRY RUN] Would run: ollama pull ${model}"
  else
    set +e
    ollama pull "${model}"
    exit_code=$?
    set -e
  fi

  return ${exit_code}
}


# Entrypoint
trap cleanup SIGINT SIGTERM EXIT
if [[ $# -lt 1 ]]; then
  error "At least one model name must be provided."
  echo -e "\nUsage: $(basename $0) [model ...]"
  exit 1
fi

info "Fetching ${#} model(s)..."
for model in "$@"; do
  if ollama_pull "${model}"; then
    info "Successfully processed model '${model}'."
  else
    error "Error processing model '${model}'."
  fi
done
