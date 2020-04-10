"""Main entry point"""

import sys
import os
from optparse import OptionParser
from dowser import server


def main():
    usage = "profile.py [-p port] [-m module | scriptfile] [arg] ..."
    parser = OptionParser(usage=usage)
    parser.allow_interspersed_args = False
    parser.add_option('-p', dest="port", type=int,
        help="Port to run dowser on.", default=8888)
    parser.add_option('-m', dest="module", action="store_true",
        help="Profile a library module.", default=False)

    if not sys.argv[1:]:
        parser.print_usage()
        sys.exit(2)

    (options, args) = parser.parse_args()
    sys.argv[:] = args

    if len(args) > 0:
        if options.module:
            import runpy
            code = "run_module(modname, run_name='__main__')"
            globs = {
                'run_module': runpy.run_module,
                'modname': args[0]
            }
        else:
            progname = args[0]
            sys.path.insert(0, os.path.dirname(progname))
            with open(progname, 'rb') as fp:
                code = compile(fp.read(), progname, 'exec')
            globs = {
                '__file__': progname,
                '__name__': '__main__',
                '__package__': None,
                '__cached__': None,
            }
        with server(port=options.port):
            exec(code, globs, None)
    else:
        parser.print_usage()
    return parser


# When invoked as main program, invoke the profiler on a script
if __name__ == '__main__':
    main()
