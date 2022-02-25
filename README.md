ln ./LaravelApp/.env ./.env

alias sail='[ -f sail ] && bash sail || bash LaravelApp/vendor/bin/sail'


pactl load-module module-native-protocol-unix socket=/tmp/pulseaudio.socket

# in /tmp/pulseaudio.client.conf
default-server = unix:/tmp/pulseaudio.socket
autospawn = no
daemon-binary = /bin/true
enable-shm = false


TODO 
container namen in env 
Pulseclient over env 
