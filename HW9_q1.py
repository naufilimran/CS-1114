####Author: Naufil Bin Imran
##Assignment / Part: HW9 - Q1
##Date due: 2022-04-28
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct

def get_nucleotide_frequencies(nucleotide):
    junk_keys="Junk"
    dictionary = {junk_keys:{}}
    nucleotide=nucleotide.upper()
    valid = "ACTG"
    for character in nucleotide:
        if character in valid:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        else:
            if character in dictionary[junk_keys]:
                dictionary[junk_keys][character] += 1
            else:
                dictionary[junk_keys][character] = 1
             
    return dictionary

def main():
    frequencies = get_nucleotide_frequencies("ACTGTCACGRFRTNHYCTCGACCSGTGTCACGT")
    print(frequencies)

if __name__ == '__main__':
    main()
