#!/bin/sh

#
# Base configuration variables for scripts
#
BRAND="NDC App"
COPYRIGHT="Copyright $(date +'%Y') ${BRAND}"
GCP_PROJECT="ndc-app"

export CLOUDSDK_CORE_PROJECT=$GCP_PROJECT

BIN_DIR="$(dirname ${0})"
ROOT_DIR="${BIN_DIR}/.."

info() {
  echo "${BRAND} :: ${1}"
}
