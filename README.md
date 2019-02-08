Run individual tests scenarios by typing command in Terminal/CMD:
    e.g. python3 <feature_name>

Install required lib's by typing command in Terminal/CMD in project root:
    pip install -r requirements.txt

Testing framework: Behave v1.2.6 , Selenium v3.141.0
Programing language: Python v3.7

Features covered:
    Login
    Sign up
    See personal data


-------TradeCore Challenge---------


URL_SIGNUP: https://demo-biq.dev.tradecore.io/#/
URL_BASE_PORTAL: https://demo-biq.dev.tradecore.io/#/portal/accounts
Install requirements command   pip install -r requirements.txt

Phase 0: Test process preparation

	General Plan:
		- Manual exploratory testing, getting to know with feature
		- Setting up automation testing framework
		- Automation testing
		- Creating Test Plan
		- Creating Testing Remote Repository(GIT Hub) 
		- Resources needed:
			- Men power: 
				- Engineers (3 Persons):
					- Automation testing skills, intermediate - senior, Python, BDD (1 SQA engineer)
						- Responsibilities:
							- Manual testing 
							- Creating test scenarios 
							- Creating test cases
							- Feature coverage with automation scripts
							- Creating Testing Remote Repository(GIT Hub) 
							- Uploading test scripts on created repo
							- [OPTIONAL] CI - Jenkins*
					- SQA Manager (1 SQA engineer/manager)
						- Creating Level of Effort Document(LOE)/Test Plan
					- BA/PO (1 stake holder/engineer/manager)
						- Setting up Business values(Prioritization)
		* DevOps engineer should validate jobs created

Phase 1: Test Plan
	Test Scope
		- Create test scenarios, test cases
		- Read technical and business documentation (User stories, Acceptance criteria, Exit criteria, API documentation, 
            DB structure, Environment setup, Security documentation)
		- Setting up automation testing framework
		- Complete coverage of the features with automation scripts (happy path + edge cases)**
		- Create documentation
		 ** “Depth of testing” should be set by SQA Manager and BA/PO
	Features count:
		- Sign Up
		- Login
		- User Portal Features:
			- Account Summary [TRADING ACCOUNTS]
			- Add new trading account [TRADING ACCOUNTS]
			- Add new demo account [TRADING ACCOUNTS]
			- See personal information’s [MY PROFILE]
		        	- Upload documents [MY PROFILE]
			- Change password [MY PROFILE]
			- Legal documents [MY PROFILE]
			- Deposit funds [PAYMENTS]
			- Withdraw funds [PAYMENTS]
			- Internal transfer [PAYMENTS]
			- Payment history [PAYMENTS]
			-Logout
					
Phase 2: Testing
	Testing approaches, Testing methods, Framework, Programing language, IDE:

		-Testing approaches: Manual, Automation
		-Testing methods: Black box
		-Testing process: BDD
		-Testing framework: Behave v1.2.6 , Selenium v3.141.0
		-Programing language: Python v3.7
		-IDE: PyCharm professional

	Two step signup process feature testing
	
		-Time Estimation : 4 hours(PO/DEV time needed not included)
		-Page Structure:

			- Enter personal informations (STEP 1)
				-Fields:
				- First name (text input field) (required)
				- Last Name (text input field) (required)
				- Email (text input field) (required) (field validation)
				- Password (text input field) (required) (field validation) (Uppercase-lowercase-special characters)
				- Phone number (dropdown menu + text input field) (required)
				- Date of birth (text input field) (required)
				- Post-code (text input field) (required)
				- Address line 1 (text input field) (required)
				- Address line 2 (text input field) (optional)
				- City or Town (text input field) (required)
			-Answer on trading related questions
				-Shares (Frequently, Sometimes, No)
				-Forex (Frequently, Sometimes, No)
				-Cfd's (Frequently, Sometimes, No)
				-Spread betting (Frequently, Sometimes, No)
				-Have you? (Attended a relevant training course, Had experience of working in the financial sector, No other relevant experience)
				-Trading platform(MT5)
				-Approximate Annual Income (Over $100,000, $50,000 - $99,999, $15,000 - $49,999, Less than $15,000)
				-Employment status (Employed, Self Employed, Retired, Unemployed)
				-Approximate value of assets(Over $100,000, $50,000 - $99,999, $5,000 - $49,999, Less than $5,000)

	Two step signup process feature testing:
		-Time Estimation : 25 hours(PO/DEV time needed not included)
		-Page Structure:

			- Account Summary [TRADING ACCOUNTS]
				-Require[Legal Documents]
				-Table [Platform, Account, Currency, Balance, Equity]
				-Button[Download, Deposit[OPTIONAL]]
			- Add new trading account [TRADING ACCOUNTS]
				-DropDown [Currency]
				-Button [Create a new trading account]
			- Add new demo account [TRADING ACCOUNTS]
				-DropDown [Currency]
				-Button [Create a new demo account]
			- See personal information’s [MY PROFILE]
				-User Info table[First name, Last name, Email, Phone, Country, Post code, Date of Birth, Language,
                  Address line 1, Address line 2[OPTIONAL]]
		        	- Upload documents [MY PROFILE]
				-Drag&Drop[ID Proof, ID Proof Back, Address Proof, Additional Customer document 1]:
					Documents must contain all of the following details:
                        * Your full name
                        * A unique ID number
                        * Your birthdate
                        * Your place of birth
                        * A visible photo
                        * Your signature
                        * Your nationality
			- Change password [MY PROFILE]
				- Input fields[Current Password, New Password, Confirm new Password]
				-Button[Save Changes]
			- Legal documents [MY PROFILE]
				-Table[Time and date, Version, Title]
			- Deposit funds [PAYMENTS] TBD
				-Require[Legal Documents]
			- Withdraw funds [PAYMENTS] TBD
				-Require[Legal Documents]
			- Internal transfer [PAYMENTS] TBD
				-Require[Legal Documents]
			- Payment history [PAYMENTS] TBD
				-Require[Legal Documents]
			-Logout
				-Button[Logout]

Phase 2: Improvements, Test steps documentation.
