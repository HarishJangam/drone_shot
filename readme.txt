/************* Drone-Shot booking system ************/

******************** Database schema *****************
    customer:
        attributes:
            1. name : string
            2. email: string
            3. phone_number : string
            4. address : string
            5. active : bool
            6. customer_id : int

        Example : 
            {
                "name": "Jangam Harish",
                "email": "jangam@gmail.com",
                "phone_number": "8947274719",
                "address": "3-45, Fathepur",
                "active": true,
                "customer_id": CUST00000001
            }

    droneshot:
        attributes:
            1. drone_id : int
            2. nick_name: string
            3. shot_type : string
            4. specifications : string
            5. price : int
            6. active : int

        Example : 
            {
                "drone_id": 29219292852,
                "nick_name": "skyhigh",
                "shot_type": "180-degree shot",
                "specifications": "In this cinematic shot, two or more characters must be in the same imaginary line with each other.",
                "price": 4000,
                "active": true           
            }


    location:
        attributes:
            1. address : string
            2. city: string
            3. district : string
            4. state : string
            5. pincode : int

        Example : 
            {
                "address": "3,52 uppal",
                "city": "hyderabad",
                "district": "rangareddy",
                "state": "telangana",
                "pincode": 506167
            }

    booking:
        attributes:
            1. customer_id : int -> reference to customer schema
            2. drone_shot_id: int -> reference to drone_shot schema
            3. location_id : int -> reference to location schema
            4. booking_id : int

        Example : 
            {
                "customer_id": "CUST00000001",
                "drone_shot_id": "DRST00000001",
                "location_id": "LOC00000001",
                "booking_id": "BKNG00000001"
            }
---------------------------------------------------------------


******************** Endpoints **************************

    customer:
        get single customer -> /api/customer/{customer_id}
        delete customer     -> /api/customer/{customer_id}
        update customer     -> /api/customer/{customer_id}
        create customer     -> /api/customer
        get all customers   -> /api/customer


    droneshot:
        get single drone_shot   -> /api/drone_shot/{drone_shot_id}
        delete drone_shot       -> /api/drone_shot/{drone_shot_id}
        update drone_shot       -> /api/drone_shot/{drone_shot_id}
        create drone_shot       -> /api/drone_shot
        get all drone_shots     -> /api/drone_shot


    location:
        get single location -> /api/location/{location_id}
        delete location     -> /api/location/{location_id}
        update location     -> /api/location/{location_id}
        create location     -> /api/location
        get all locations   -> /api/location


    booking:
        get single booking -> /api/booking/{booking_id}
        delete booking     ->  /api/booking/{booking_id}
        update booking     -> /api/booking/{booking_id}
        create booking     -> /api/booking
        get all bookings   -> /api/booking

 Features:
    1. All CRUD operations
    2. req body validation
    3. proper error messages
    4. Database: json files
--------------------------------------------------------------

**********  sample db format ********************************

    DB/
        customer/
            cust0000001.json
            cust0000002.json

        droneshot/
            DRST0000001.json
            DRST0000002.json
        location/
            LOC0000001.json
            LOC0000002.json
        booking/
            BKNG0000001.json
            BKNG0000002.json


sample file content:
    customer:
    {

        {   name": "Jangam Harish", 
            "email": "jangam@gmail.com", 
            "phone_number": "8947274719", 
            "address": "3-45, Fathepur", 
            "active": true, "
            "customer_id": "CUST00000001"
        }
    }

    drone_shot: 
    {
        {
            "drone_id": 29219292852,
            "nick_name": "skyhigh",
            "shot_type": "180-degree shot",
            "specifications": "In this cinematic shot, two or more characters must be in the same imaginary line with each other.",
            "price": 4000,
            "active": true
        }
    }

    location:
    {
        {
            "address": "3,52 uppal",
            "city": "hyderabad",
            "district": "rangareddy",
            "state": "telangana",
            "pincode": 506167
        }
    }

    booking:
    {
        {
            "customer_id": "CUST00000001",
            "drone_shot_id": "DRST00000001",
            "location_id": "LOC00000001",
            "booking_id": "BKNG00000001"
        }
    }
    

********* Start Application ***************
Github link: {link}
Demo link: {link}
requrements:
    1. python, flask

steps:
    1. clone the repository
        cmd: git clone {githublink}
    
    2. install python
    3. install flask 
        cmd: pip install flask
    
    4. run the application:
        cmd python app.py
        - application runs at 127.0.0.1:5000
        
    




        