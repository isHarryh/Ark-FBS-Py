def main(flatc:str, fbs_dir:str, output_dir:str):
    """Compiles FBS files into python scripts.\n
    Preparation: Download [flatc](https://github.com/google/flatbuffers/releases) into the working dir.\n
    Note: `ROOT_TYPE` const will be added to the compiled python scripts for convenience.

    :param flats: Path to the flatc executable;
    :param fbs_dir: Path to the source FBS dir;
    :param output_dir: Path to the output dir;
    """
    import os
    import shutil
    import subprocess

    print("Starting...")
    if os.path.exists(output_dir):
        print(f"Rmdir: {output_dir}")
        shutil.rmtree(output_dir)

    print(f"Mkdir: {output_dir}")
    os.makedirs(output_dir)

    print(f"From: {fbs_dir}")
    count = 0
    for root, _, files in os.walk(fbs_dir):
        for file in files:
            if file.endswith(".fbs"):
                # Compile
                fbs_file = os.path.join(root, file)
                pure_name = os.path.splitext(os.path.basename(fbs_file))[0]
                print(f"Compiling: {fbs_file}")
                subprocess.run([flatc, '--python', '--gen-onefile', '-o', output_dir, fbs_file])
                # Modify
                py_file = os.path.join(output_dir, f'{pure_name}_generated.py')
                root_type_name = get_root_type_name(fbs_file)
                with open(py_file, encoding='UTF-8') as r:
                    content = r.readlines()
                    linesep = '\r\n' if content[0].endswith('\r\n') else '\n'
                    while content[-1] == linesep:
                        content.pop()
                    content.extend([linesep, f'ROOT_TYPE = {root_type_name}', linesep])
                # Replace
                new_file = os.path.join(output_dir, f'{pure_name}.py')
                os.unlink(py_file)
                with open(new_file, 'w', encoding='UTF-8') as w:
                    w.writelines(content)
                count += 1

    print(f"Finished! {count} files done.")

def get_root_type_name(fbs_file):
    import re
    with open(fbs_file, encoding='UTF-8') as f:
        content = f.readlines()
        for l in content:
            match = re.match(r'root_type\s(.+);', l)
            if match:
                return match.group(1)

if __name__ == '__main__':
    main('flatc', 'FBS', 'compiled')
