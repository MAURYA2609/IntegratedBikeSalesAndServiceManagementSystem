	create database ibssms;

	use ibssms;


	create table users(
		id integer PRIMARY KEY NOT NULL auto_increment,
		username varchar(255) not null,
		password varchar(255) not null,
		user_type varchar(255) default "customer"
	);

	CREATE TABLE InsuranceCompany (
		taxationID INT PRIMARY KEY NOT NULL,
		companyName VARCHAR(255),
		companyAddress VARCHAR(255),
		companyEmail VARCHAR(255),
		companyWebsite VARCHAR(255),
		companyRating INT,
		policyTypes ENUM('Home Insurance', 'Auto Insurance', 'Motorcycle Insurance')
	);

	CREATE TABLE BikeEngine(
		engineID INT PRIMARY KEY NOT NULL,
		manufacturingYear INT,
		engineType VARCHAR(255),
		engineDisplacement INT,
		engineWeight INT,
		engineFuelType VARCHAR(255),
		enginefuelEfficiency VARCHAR(255),
		engineTorque INT,
		engineHorsePower INT
	);

	CREATE TABLE Service(
		serviceID INT PRIMARY KEY NOT NULL,
		serviceOnDate DATE,
		serviceDetails VARCHAR(255),
		serviceCharges INT,
		newPartsCharges INT,
		serviceType ENUM('Paid', 'Unpaid')
	);

	CREATE TABLE PaymentDetails (
		paymentDetailsID INT PRIMARY KEY NOT NULL,
		paymentMethod ENUM('Debit Card', 'Credit Card'),
		paymentDate DATE,
		paymentAmount INT,
		invoiceNumber INT
	);



	CREATE TABLE Showroom(
		showroomID INT PRIMARY KEY NOT NULL,
		showroomName VARCHAR(255),
		showroomAddress VARCHAR(255),
		showroomEmail VARCHAR(255),
		showroomPhone VARCHAR(10)
	);


	CREATE TABLE Employees(
		employeeID INT PRIMARY KEY NOT NULL,
		employeeName VARCHAR(255),
		employeePhone VARCHAR(10),
		employeeEmail VARCHAR(255),
		employeeSalary INT,
		employeeDesignation VARCHAR(255),
		employeeJoiningDate DATE,
		showroomID INT,
		
		CONSTRAINT employee_showroom_fk FOREIGN KEY (showroomID) REFERENCES Showroom(showroomID)
			ON UPDATE RESTRICT
			ON DELETE RESTRICT
	);

	CREATE TABLE EmployeeManager(
		employeeID INT PRIMARY KEY NOT NULL,
		CONSTRAINT employee_empManager_fk FOREIGN KEY (employeeID) REFERENCES Employees(employeeID)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);


	CREATE TABLE InsurancePolicy (
		policyNumber INT PRIMARY KEY NOT NULL,
		insStartDate DATE,
		insEndDate DATE, 
		insCoverageDetails VARCHAR(255),
		insPremium INT,
		noOfServices INT,
		employeeID INT,
		taxationID INT NOT NULL,
		
		CONSTRAINT policy_manager_fk FOREIGN KEY (employeeID) REFERENCES EmployeeManager(employeeID)
			ON UPDATE CASCADE
			ON DELETE SET NULL,
			
		CONSTRAINT policy_company_fk FOREIGN KEY (taxationID) REFERENCES InsuranceCompany(taxationID)
			ON UPDATE CASCADE
			ON DELETE CASCADE
	);



	CREATE TABLE Bike(
		bikeID INT PRIMARY KEY NOT NULL,
		bikeModelName VARCHAR(255),
		bikeManufacturingYear INT,
		bikePrice INT,
		bikeColor VARCHAR(255),
		bikeDescription VARCHAR(255),
		engineID INT ,
		showroomID INT,
		policyNumber INT ,
		
		CONSTRAINT bike_engine_fk FOREIGN KEY (engineID) REFERENCES BikeEngine(engineID)
			ON UPDATE CASCADE
			ON DELETE SET NULL,
			
		CONSTRAINT bike_showroom_fk FOREIGN KEY (showroomID) REFERENCES Showroom(showroomID)
			ON UPDATE CASCADE
			ON DELETE SET NULL,
			
		CONSTRAINT bike_policy_fk FOREIGN KEY (policyNumber) REFERENCES InsurancePolicy(policyNumber)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);


	CREATE TABLE Booking (
		bookingID INT PRIMARY KEY NOT NULL,
		bookingDate DATE,
		deliveryDate DATE,
		isDelivered BOOLEAN,
		paymentDetailsID INT ,
		CONSTRAINT booking_payment_fk FOREIGN KEY (paymentDetailsID) REFERENCES PaymentDetails(paymentDetailsID)
			ON UPDATE CASCADE
			ON DELETE SET NULL
	);


	CREATE TABLE Customer(
		customerID INT PRIMARY KEY NOT NULL,
		customerName VARCHAR(255),
		customerAddress VARCHAR(255),
		customerPhone INT,
		customerDOB DATE
	);

	CREATE TABLE ServiceAppointment(
		appointmentID INT PRIMARY KEY NOT NULL,
		appointmentDate DATE,
		appointmentTime TIME,
		approxServiceDetails VARCHAR(255),
		policyNumber INT,
		serviceID INT NOT NULL,
		
		CONSTRAINT appointment_policy_fk FOREIGN KEY (policyNumber) REFERENCES InsurancePolicy(policyNumber)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
			
		CONSTRAINT service_appointment_fk FOREIGN KEY (serviceID) REFERENCES Service(serviceID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE
	);

	CREATE TABLE schedules(
		customerID INT,
		bikeID INT,
		appointmentID INT,
		
		CONSTRAINT schedule_customer_fk FOREIGN KEY (customerID) REFERENCES Customer(customerID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
			
		CONSTRAINT schedule_bike_fk FOREIGN KEY (bikeID) REFERENCES Bike(bikeID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
			
		CONSTRAINT schedule_appointment_fk FOREIGN KEY (appointmentID) REFERENCES ServiceAppointment(appointmentID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE
	);

	CREATE TABLE makes (
		bikeID INT,
		customerID INT,
		bookingiD INT,
		
		CONSTRAINT makes_bike_fk FOREIGN KEY (bikeID) REFERENCES Bike(bikeID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
			
		CONSTRAINT makes_customer_fk FOREIGN KEY (customerID) REFERENCES Customer(customerID)
			ON DELETE RESTRICT
			ON UPDATE CASCADE,
			
		CONSTRAINT makes_booking_fk FOREIGN KEY (bookingiD) REFERENCES Booking(bookingiD)
			ON DELETE RESTRICT
			ON UPDATE CASCADE
	);

	INSERT INTO InsuranceCompany (taxationID, companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes) VALUES
	(101, 'ABC Insurance', '123 Main Street, Anytown, USA', 'info@abcinsurance.com', 'www.abcinsurance.com', 4, 'Home Insurance'),
	(102, 'XYZ Insurance', '456 Oak Ave, Somewhere, USA', 'info@xyzinsurance.com', 'www.xyzinsurance.com', 3, 'Auto Insurance'),
	(103, 'PQR Insurance', '789 Maple St, Nowhere, USA', 'info@pqinsurance.com', 'www.pqinsurance.com', 5, 'Home Insurance'),
	(104, 'LMN Insurance', '321 Elm St, Anytown, USA', 'info@lmninsurance.com', 'www.lmninsurance.com', 4, 'Motorcycle Insurance'),
	(105, 'EFG Insurance', '567 Cedar Rd, Somewhere, USA', 'info@efginsurance.com', 'www.efginsurance.com', 3, 'Motorcycle Insurance');

	INSERT INTO BikeEngine (engineID, manufacturingYear, engineType, engineDisplacement, engineWeight, engineFuelType, enginefuelEfficiency, engineTorque, engineHorsePower) VALUES
	(1, 2022, 'V-twin', 1200, 150, 'Petrol', '20 km/l', 100, 100),
	(2, 2021, 'Inline-four', 1000, 120, 'Petrol', '18 km/l', 90, 120),
	(3, 2023, 'Parallel-twin', 650, 80, 'Petrol', '25 km/l', 70, 80),
	(4, 2022, 'Single-cylinder', 350, 50, 'Petrol', '30 km/l', 40, 30),
	(5, 2020, 'V-twin', 1600, 200, 'Petrol', '15 km/l', 150, 160);


	INSERT INTO Service (serviceID, serviceOnDate, serviceDetails, serviceCharges, newPartsCharges, serviceType)
	VALUES 
		(1, '2022-01-15', 'Oil change and filter replacement', 50, 20, 'Paid'),
		(2, '2022-02-28', 'Brake pads replacement', 100, 60, 'Paid'),
		(3, '2022-03-12', 'Chain cleaning and adjustment', 30, 0, 'Unpaid'),
		(4, '2022-04-05', 'Tire replacement', 150, 80, 'Paid'),
		(5, '2022-05-23', 'Battery replacement', 80, 40, 'Unpaid');



	INSERT INTO PaymentDetails (paymentDetailsID, paymentMethod, paymentDate, paymentAmount, invoiceNumber)
	VALUES
	(1, 'Debit Card', '2022-01-01', 1000, 12345),
	(2, 'Credit Card', '2022-01-02', 2000, 12346),
	(3, 'Debit Card', '2022-01-03', 3000, 12347),
	(4, 'Credit Card', '2022-01-04', 4000, 12348),
	(5, 'Debit Card', '2022-01-05', 5000, 12349);

	INSERT INTO Showroom (showroomID, showroomName, showroomAddress, showroomEmail, showroomPhone)
	VALUES 
	(1, 'ABC Motors', '123 Main St', 'abc@example.com', 1234567890),
	(2, 'XYZ Bikes', '456 Oak Ave', 'xyz@example.com', 9876543210),
	(3, 'PQR Motors', '789 Elm St', 'pqr@example.com', 5551234567),
	(4, 'LMN Bikes', '101 Maple Rd', 'lmn@example.com', 7778889999),
	(5, 'DEF Motors', '555 Pine St', 'def@example.com', 8885551234);


	INSERT INTO Employees(employeeID, employeeName, employeePhone, employeeEmail, employeeSalary, employeeDesignation, employeeJoiningDate, showroomID) VALUES
	(101, 'John Doe', 1234567890, 'johndoe@example.com', 50000, 'Sales Manager', '2020-01-01', 1),
	(102, 'Jane Smith', 2345678901, 'janesmith@example.com', 45000, 'Sales Associate', '2020-02-01', 1),
	(103, 'Bob Johnson', 3456789012, 'bobjohnson@example.com', 60000, 'Service Manager', '2019-12-01', 2),
	(104, 'Alice Brown', 4567890123, 'alicebrown@example.com', 55000, 'Service Advisor', '2021-01-01', 2),
	(105, 'Mike Lee', 5678901234, 'mikelee@example.com', 70000, 'Parts Manager', '2019-11-01', 3);


	INSERT INTO EmployeeManager(employeeID) VALUES (101), (102), (103), (104), (105);


	INSERT INTO InsurancePolicy (policyNumber, insStartDate, insEndDate, insCoverageDetails, insPremium, noOfServices, employeeID, taxationID) 
	VALUES 
		(1, '2023-01-01', '2023-12-31', 'Health insurance', 1000, 12, 101, 101),
		(2, '2023-02-01', '2023-12-31', 'Life insurance', 2000, 6, 102, 102),
		(3, '2023-03-01', '2023-12-31', 'Home insurance', 1500, 9, 103, 03),
		(4, '2023-04-01', '2023-12-31', 'Car insurance', 1200, 10, 104, 104),
		(5, '2023-05-01', '2023-12-31', 'Travel insurance', 800, 4, 105, 105);


	INSERT INTO Bike (bikeID, bikeModelName, bikeManufacturingYear, bikePrice, bikeColor, bikeDescription, engineID, showroomID, policyNumber)
	VALUES
	(1, 'Ninja 400', 2021, 6500, 'Green', 'Sport bike with great handling', 1, 1, 1),
	(2, 'Harley-Davidson Street Glide', 2022, 25000, 'Black', 'Cruiser with classic styling', 2, 2, 2),
	(3, 'Honda Gold Wing', 2020, 30000, 'Red', 'Touring bike with lots of features', 3, 1, 3),
	(4, 'BMW S 1000 RR', 2021, 20000, 'Blue', 'High-performance sport bike', 4, 3, 4),
	(5, 'Ducati Scrambler', 2022, 12000, 'Yellow', 'Retro-inspired bike with off-road capability', 5, 2, 5);


	INSERT INTO Customer (customerID, customerName, customerAddress, customerPhone, customerDOB)
	VALUES
	(1, 'John Doe', '123 Main St, Anytown', 5551234, '1985-01-01'),
	(2, 'Jane Smith', '456 Broad St, Somewhere', 5555678, '1990-05-15'),
	(3, 'Bob Johnson', '789 1st Ave, Anytown', 5559876, '1980-11-30'),
	(4, 'Alice Williams', '101 Maple St, Anytown', 5552468, '1995-03-20'),
	(5, 'David Brown', '789 Elm St, Somewhere', 5558642, '1988-07-05');



	INSERT INTO ServiceAppointment (appointmentID, appointmentDate, appointmentTime, approxServiceDetails, policyNumber, serviceID) 
	VALUES 
		(1, '2022-05-01', '10:00:00', 'Oil change, Brake pad replacement', 111, 3),
		(2, '2022-05-03', '14:00:00', 'Chain adjustment, Tyre rotation', 112, 4),
		(3, '2022-05-05', '11:00:00', 'Engine tuning, Spark plug replacement', 113, 2),
		(4, '2022-05-06', '09:00:00', 'Battery replacement, Electrical system check', 114, 1),
		(5, '2022-05-10', '13:00:00', 'Fuel system cleaning, Air filter replacement', 115, 5);


	INSERT INTO schedules (customerID, bikeID, appointmentID) 
	VALUES 
		(1, 1, 1),
		(2, 3, 2),
		(3, 5, 3),
		(4, 2, 4),
		(5, 4, 5);

	INSERT INTO makes (bikeID, customerID, bookingiD)
	VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5);




DELIMITER //
DROP PROCEDURE IF EXISTS delete_insurance_company //
CREATE PROCEDURE delete_insurance_company(taxation_id INT)
BEGIN
    DECLARE row_count INT;
    SET row_count = 0;
    SELECT COUNT(*) INTO row_count FROM InsuranceCompany WHERE taxationID = taxation_id;
    IF row_count = 0 THEN
        SELECT 'No insurance company found with the given taxation ID.' AS message;
    ELSE
        DELETE FROM InsuranceCompany WHERE taxationID = taxation_id;
        SELECT CONCAT('Insurance company with taxation ID ', taxation_id, ' deleted successfully.') AS message;
    END IF;
END //
DELIMITER ;
