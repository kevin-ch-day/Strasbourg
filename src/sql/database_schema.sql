CREATE TABLE `company_info` (
  `CompanyID` int(11) NOT NULL,
  `CompanyName` varchar(255) NOT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `StockSymbol` varchar(10) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL
);

INSERT INTO `company_info` (`CompanyID`, `CompanyName`, `Location`, `StockSymbol`, `note`) VALUES
(1, 'Equifax Inc.', 'Atlanta, Georgia, USA', 'EFX', NULL),
(2, 'Verizon Communications Inc.', 'New York, New York, USA', 'VZ', NULL),
(3, 'Yahoo! Inc.', 'Sunnyvale, California, USA', 'YHOO', 'Acquired by Verizon Communications Inc. in June 2017'),
(4, 'Whole Foods Market Inc.', 'Austin, Texas, USA', 'AMZN', 'Acquired by Amazon.com, Inc. in 2017'),
(5, 'Dun & Bradstreet Inc.', 'Short Hills, New Jersey, USA', 'DNB', NULL),
(6, 'Marriott International, Inc.', 'Bethesda, Maryland, USA', 'MAR', NULL),
(7, 'Under Armour, Inc.', 'Baltimore, Maryland, USA', 'UAA', NULL),
(8, 'T-Mobile US, Inc.', 'Bellevue, Washington, USA', 'TMUS', NULL),
(9, 'Google Inc.', 'Mountain View, California, USA', 'GOOGL', 'Part of Alphabet Inc. at the time'),
(10, 'Ticketfly, Inc.', 'San Francisco, California, USA', 'EB', 'Owned by Eventbrite, Inc.'),
(11, 'Facebook, Inc.', 'Menlo Park, California, USA', 'META', 'Now Meta Platforms, Inc'),
(12, 'Capital One Financial', 'McLean, Virginia, USA', 'COF', 'Capital One Financial Corporation'),
(13, 'Quest Diagnostics Incorporated', 'Secaucus, New Jersey, USA', 'DGX', NULL),
(14, 'Zynga Inc.', 'San Francisco, California, USA', 'ZNGA', NULL),
(15, 'Twitter, Inc.', 'San Francisco, California, USA', 'TWTR', NULL),
(16, 'SolarWinds Corporation', 'Austin, Texas, USA', 'SWI', NULL),
(17, 'Marriott International, Inc.', 'Bethesda, Maryland, USA', 'MAR', NULL),
(18, 'MGM Resorts International', 'Las Vegas, Nevada, USA', 'MGM', NULL),
(19, 'Sina Weibo', 'Beijing, China', 'WB', 'Weibo Corporation'),
(20, 'Microsoft Corporation', 'Redmond, Washington, USA', 'MSFT', NULL),
(21, 'LinkedIn Corporation', 'Sunnyvale, California, USA', 'MSFT', 'Owned by Microsoft Corporation'),
(22, 'JBS S.A.', 'São Paulo, Brazil', 'JBSAY', NULL),
(23, 'Nvidia Corporation', 'Santa Clara, California, USA', 'NVDA', NULL),
(24, 'Okta, Inc.', 'San Francisco, California, USA', 'OKTA', NULL),
(25, 'Uber Technologies, Inc.', 'San Francisco, California, USA', 'UBER', NULL),
(26, 'Rockstar Games', 'New York, New York, USA', 'TTWO', 'Subsidiary of Take-Two Interactive Software, Inc.'),
(27, 'Block, Inc.', 'San Francisco, California, USA', 'SQ', NULL);

CREATE TABLE `data_breach_disclosures` (
  `DisclosureID` int(11) NOT NULL,
  `CompanyID` int(11) NOT NULL,
  `DisclosureDate` date NOT NULL,
  `Perpetrators` varchar(200) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Impact` text DEFAULT NULL
);

INSERT INTO `data_breach_disclosures` (`DisclosureID`, `CompanyID`, `DisclosureDate`, `Perpetrators`, `Description`, `Impact`) VALUES
(1, 1, '2017-09-07', NULL, 'This breach exposed sensitive information of approximately 147 million consumers, including Social Security numbers, birth dates, addresses, and in some cases, driver\'s license numbers.', NULL),
(2, 2, '2017-06-22', NULL, 'An unprotected AWS storage instance exposed the data of 6 million Verizon customers, including phone numbers, names, and PIN codes used for customer service calls.', NULL),
(3, 4, '2017-09-28', NULL, 'A breach involving unauthorized access to payment card information used in taprooms and full table-service restaurants in some Whole Foods Market stores.', NULL),
(4, 6, '2018-11-30', NULL, 'The breach affected approximately 500 million guests of its Starwood hotel properties. Information compromised included names, phone numbers, email addresses, passport numbers, and travel information.', NULL),
(5, 11, '2018-09-28', NULL, 'Exposed the personal information of up to 50 million users due to a flaw in the platform’s “View As” feature.', NULL),
(6, 7, '2018-03-29', NULL, 'Affected about 150 million MyFitnessPal app users. Compromised data included usernames, email addresses, and hashed passwords.', NULL),
(7, 8, '2018-08-24', NULL, 'Exposed personal information of about 2 million customers, including names, billing zip codes, phone numbers, email addresses, account numbers, and account types.', NULL),
(8, 9, '2018-10-08', NULL, 'A bug in the Google+ API potentially exposed the personal data of up to 500,000 users, including names, email addresses, occupations, and age. This led to the decision to shut down Google+ for consumers.', NULL),
(9, 12, '2019-07-29', NULL, 'Exposed personal information of over 100 million individuals in the U.S. and 6 million in Canada, including names, addresses, credit scores, Social Security numbers, and bank account numbers.', NULL),
(10, 11, '2019-04-03', NULL, 'Stored passwords of hundreds of millions of users in plain text across several of its products, accessible by thousands of its employees.', NULL),
(11, 8, '2019-11-22', NULL, 'Unauthorized access to prepaid wireless accounts, affecting an undisclosed number of customers. Information exposed included billing names, phone numbers, and account information.', NULL),
(12, 16, '2020-12-13', NULL, 'A sophisticated supply chain attack, known as SUNBURST, affecting numerous government agencies and corporations worldwide. Malicious code was inserted into updates for the SolarWinds Orion platform.', NULL),
(13, 17, '2020-03-31', NULL, 'Information of approximately 5.2 million guests was accessed using the login credentials of two employees at a franchise property.', NULL),
(14, 18, '2020-02-20', NULL, 'Details of over 10.6 million guests, including personal and contact information, were leaked online.', NULL),
(15, 19, '2020-03-19', NULL, 'Data of 538 million users, including real names, site usernames, gender, location, and phone numbers for 172 million users, were breached and sold online.', NULL),
(16, 11, '2021-04-03', NULL, 'Personal data of over 530 million users from 106 countries was found on a hacking forum. The data included phone numbers, Facebook IDs, full names, locations, birthdates, and some email addresses.', NULL),
(17, 20, '2021-03-02', NULL, 'A state-sponsored threat actor exploited vulnerabilities in the Microsoft Exchange Server, impacting tens of thousands of organizations globally, including email theft and malware installation.', NULL),
(18, 8, '2021-08-16', NULL, 'Affecting over 50 million current, former, and prospective customers, the breach exposed data including social security numbers, drivers license information, and IMEI numbers.', NULL),
(19, 22, '2021-05-31', NULL, 'The world\'s largest meat processing company was hit by a ransomware attack, significantly disrupting operations in the U.S., Canada, and Australia.', NULL),
(20, 23, '2022-02-23', 'Lapsus$', 'Nvidia experienced a cyberattack compromising employee credentials and proprietary information. The attackers, known as \"Lapsus$\", leaked company data online.', NULL),
(21, 20, '2022-03-22', 'Lapsus$', 'Microsoft confirmed that the \"Lapsus$\" hacking group gained limited access to company systems, including source code repositories, though they stated that customer data and services were not compromised.', NULL),
(22, 24, '2022-03-22', 'Lapsus$', 'Okta, a major identity and access management company, reported a breach involving a subcontractor\'s access by the \"Lapsus$\" group, potentially affecting hundreds of clients.', NULL),
(23, 26, '2022-09-19', NULL, 'Before the official release, footage and details of the highly anticipated game, Grand Theft Auto VI, were leaked online following a hack. The breach raised concerns about cybersecurity measures at the company.', NULL),
(24, 8, '2023-01-19', NULL, NULL, NULL),
(25, 8, '2023-04-28', NULL, NULL, NULL);

CREATE TABLE `dow_jones` (
  `Date` date NOT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `Open` decimal(10,2) DEFAULT NULL,
  `Close` decimal(10,0) DEFAULT NULL,
  `High` decimal(10,2) DEFAULT NULL,
  `Low` decimal(10,2) DEFAULT NULL,
  `Volume` varchar(20) DEFAULT NULL,
  `Change_Percent` decimal(5,2) DEFAULT NULL
);

CREATE TABLE `stock_data` (
  `CompanyID` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Open` decimal(15,6) DEFAULT NULL,
  `High` decimal(15,6) DEFAULT NULL,
  `Low` decimal(15,6) DEFAULT NULL,
  `Close` decimal(15,6) DEFAULT NULL,
  `AdjClose` decimal(15,6) DEFAULT NULL,
  `Volume` int(11) DEFAULT NULL
);