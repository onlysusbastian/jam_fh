# JACK Audio Middleware For Hardware

## this solves a very specific problem of audio routing for DAWs in Linux.

The biggest issue with DAWs in Linux is switching between different audio drivers in the system. DAWs don't detect the external devices most of the time even if it is connected through JACK. This tool helps switching the audio drivers in the system really easy through one command.

command terms:
    internal - the internal audio of the device   
    external - the external audio device being used  
    souce - input audio  
    sink - output audio  

**COMMANDS**:
    python main.py internal source (internal device as the source)  
    python main.py external source (external device as the source)  

    python main.py external source (external device as the source)  
    python main.py external sink (external device as the sink)  

    python main.py internal both (internal device as the source and sink)  
    python main.py external both (external device as the source and sink)  

    python main.py status (show current status of the drivers)  

P.S. this project will be improved soon. adding universal commands is my next goal.
