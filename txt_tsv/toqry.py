import glob
import sys
import random



listatxt = glob.glob("*.txt", recursive = True)
listatsv = glob.glob("*.tsv", recursive = True)
Queries = 0
for txtname in listatxt:
    base = txtname.strip(".txt")
    if "r" + base + ".tsv" in listatsv:
        with open ("r" + base + ".tsv","r") as tsv:
            with open("end/" + base + ".qry","w") as end:
                with open(txtname,"r") as txt:
                    text = txt.read()
                    for l in tsv:
                        x,_,y = l.partition("\t")
                        if l.strip() != '':
                            Queries += 1
                            sys.stdout.write(f"Queries Total: {Queries}\r" )
                            sys.stdout.flush()
                            if y.strip() == "<|answer|>":
                                end.write("<|query|>")
                                end.write(x.strip())
                                end.write("<|answer|>")
                                end.write(text)
                                end.write("<|endoftext|>")
                            else:
                                end.write("<|query|>")
                                end.write(text)
                                end.write("\n"*(random.randint(1,3)))
                                end.write(x.strip())
                                end.write("<|answer|>")
                                end.write(y.strip())
                                end.write("<|endoftext|>")
                            end.write("\n")
print(f"Queries Total: {Queries}" )

