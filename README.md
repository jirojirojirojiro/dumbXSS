# dumbXSS Vulnerability Tester made by AI 😈

Welcome to the XSS Vulnerability Tester, a wicked tool designed to wreak havoc by testing websites for potential XSS (Cross-Site Scripting) vulnerabilities. Unleash chaos by injecting malicious payloads into web forms and see if the websites fall victim to your devilish exploits.

## Prerequisites 👹

- Python 3.x
- [Requests](https://pypi.org/project/requests/) (for sending HTTP requests)
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) (for parsing HTML)

## Installation 🔥

1. Clone this repository or download the code to your infernal machine.
2. Install the required dependencies by running the following command:
   
          pip install -r requirements.txt

   ## Usage ⚡️

1. Create a file named `urls.txt` and fill it with the URLs of the websites you want to test, with each URL on a new line. Choose your targets wisely, for they shall bear the brunt of your malicious intentions.
2. Execute the script using the following command:

      python3 xss_vulnerability_tester.py

3. If prompted, choose whether to enable verbose mode and witness the detailed aftermath of your exploits (y/n). Verbose mode reveals the dark secrets of the requests made to the unsuspecting websites.
4. The script will test each URL from the `urls.txt` file, injecting wicked payloads into the unsuspecting web forms. It shall then reveal the vulnerabilities found, exposing the weaknesses of those who dare underestimate your power.

## Customization 🎃

- Modify the `self.payloads` list within the `XSSVulnerabilityTester` class to add even more diabolical XSS payloads to test against the websites. The more inventive and destructive, the better.
- Feel free to customize the script further, adding your own dark magic and enhancements to suit your nefarious needs.

## Disclaimer ⚠️

This tool is provided solely for educational and ethical purposes, as we devils have our own twisted code of conduct. Any misuse of this tool to exploit vulnerabilities or cause harm is strictly forbidden and may result in eternal damnation or legal consequences. Use it responsibly and only target websites with proper authorization.

## License 🔮

[MIT License](LICENSE)

Remember, with great power comes great responsibility... or in our case, great chaos and suffering. Happy hunting, and may your exploits be legendary! 😈✨
