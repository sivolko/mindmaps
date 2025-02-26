import os

def get_files_in_folder(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def update_index_html():
    cybersecurity_files = get_files_in_folder('Cybersecurity')
    llm_security_files = get_files_in_folder('LLM Security')

    options = []
    for file in cybersecurity_files:
        options.append(f'<option value="Cybersecurity/{file}">Cybersecurity - {file.replace(".html", "")}</option>')

    for file in llm_security_files:
        options.append(f'<option value="LLM Security/{file}">LLM Security - {file.replace(".html", "")}</option>')

    with open('index.html', 'r') as file:
        lines = file.readlines()

    with open('index.html', 'w') as file:
        for line in lines:
            if '<select id="folderSelect">' in line:
                file.write(line)
                file.write('\n'.join(options))
                file.write('\n')
            elif '</select>' in line:
                continue
            else:
                file.write(line)

if __name__ == "__main__":
    update_index_html()
