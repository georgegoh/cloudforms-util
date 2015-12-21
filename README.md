# cloudforms-util

Aliases and environment settings to make working with CloudForms on the command line easier.

## To Build

    make rpm

To get a pre-built rpm, see this link https://packagecloud.io/georgegoh/cloudforms-util
Latest RPM package: https://packagecloud.io/georgegoh/cloudforms-util/el/7/noarch/cloudforms-util-0.3-4.noarch.rpm

## To install

Copy the rpm into the CloudForms VM and perform a normal RPM install.

## To Use

Shortcut aliases for CloudForms:

   cf    - bring up the rails console with $evm object loaded.
   
   auto  - less +F automate.log
   
   evm   - less +F evm.log
   
   log   - cd /var/www/miq/vmdb/log
   
   scrub - truncate the automate and evm logs.
