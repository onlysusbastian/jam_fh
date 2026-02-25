JACK Audio Middleware For Hardware.

First problem:
    no universal audio hardware switcher in DAW while using JACK in linux.
    Windows has ASIO4ALL which is directly supported by vendors. This 
    solves the problem by allowing the user to select I/O inside the CLI
    before allowing input.


Process: 
    -read pw-dump (pipewire dump) which will provide us the information 
    about the current drivers and hardware linked with each other.

    -filter the data according to needs and rank the devices.

    -select best ranked device for I/O that the user will use in the DAW.


allows effortless selection of the device in the terminal and sets it 
default whenever the device is connected. so no problem of changing the 
input/output of the device in a patchbay everytime you use a DAW in linux.


control flow:
    DAW -> JACK -> Pipewire graph -> ALSA -> Hardware
                        |
                        |
                      wpctl  

