# User specific aliases and functions
CF_LOGS=/var/www/miq/vmdb/log
export AUTO=${CF_LOGS}/automation.log
export EVM=${CF_LOGS}/evm.log

alias cf='echo "Starting CloudForms Console"; pushd /var/www/miq/vmdb; rails c; popd'
alias log='cd $CF_LOGS'
alias auto='less +F ${AUTO}'
alias evm='less +F ${EVM}'
alias scrub='truncate -s 0 ${CF_LOGS}/evm.log; truncate -s 0 ${CF_LOGS}/automation.log'

