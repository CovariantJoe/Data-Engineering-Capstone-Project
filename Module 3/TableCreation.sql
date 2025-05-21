BEGIN;


CREATE TABLE IF NOT EXISTS public."softcartFactSales"
(
    "orderID" integer NOT NULL,
    "categoryID" integer NOT NULL,
    price double precision NOT NULL,
    "countryID" integer NOT NULL,
    "dateID" integer NOT NULL,
    PRIMARY KEY ("orderID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimItem"
(
    "itemID" integer NOT NULL,
    "itemName" character varying(45) NOT NULL,
    PRIMARY KEY ("itemID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimDate"
(
    "dateID" integer NOT NULL,
    date date NOT NULL,
    day integer NOT NULL,
    weekday integer NOT NULL,
    "weekdayName" character varying(12) NOT NULL,
    month integer NOT NULL,
    "monthName" character varying(15) NOT NULL,
    year integer NOT NULL,
    quarter integer NOT NULL,
    "quarterName" character varying(12) NOT NULL,
    PRIMARY KEY ("dateID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimCountry"
(
    "countryID" integer NOT NULL,
    "countryName" character varying(30) NOT NULL,
    PRIMARY KEY ("countryID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimCategory"
(
    "categoryID" integer NOT NULL,
    "categoryName" character varying(50) NOT NULL,
    PRIMARY KEY ("categoryID")
);

ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("categoryID")
    REFERENCES public."softcartDimCategory" ("categoryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("countryID")
    REFERENCES public."softcartDimCountry" ("countryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("dateID")
    REFERENCES public."softcartDimDate" ("dateID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
