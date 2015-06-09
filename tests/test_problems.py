from hacksport.deploy import deploy_problem

from os.path import join, realpath, dirname

PATH = dirname(realpath(__file__))

class TestProblems:
    """
    Regression tests for compiled problems.
    """

    def test_compiled_sources(self):
        deploy_problem(join(PATH, "problems/compiled_sources"))

    def test_remote_compiled_makefile_template(self):
        deploy_problem(join(PATH, "problems/remote_compiled_makefile_template"))

    def test_remote_no_compile(self):
        deploy_problem(join(PATH, "problems/remote_no_compile"))

    def test_compiled_sources_url(self):
        deploy_problem(join(PATH, "problems/compiled_sources_url"))
