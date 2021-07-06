import json

def readJson (numTrial, numIteration, path):
    acc_return = []
    config_return = []
    for j in range (numTrial): 
        with open(path[j], 'r') as f:
            configurations = []
            accuracy = []
            lines = f.readlines()
            i = 0
            appended = False
            while (i < numIteration): 
                target = lines[i]
                parse = json.loads(target)
                accuracy.append(parse["mean_accuracy"])
                if (appended == False):
                    for key in parse["config"]:
                        if (key != "args"):
                            configurations.append(parse["config"][key])
                    config_return.append(configurations)
                    appended = True

                i = i + 1
            acc_return.append(accuracy)
    
    return [acc_return, config_return]

print (readJson(1, 2, ["/Users/timchang/Desktop/project/result.json"])[0])
print (readJson(1, 2, ["/Users/timchang/Desktop/project/result.json"])[1])
