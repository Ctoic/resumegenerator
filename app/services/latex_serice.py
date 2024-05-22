import os
from subprocess import Popen, PIPE

def compile_latex(latex_code):
    tex_file = '/tmp/resume.tex'
    with open(tex_file, 'w') as f:
        f.write(latex_code)

    process = Popen(['pdflatex', '-output-directory', '/tmp', tex_file], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(f"LaTeX compilation failed: {stderr.decode()}")

    return 'resume.pdf'
