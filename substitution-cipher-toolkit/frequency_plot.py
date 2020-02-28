def plot(freqs, PLOT_HEIGHT=20):
    freqs = [(k, freqs[k]) for k in sorted(freqs.keys())]
    max_freq = max([y for (x, y) in freqs])
    step = max_freq/PLOT_HEIGHT
    for i in range(PLOT_HEIGHT):
        print(end='{:.3f} |'.format(max_freq))
        for (x, y) in freqs:
            if y >= max_freq:
                print(end='█ ')
            else:
                print(end='  ')
        max_freq -= step
        print()
    
    print(' '*7 + '--'*len(freqs))
    print(' '*7 + ' '.join([x for (x, y) in freqs]))
