def read_lines_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def write_script(character1_lines, character2_lines):
    script_lines = []
    i = 0
    j = 0
    while i < len(character1_lines) and j < len(character2_lines):
        script_lines.append(character1_lines[i].strip())
        if '$$$' in character1_lines[i]:
            while '$$$' in character1_lines[i]:
                user_input = input(f"Replace '{character1_lines[i].strip()}' with a line (at least 3 words): ")
                if len(user_input.split()) >= 3:
                    script_lines[-1] = user_input.strip()
                    break
                else:
                    print("Please enter a line with at least 3 words.")
        i += 1

        script_lines.append(character2_lines[j].strip())
        j += 1

    while i < len(character1_lines):
        script_lines.append(character1_lines[i].strip())
        if '$$$' in character1_lines[i]:
            while '$$$' in character1_lines[i]:
                user_input = input(f"Replace '{character1_lines[i].strip()}' with a line (at least 3 words): ")
                if len(user_input.split()) >= 3:
                    script_lines[-1] = user_input.strip()
                    break
                else:
                    print("Please enter a line with at least 3 words.")
        i += 1

    try:
        with open('script.txt', 'w', encoding='utf-8') as script_file:
            for line in script_lines:
                script_file.write(line + '\n')
        print("Script is ready! Check script.txt.")
    except IOError:
        print("Error writing to script.txt. Check file permissions or disk space.")



character1_lines = read_lines_from_file('file.txt')
character2_lines = read_lines_from_file('file1.txt')

if not character1_lines:
    print("No content found in file.txt.")
if not character2_lines:
    print("No content found in file1.txt.")

write_script(character1_lines, character2_lines)