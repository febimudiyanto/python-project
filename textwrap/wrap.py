import textwrap

def wrap(string, max_width):
    '''
    input: string and integer
    output: string with "\n" spartator
    '''
    return "\n".join(textwrap.wrap(string, width=max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
