import json

def readJson (numTrial, numIteration, path):
    configurations = []
    acc_return = []
    config_return = []
    for i in range (numTrial): 
        with open(path[i], 'r') as f:
            lines = f.readlines()
            i = 0
            appended = False
            while (i < len(lines)): 
                target = lines[i]
                parse = json.loads(target)
                acc_return.append(parse["mean_accuracy"])
                if (appended == False):
                    for key in parse["config"]:
                        if (key != "args"):
                            configurations.append(parse["config"][key])
                    config_return.append(configurations)
                    appended = True

                i = i + 1
    
    return [acc_return, config_return]

print (readJson(1, 4, ["/Users/timchang/Desktop/project/result.json"])[0])
print (readJson(1, 4, ["/Users/timchang/Desktop/project/result.json"])[1])
