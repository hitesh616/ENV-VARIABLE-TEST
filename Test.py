import json
import subprocess
command = "aws s3api list-objects-v2 \--bucket dev-phynart-platform \--prefix firmwares/qa/sirius-5s-classic-r \--query 'reverse(sort_by(Contents,&LastModified))[0]'"
def getLatestExistingVersionfroms3(command):

    proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    output_json = json.loads(out)
    splitexistinglatestvarionpath = output_json["Key"].split('/')
    for Version in splitexistinglatestvarionpath:
        if Version[0].isdigit():
            # print(Version)
            return Version
    
print(getLatestExistingVersionfroms3(command))
