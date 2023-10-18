# main.py

from set import ascii_art
from xss_vulnerability_tester import XSSVulnerabilityTester

if __name__ == "__main__":
    verbose_mode = input("Enable verbose mode? (y/n): ").lower() == "y"
    ascii_art.print_jirojiro_art()
    tester = XSSVulnerabilityTester("urls.txt", verbose=verbose_mode)
    tester.run_tests()
