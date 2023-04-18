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
    SET bikeModelName = in_bike_model_name,
        bikeManufacturingYear = in_bike_manufacturing_year,
        bikePrice = in_bike_price,
        bikeColor = in_bike_color,
        bikeDescription = in_bike_description,
        engineID = in_engine_id,
        showroomID = in_showroom_id,
        policyNumber = in_policy_number
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

