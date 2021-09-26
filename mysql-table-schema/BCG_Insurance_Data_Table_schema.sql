
-- Database: `BCG_Insurance_Data`
--

CREATE DATABASE BCG_Insurance_Data;

-- --------------------------------------------------------


--
-- Table structure for table `customer`
--


CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------
--
-- Table structure for table `policy`
--

CREATE TABLE `policy` (
  `policy_id` int(11) NOT NULL AUTO_INCREMENT,
  `purchase_date` date NOT NULL,
  `premium` decimal(10,2) NOT NULL,
  `fk_customer_id` int(11) NOT NULL,
  `region` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`policy_id`),
  KEY `policy_fk_cust_807bb2_idx` (`fk_customer_id`),
  CONSTRAINT `policy_fk_customer_id_e8727491_fk_customer_customer_id` FOREIGN KEY (`fk_customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------
