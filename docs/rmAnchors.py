import re
#get a list of files in a directory and output all the markdown files in a list
def get_markdown_files(dir):
    markdown_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

#open a file and edit it to remove all anchors from paths
def remove_anchors(file):
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        #remove anchors from paths using regex where a link is in the form [text](path#anchor) but replace the anchor with whitespace the same length as the anchor
        regex = r"\[(.*?)\]\((.*?)#(.*?)\)"
        # replace 3rd group with whitespace the same length as the anchor to preserve formatting
        re.sub(regex, r"[\1](\2" + " " * len(r"\3") + ")", lines)
        f.writelines(lines)

#main function taking in a directory
def main(dir):
    files = get_markdown_files(dir)
    for file in files:
        remove_anchors(file)

if __name__ == "__main__":
    main(sys.argv[1])