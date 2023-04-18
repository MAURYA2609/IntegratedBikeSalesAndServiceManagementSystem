DELIMITER //
DROP PROCEDURE IF EXISTS authenticate_user //
CREATE PROCEDURE authenticate_user (
IN p_username VARCHAR(255),
IN p_password VARCHAR(255),
OUT p_user_type VARCHAR(50)
)
BEGIN
SELECT COUNT(*) INTO @count FROM users WHERE username = p_username AND password = p_password;

IF @count > 0 THEN
	SELECT user_type INTO p_user_type FROM users WHERE username = p_username AND password = p_password;
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



DELIMITER //
DROP PROCEDURE IF EXISTS delete_bike//

CREATE PROCEDURE delete_bike(IN bike_id INT)
BEGIN
DELETE FROM Bike WHERE bikeID = bike_id;

IF ROW_COUNT() = 0 THEN
	SELECT "No bike with ID ", bike_id, " found.";
ELSE
	SELECT "Bike with ID ", bike_id, " deleted successfully.";
END IF;
END//

DELIMITER ;
