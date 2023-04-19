DELIMITER $$
DROP PROCEDURE IF EXISTS add_bike $$
CREATE PROCEDURE add_bike(
    IN bike_id INT,
    IN bike_model_name VARCHAR(255),
    IN bike_manufacturing_year INT,
    IN bike_price FLOAT,
    IN bike_color VARCHAR(255),
    IN bike_description TEXT,
    IN engine_id INT,
    IN showroom_id INT,
    IN policy_number INT
)
BEGIN
    DECLARE showroom_count INT;
    DECLARE engine_count INT;
    DECLARE policy_count INT;

    -- Check if the showroom_id exists
    SELECT COUNT(*) INTO showroom_count FROM Showroom WHERE showroomID = showroom_id;

    IF showroom_count = 0 THEN
        -- If the showroom_id doesn't exist, create a new tuple in the Showroom table
        INSERT INTO Showroom (showroomID) VALUES (showroom_id);
    END IF;

    -- Check if the policy_number exists
    SELECT COUNT(*) INTO policy_count FROM InsurancePolicy WHERE policyNumber = policy_number;

    IF policy_count = 0 THEN
        -- If the policy_number doesn't exist, create a new tuple in the InsurancePolicy table
        INSERT INTO InsurancePolicy (policyNumber) VALUES (policy_number);
    END IF;

    -- Check if the engine_id exists
    SELECT COUNT(*) INTO engine_count FROM BikeEngine WHERE engineID = engine_id;

    IF engine_count = 0 THEN
        -- If the engine_id doesn't exist, create a new tuple in the BikeEngine table
        INSERT INTO BikeEngine (engineID) VALUES (engine_id);
    END IF;

    -- Insert the new bike into the Bike table
    INSERT INTO Bike (bikeID, bikeModelName, bikeManufacturingYear, bikePrice, bikeColor, bikeDescription, engineID, showroomID, policyNumber)
    VALUES (bike_id, bike_model_name, bike_manufacturing_year, bike_price, bike_color, bike_description, engine_id, showroom_id, policy_number);

END $$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS select_all_bikes $$
CREATE PROCEDURE select_all_bikes()
BEGIN
    SELECT * FROM Bike;
END $$
DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS update_bike $$
CREATE PROCEDURE update_bike(
    IN in_bike_id INT,
    IN in_bike_model_name VARCHAR(255),
    IN in_bike_manufacturing_year INT,
    IN in_bike_price FLOAT,
    IN in_bike_color VARCHAR(255),
    IN in_bike_description TEXT,
    IN in_engine_id INT,
    IN in_showroom_id INT,
    IN in_policy_number INT
)
BEGIN
    DECLARE showroom_count INT;
    DECLARE engine_count INT;
    DECLARE policy_count INT;
    DECLARE bike_count INT;

    -- check if the bike with given id exists or not
    SELECT COUNT(*) INTO bike_count FROM Bike WHERE bikeID = in_bike_id;

    IF bike_count = 0 THEN
        -- If the bike_id doesn't exist, show a message
        SELECT CONCAT('Bike with ID ', in_bike_id, ' was not found.') AS Message;
    END IF;

    -- Check if the showroom_id exists
    SELECT COUNT(*) INTO showroom_count FROM Showroom WHERE showroomID = in_showroom_id;
    IF showroom_count = 0 THEN
        -- If the showroom_id doesn't exist, create a new tuple in the Showroom table
        INSERT INTO Showroom (showroomID) VALUES (in_showroom_id);
    END IF;

    -- Check if the policy_number exists
    SELECT COUNT(*) INTO policy_count FROM InsurancePolicy WHERE policyNumber = in_policy_number;

    IF policy_count = 0 THEN
        -- If the policy_number doesn't exist, create a new tuple in the InsurancePolicy table
        INSERT INTO InsurancePolicy (policyNumber) VALUES (in_policy_number);
    END IF;

    -- Check if the engine_id exists
    SELECT COUNT(*) INTO engine_count FROM BikeEngine WHERE engineID = in_engine_id;

    IF engine_count = 0 THEN
        -- If the engine_id doesn't exist, create a new tuple in the BikeEngine table
        INSERT INTO BikeEngine (engineID) VALUES (in_engine_id);
    END IF;

    -- Update the bike in the Bike table
	UPDATE Bike
	SET bikeModelName = CASE WHEN in_bike_model_name IS NULL OR in_bike_model_name = '' THEN bikeModelName ELSE in_bike_model_name END,
    bikeManufacturingYear = COALESCE(in_bike_manufacturing_year, bikeManufacturingYear),
    bikePrice = COALESCE(in_bike_price, bikePrice),
    bikeColor = CASE WHEN in_bike_color IS NULL OR in_bike_color = '' THEN bikeColor ELSE in_bike_color END,
    bikeDescription = CASE WHEN in_bike_description IS NULL THEN bikeDescription ELSE in_bike_description END,
    engineID = COALESCE(in_engine_id, engineID),
    showroomID = COALESCE(in_showroom_id, showroomID),
    policyNumber = COALESCE(in_policy_number, policyNumber)
	WHERE bikeID = in_bike_id;
END $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS delete_bike$$
CREATE PROCEDURE delete_bike(IN bike_id INT)
BEGIN
    DECLARE bike_count INT;

    -- Check if the bike_id exists
    SELECT COUNT(*) INTO bike_count FROM Bike WHERE bikeID = bike_id;

    IF bike_count = 0 THEN
        -- If the bike_id doesn't exist, show a message
        SELECT 'The bike with given ID  does not exist' AS Message;
    ELSE
        -- Delete the bike from the Bike table
        DELETE FROM Bike WHERE bikeID = bike_id;
        SELECT CONCAT('The bike with ID ', bike_id, ' deleted successfully.') AS message;
    END IF;
END $$
DELIMITER ;




    DELIMITER //
    DROP PROCEDURE IF EXISTS authenticate_user //
    CREATE PROCEDURE authenticate_user (
    IN p_username VARCHAR(255),
    IN p_password VARCHAR(255)
    )
    BEGIN
    DECLARE user_count INT DEFAULT 0;
    SELECT COUNT(*) INTO user_count FROM users WHERE username = p_username AND password = p_password;

    IF user_count > 0 THEN
        SELECT CONCAT(user_type) AS message FROM users WHERE username = p_username AND password = p_password;
    END IF;
    END //
    DELIMITER ;


DELIMITER //
drop procedure if exists signup_user //
CREATE PROCEDURE signup_user (IN p_username VARCHAR(50), IN p_password VARCHAR(255))
BEGIN
INSERT INTO users (username, password)
VALUES (p_username, p_password);
END //
DELIMITER ;


    -- Procedures for insurance company crud

    DELIMITER //
    DROP PROCEDURE IF EXISTS add_insurance_company //
    CREATE PROCEDURE add_insurance_company (
    IN p_taxationID VARCHAR(255),
    IN p_companyName VARCHAR(255),
    IN p_companyAddress VARCHAR(255),
    IN p_companyEmail VARCHAR(255),
    IN p_companyWebsite VARCHAR(255),
    IN p_companyRating INT,
    IN p_policyTypes VARCHAR(255)
    )
    BEGIN
    INSERT INTO InsuranceCompany
    (taxationID, companyName, companyAddress, companyEmail, companyWebsite, companyRating, policyTypes)
    VALUES (p_taxationID, p_companyName, p_companyAddress, p_companyEmail, p_companyWebsite, p_companyRating, p_policyTypes);
    END //
    DELIMITER ;

    DELIMITER //
    DROP PROCEDURE IF EXISTS read_insurance_company //
    CREATE PROCEDURE read_insurance_company ()
    BEGIN
    SELECT * FROM InsuranceCompany;
    END //
    DELIMITER ;

    DELIMITER //
    DROP PROCEDURE IF EXISTS update_insurance_company //
    CREATE PROCEDURE update_insurance_company (
    IN p_taxationID VARCHAR(255),
    IN p_companyName VARCHAR(255),
    IN p_companyAddress VARCHAR(255),
    IN p_companyEmail VARCHAR(255),
    IN p_companyWebsite VARCHAR(255),
    IN p_companyRating INT,
    IN p_policyTypes VARCHAR(255)
    )
    BEGIN
    UPDATE InsuranceCompany SET companyName = p_companyName, companyAddress = p_companyAddress, companyEmail = p_companyEmail,
    companyWebsite = p_companyWebsite, companyRating = p_companyRating, policyTypes = p_policyTypes WHERE taxationID = p_taxationID;
    END //
    DELIMITER ;


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


DELIMITER //
    DROP PROCEDURE IF EXISTS delete_showroom //
    CREATE PROCEDURE delete_showroom(showroom_id INT)
    BEGIN
    DECLARE row_count INT;
    SET row_count = 0;
    SELECT COUNT(*) INTO row_count FROM Showroom WHERE showroomID = showroom_id;
    IF row_count = 0 THEN
        SELECT 'No showroom found with the given ID.' AS message;
    ELSE
        DELETE FROM Showroom WHERE showroomID = showroom_id;
        SELECT CONCAT('Showroom with ID ', showroom_id, ' deleted successfully.') AS message;
    END IF;
    END //
DELIMITER ;



DELIMITER $$
DROP PROCEDURE IF EXISTS update_bike_availability $$
CREATE PROCEDURE update_bike_availability(
    IN p_bikeID INT
)
BEGIN
    UPDATE Bike SET isAvailable = 0 WHERE bikeID = p_bikeID;
END $$
DELIMITER ;



DELIMITER //
DROP PROCEDURE IF EXISTS add_employee //
CREATE PROCEDURE add_employee(
    IN emp_id INT,
    IN name VARCHAR(255),
    IN email VARCHAR(255),
    IN phone VARCHAR(10),
    IN salary INT,
    IN designation VARCHAR(255),
    IN joinDate DATE,
    IN showroom_id INT
)
BEGIN
    INSERT INTO Employees (employeeID, employeeName, employeeEmail, employeePhone, employeeSalary, employeeDesignation, employeeJoiningDate, showroomID)
    VALUES (emp_id, name, email, phone, salary, designation, joinDate, showroom_id);
END //
DELIMITER ;


DELIMITER //
DROP PROCEDURE IF EXISTS select_all_employees //
CREATE PROCEDURE select_all_employees()
BEGIN
    SELECT * FROM Employees;
END //
DELIMITER ;


DELIMITER //
DROP PROCEDURE IF EXISTS update_employee //
CREATE PROCEDURE update_employee(
	IN emp_id INT,
    IN name VARCHAR(255),
    IN email VARCHAR(255),
    IN phone VARCHAR(10),
    IN salary INT,
    IN designation VARCHAR(255),
    IN joinDate DATE,
    IN showroom_id INT
)
BEGIN
    UPDATE Employees
    SET name = name,
		employeePhone = phone,
        employeeEmail = email,
		employeeSalary = salary,
        employeeDesignation = designation,
        employeeJoiningDate = joinDate,
        showroomID = showroom_id
    WHERE employeeID = employeeID;
END //
DELIMITER ;


DELIMITER //
DROP PROCEDURE IF EXISTS delete_employee //
CREATE PROCEDURE delete_employee(IN emp_id INT)
BEGIN
  DELETE FROM employees WHERE id = emp_id;
  SELECT ROW_COUNT();
END //
DELIMITER ;