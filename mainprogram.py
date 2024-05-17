# import sys
import os
import subprocess
def filecreation(script_path):
    with open(script_path,"w") as f:
        f.write("Add-Type -AssemblyName System.Speech\n")
        f.write("$speechSynthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer\n")
        f.write("$speechSynthesizer.SelectVoice('Microsoft Zira Desktop')\n")
    return
def run_powershell_script(script_path):
    # Use subprocess to run the PowerShell script
    
        subprocess.run(['powershell.exe', '-File', script_path])
        # os.remove(script_path)
def textinput(text,script_path):
        with open("tt1.ps1","a") as f:
        # f.write("$text = Read-Host '${text}'\n")
             f.write("$speechSynthesizer.Speak(\"" + text + "\")\n")
             
             return
        # f.write("$speechSynthesizer.Speak("'+ text +'")\n")   
     

    
# print('file ban gyi ha')
# Path to the PowerShell script file
script_path = 'tt1.ps1'
  # Change this to the path of your PowerShell script
# Run the PowerShell script

# with open("tt1.ps1","r") as f:
#    s=f.read()
#    print(s)
while(True):
    text =input("Enter text you want to speak :")
    if(text=='N'):
     break
    #  sys.exit()
    else:
     filecreation(script_path)
     textinput(text,script_path)
     run_powershell_script(script_path) 
     filecreation(script_path)


