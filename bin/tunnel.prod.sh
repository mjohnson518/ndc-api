#!/bin/sh
source $(dirname ${0})/base.sh

if ! [ -x "$(command -v cloud_sql_proxy)" ]; then
  echo '\nError:' >&2
  echo 'The Cloud SQL proxy command cannot be found, try installing it from here:' >&2
  echo 'https://cloud.google.com/sql/docs/mysql/connect-external-app#proxy' >&2
  echo '\n' >&2
  exit 1
fi

info "Tunneling into GCP production SQL instance"
$(which cloud_sql_proxy) -instances=ndc-app-1234:us-central1:instance-1=tcp:3308
