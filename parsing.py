def parse(filename):
    f = open(filename, "r")
    header_read = False
    ls = []
    for line in f:
        if not header_read:
            header_read = True
            continue

        tokens = []
        i = 0
        print(line)
        while i < len(line):
            token = ''
            if line[i] == '"':
                j = i + 1
                while j < len(line) and line[j] != '"':
                    token += line[j]
                    j += 1
                j += 1 # Skip the ending '"'
                i = j + 1  # Skip the ','
            else:
                j = i
                while j < len(line) and line[j] != ',' and line[j] != '\n':
                    token += line[j]
                    j += 1
                i = j + 1 # Skip the ','
            tokens.append(token)
            
        ls.append(tokens[3:])
    return ls

fn = '/Users/zoe/zoeprojects/COVID-19-Data/Socioeconomic Data/Employment/Unemployment Insurance Claims/Weekly report/Unemployment_2020_01_11.csv'
print(parse(fn))
