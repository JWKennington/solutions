import argparse
import pathlib
from solman.soln import SolutionGroup


ROOT = pathlib.Path(__file__).parent
GROUPS = [x.name for x in ROOT.iterdir() if x.is_dir()]


def parse():
    parser = argparse.ArgumentParser(description='Build Solutions')
    parser.add_argument('-g', type=str, help='Name of the subdirectory to build')
    parser.add_argument('-o', type=str, help='latex or pdf', default='pdf')
    return parser.parse_args()


def main():
    args = parse()
    group_root = args.g
    if group_root not in GROUPS:
        raise ValueError('Unknown group {}, available: {}'.format(group_root, GROUPS))
    group_root = ROOT / group_root 
    group_meta = group_root / 'meta.yml'
    g = SolutionGroup.from_meta(group_meta)
    if args.o == 'pdf':
        g.to_pdf(outfile=group_root / 'solns.pdf')
    elif args.o == 'latex':
        g.to_latex(outfile=group_root / 'solns.tex')
    else:
        raise ValueError('Unknown output format {}, available: {}'.format(args.o, 'pdf, latex'))

if __name__ == '__main__':
    main()
