infile=open("values.txt","rt")
outfile=open("value-op.txt","wt")
print("Processing input")

sum=0

for line in infile:
    sum+=int(line)
    print(line.rstrip(),file=outfile)
print("\nTotal:" + str(sum), file=outfile)
outfile.close()
print("Output Complete")