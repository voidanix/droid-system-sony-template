%define rpm_device pdx201

%define multiple_rpms 1

%include droid-system-license.inc
%include droid-system-common.inc
%include droid-system-device/droid-system.inc

%pre
# This may/should be removed after the next stop release after 4.2.0.
STATUS_FILE=/data/vendor/audio/.speaker-recal-done
if [ ! -f $STATUS_FILE ]; then
    rm -rf /data/vendor/audio
    mkdir -p /data/vendor/audio
    touch $STATUS_FILE
fi
